from flask_restful import Resource, reqparse

from models.accounts import AccountModel, auth


class Account(Resource):
    # Get: Returns the account information
    def get(self, id):
        account = AccountModel.find_by_id(id)
        if account:
            return {"account": account.json()}, 200
        else:
            return {"error: ": "Account not found"}, 400

    # Post: Adds an account to our database
    def post(self):
        parser = reqparse.RequestParser()

        # define the input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('lastname', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', required=True, type=str, help="This field cannot be left blank")

        data = parser.parse_args()
        account = AccountModel(data['email'], data['name'], data['lastname'], data['password'])

        try:
            account.save_to_db()
            return {"message": "Account saved correctly"}, 200
        except:
            account.db_rollback()
            return {"message": "Couldn't save changes"}, 500

    # Delete: Deletes an account from the database
    def delete(self, id):
        account = AccountModel.find_by_id(id)
        if not account:
            return {'message': 'Account with id [{}] not found'.format(id)}, 404

        [add.delete_from_db() for add in account.addresses]
        [rev.delete_from_db() for rev in account.reviews]
        [c.delete_from_db() for c in account.cards]
        [o.delete_from_db() for o in account.orders]
        # TODO: remove wish list as well

        account.delete_from_db()

        return {'message': 'Account with id[{}] deleted correctly'.format(id)}, 200


class Accounts(Resource):
    def get(self):
        accounts = []
        for a in AccountModel.query.all():
            accounts.append(a.json())
        return {"accounts": accounts}, 200
