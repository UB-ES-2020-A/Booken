from flask_restful import Resource, reqparse

from models.contact import ContactModel

class Contact(Resource):
    #Get: Returns a contact_query information
    def get(self,id):
        contact = ContactModel.find_by_id(id)
        if(contact != None):
            return {"contact": contact.json()}, 200
        else:
            return {"Error: ": "Contact information not found"}, 400

    #Post: Adds a contact_query to our database
    def post(self):
        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('full_name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('phone_number', required=True, type=int, help="This field cannot be left blanck")
        parser.add_argument('contact_query', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        contact = ContactModel(data['full_name'], data['email'], data['phone_number'], data['contact_query'])

        try:
            contact.save_to_db()
            return {"Message": "Contact saved correctly"}, 200
        except:
            return {"Message": "Coudln't save changes"}, 500


    #Delete: Deletes an account from the database
    def delete(self, id):
        contact = ContactModel.find_by_id(id)
        if(contact==None):
            return{'Message':'Contact with id [{}] not found'.format(id)}, 404

        contact.delete_from_db()

        return{'Message':'Contact with id[{}] deleted correctly'.format(id)}, 200

class ContactList(Resource):
    def get(self):
        contacts = []
        for a in ContactModel.query.all():
            contacts.append(a.json())
        return{"contacts": contacts}, 200
