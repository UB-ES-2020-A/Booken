from flask import Flask
from flask_restful import Resource, Api, reqparse

from models.payment_card import CardModel
from models.accounts import AccountModel


class Card(Resource):

    def get(self, account_id, id):
        account = AccountModel.find_by_id(account_id)
        card = CardModel.find_by_id(id)

        if (card != None and account != None):
            if (card in account.cards):
                return {'card': card.json()}, 200
            else:
                return {'message': "This account doesn't have a card with id [{}] ".format(id)}, 409

        elif (card == None):
            return {'message': "Card with id [{}] Not found".format(id)}, 404

        else:
            return {'message': "Account with id [{}] Not found".format(id)}, 404

    def post(self, account_id, id=None):
        parser = reqparse.RequestParser()

        account = AccountModel.find_by_id(account_id)
        if (account == None):
            return {'message': "Account with id [{}] Not found".format(account_id)}, 404

        if (len(account.cards) == 2):
            return {'message': "Account with id [{}] cannot have more cards".format(account_id)}, 404

        # define the input parameters need and its type
        parser.add_argument('card_owner', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('number', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('payment_method', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        card = CardModel(data['card_owner'],data['number'],data['date'],data['payment_method'])

        account.cards.append(card)

        try:
            account.save_to_db()
            return {"Message": "Card saved correctly"}, 200
        except:
            return {"Message": "Coudln't save changes"}, 500

    def delete(self, account_id, id):
        account = AccountModel.find_by_id(account_id)
        card = CardModel.find_by_id(id)

        if (card != None and account != None):
            if (card in account.cards):
                try:
                    card.delete_from_db()
                    return {"Message": "Card deleted correctly"}, 200
                except:
                    return {"Message": "Coudln't save changes"}, 500

            else:
                return {'message': "This account doesn't have an card with id [{}] ".format(id)}, 409

        elif (card == None):
            return {'message': "Card with id [{}] Not found".format(id)}, 404

        else:
            return {'message': "Account with id [{}] Not found".format(id)}, 404


class CardList(Resource):
    def get(self, account_id):
        account = AccountModel.find_by_id(account_id)
        cards = []
        for a in account.cards:
            cards.append(a.json())
        return {"accounts_cards": cards}, 200
