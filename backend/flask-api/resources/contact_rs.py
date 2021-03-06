from flask_restful import Resource, reqparse
from models.contact import ContactModel

from models.accounts import auth

class Contact(Resource):
    # Get: Returns a contact_query information
    @auth.login_required(role='dev_manager')
    def get(self, idd):
        contact = ContactModel.find_by_id(idd)
        if contact:
            return {"contact": contact.json()}, 200

        return {"Error: ": "Contact information not found"}, 404

    # Post: Adds a contact_query to our database
    def post(self):
        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('full_name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('phone_number', required=True, type=int, help="This field cannot be left blanck")
        parser.add_argument('contact_query', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        contact = ContactModel(data['full_name'], data['email'], data['phone_number'], data['contact_query'])

        contact.save_to_db()
        return {"Message": "Contact saved correctly"}, 200

    # Delete: Deletes an account from the database
    @auth.login_required(role='dev_manager')
    def delete(self, idd):
        contact = ContactModel.find_by_id(idd)
        if not contact:
            return {'Message': 'Contact with id [{}] not found'.format(idd)}, 404
        contact.delete_from_db()
        return {'Message': 'Contact with id[{}] deleted correctly'.format(idd)}, 200


class ContactList(Resource):
    @auth.login_required(role='dev_manager')
    def get(self):
        contacts = []
        for a in ContactModel.query.all():
            contacts.append(a.json())
        return {"contacts": contacts}, 200
