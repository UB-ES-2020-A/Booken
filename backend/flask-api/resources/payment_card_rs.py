from flask import Flask
from flask_restful import Resource, Api, reqparse

from models.payment_card import CardModel
from models.accounts import AccountModel


class Card(Resource):

    def get(self, account_id, idd):
        account = AccountModel.find_by_id(account_id)
        card = CardModel.find_by_id(idd)

        if card is not None and account is not None:
            if card in account.cards:
                return {'card': card.json()}, 200
            return {'message': "This account doesn't have a card with id [{}] ".format(idd)}, 409
        elif card is None:
            return {'message': "Card with id [{}] Not found".format(idd)}, 404
        return {'message': "Account with id [{}] Not found".format(idd)}, 404

    def post(self, account_id, idd=None):
        parser = reqparse.RequestParser()

        account = AccountModel.find_by_id(account_id)
        if account is None:
            return {'message': "Account with id [{}] Not found".format(account_id)}, 404

        if len(account.cards) == 2:
            return {'message': "Account with id [{}] cannot have more cards".format(account_id)}, 403

        # define the input parameters need and its type
        parser.add_argument('card_owner', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('number', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('payment_method', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        card = CardModel(data['card_owner'], data['number'], data['date'], data['payment_method'])

        account.cards.append(card)


        account.save_to_db()
        return {"Message": "Card saved correctly"}, 200

    def delete(self, account_id, idd):
        account = AccountModel.find_by_id(account_id)
        card = CardModel.find_by_id(idd)

        if card is not None and account is not None:
            if card in account.cards:
                card.delete_from_db()
                return {"Message": "Card deleted correctly"}, 200
            return {'message': "This account doesn't have an card with id [{}] ".format(idd)}, 409
        elif card is None:
            return {'message': "Card with id [{}] Not found".format(idd)}, 404
        return {'message': "Account with id [{}] Not found".format(idd)}, 404


class CardList(Resource):
    def get(self, account_id):
        account = AccountModel.find_by_id(account_id)
        cards = []
        for a in account.cards:
            cards.append(a.json())
        return {"accounts_cards": cards}, 200
