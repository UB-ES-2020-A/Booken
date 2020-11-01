from flask_restful import Resource, reqparse

from models.accounts import AccountModel, auth

class Account(Resource):
    #Get: Returns the account information
    def get(self, id):
        account = AccountModel.find_by_id(id)
        if(account != None):
            return {"account": account.json()}, 200
        else:
            return{"Error: ": "Account not found"}, 400

    #Post: Adds an account to our database
    def post(self):
        parser = reqparse.RequestParser()

        #define the input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('lastname', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('password', required=True, type=str, help="This field cannot be left blanck")

        data = parser.parse_args()
        account = AccountModel(data['email'],data['name'],data['lastname'],data['password'])

        try:
            account.save_to_db()
            return{"Message":"Account saved correctly"}, 200
        except:
            return{"Message": "Coudln't save changes"}, 500

    #Delete: Deletes an account from the database
    def delete(self, id):
        account = AccountModel.find_by_id(id)
        if(account==None):
            return{'Message':'Account with id [{}] not found'.format(id)}, 404

        #TODO: remove orders as well
        #TODO: remove wish list as well

        account.delete_from_db()

        return{'Message':'Account with id[{}] deleted correctly'.format(id)}, 200

class Accounts(Resource):
    def get(self):
        accounts = []
        for a in AccountModel.query.all():
            accounts.append(a.json())
        return{"Accounts": accounts}, 200
