import smtplib

from flask_restful import Resource, reqparse

from models.contact import ContactModel
from utils.mail_sender import MailSender
import os

class SendContactResponse(Resource):

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
                print(e, os.getcwd())
                return {'message': 'Something went wrong'}, 500
        else:
            return {"message":"Contact not found"}, 404