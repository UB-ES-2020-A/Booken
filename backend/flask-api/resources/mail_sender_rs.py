import smtplib

from flask_restful import Resource, reqparse

from models.accounts import AccountModel, auth
from models.orders import OrdersModel
from models.contact import ContactModel
from utils.mail_sender import MailSender

class SendContactResponse(Resource):

    @auth.login_required(role="dev_manager")
    def post(self,):
        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('contact_id', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('contact_response', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        contact_id, contact_response = data['contact_id'], data['contact_response']

        contact = ContactModel.find_by_id(contact_id)

        if contact:
            try:
                MailSender.send_contact_response_mail(
                    contact.email,
                    contact.full_name,
                    contact.contact_query,
                    contact_response
                )

                contact.delete_from_db()
                return {"message":"Email sended correctly"}, 200
            except (FileNotFoundError, smtplib.SMTPException) as e:
                print(e)
                return {'message': 'Something went wrong'}, 500
        else:
            return {"message":"Contact not found"}, 404

class SendTicket(Resource):

    @auth.login_required
    def post(self,):
        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('account_id', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('order_id', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        account_id, order_id = data['account_id'], data['order_id']

        account = AccountModel.find_by_id(account_id)
        order = OrdersModel.find_by_id(order_id)

        if account and order:
            try:
                MailSender.send_ticket_order_mail(account.email, account.name, order)

                return {"message":"Email sended correctly"}, 200
            except (FileNotFoundError, smtplib.SMTPException) as e:
                print(e)
                return {'message': 'Something went wrong'}, 500
        else:
            return {"message":"Account or Order not found"}, 404