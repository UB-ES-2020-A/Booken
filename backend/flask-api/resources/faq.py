from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.faq import FAQModel


class FAQ(Resource):

    def get(self, idd):
        faq = FAQModel.find_by_id(idd)
        if faq:
            return {'faq': faq.json()},200
        return {'message': "Faq with id [{}] Not found".format(idd)}, 409

    def post(self):
        # Create a new faq with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('question', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('answer', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        # The ID is the following to the last one
        new_faq = FAQModel(data.get('question'), data.get('answer'))
        new_faq.save_to_db()
        return {'message': "OK"}, 200

    def delete(self, idd):
        faq = FAQModel.find_by_id(idd)
        if faq:
            faq.delete_from_db()
            return {'message': "OK"}, 200
        return {'message': "Faq with id [{}] Not found".format(idd)}, 409

    def put(self, idd):

        # Create a new faq with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        # define all input parameters need and its type
        parser.add_argument('question', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('answer', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        faq = FAQModel.find_by_id(idd)
        if faq:
            faq.question = data.get('question')
            faq.answer = data.get('answer')
            faq.save_to_db()
            return {'message': "FAQ modified"}, 200
        return {'message': "FAQ with id [{}] Not found".format(idd)}, 409


class FAQList(Resource):
    def get(self):
        return FAQModel.get_faqs(), 200 if FAQModel.get_faqs() else 404