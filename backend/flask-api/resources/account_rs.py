from flask_restful import Resource, reqparse
from flask import g

from models.accounts import AccountModel, auth


class Account(Resource):
    # Get: Returns the account information
    def get(self, idd):
        account = AccountModel.find_by_id(idd)
        if account:
            return {"account": account.json()}, 200
        return {"error: ": "Account not found"}, 404

    # Post: Adds an account to our database
    def post(self):
        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('lastname', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', required=True, type=str, help="This field cannot be left blank")

        data = parser.parse_args()
        if AccountModel.find_by_email(data['email']):
            return {"message": "Account already registered for that email address"}, 409
        account = AccountModel(data['email'], data['name'], data['lastname'], data['password'])
        account.save_to_db()
        return {"message": "Account saved correctly"}, 200

    @auth.login_required
    def put(self, idd):
        account = AccountModel.find_by_id(idd)
        if account:
            if g.user != account:
                return {"error: ": "You cannot modify an account which you are not log with"}, 401
        else:
            return {"error: ": "Account not found"}, 404

        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('lastname', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        data = parser.parse_args()
        if AccountModel.find_by_email(data['email']):
            return {"message": "Account already registered for that email address"}, 409

        account.name, account.lastname, account.email = data['name'], data['lastname'], data['email']

        account.save_to_db()
        return {"message": "Account saved correctly"}, 200

    # Delete: Deletes an account from the database
    def delete(self, idd):
        account = AccountModel.find_by_id(idd)
        if not account:
            return {'message': 'Account with id [{}] not found'.format(idd)}, 404

        tmp = [add.delete_from_db() for add in account.addresses]
        tmp = [rev.delete_from_db() for rev in account.reviews]
        tmp = [c.delete_from_db() for c in account.cards]
        tmp = [o.delete_from_db() for o in account.orders]

        account.delete_from_db()

        return {'message': 'Account with id[{}] deleted correctly'.format(idd)}, 200


class Accounts(Resource):
    def get(self):
        accounts = []
        for a in AccountModel.query.all():
            accounts.append(a.json())
        return {"accounts": accounts}, 200


class PasswordChange(Resource):
    @auth.login_required
    def put(self, idd):
        account = AccountModel.find_by_id(idd)
        if account:
            if g.user != account:
                return {"error: ": "You cannot modify an account which you are not log with"}, 401

        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('old_password', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('new_password', type=str, required=True, help="This field cannot be left blank")

        data = parser.parse_args()

        if account.verify_password(data["old_password"]):
            account.hash_password(data['new_password'])
            account.save_to_db()
            return {"message": "Password changed correctly"}, 200
        return {'message': "Incorrect password"}, 406
