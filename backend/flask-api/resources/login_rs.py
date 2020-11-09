from flask_restful import Resource, reqparse

from models.accounts import AccountModel


class Login(Resource):

    def post(self):

        parser = reqparse.RequestParser()  # create parameters parser from request

        # define the input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('password', required=True, type=str, help="This field cannot be left blanck")

        data = parser.parse_args()

        account = AccountModel.find_by_email(data["email"])

        if account:
            if account.verify_password(data["password"]):
                token = account.generate_auth_token()
                return {'token': token.decode('ascii')}, 200
            else:
                return {'message': "Password is invalid"}, 400
        else:
            return {'message': "Account with email [{}] Not found".format(data["email"])}, 404
