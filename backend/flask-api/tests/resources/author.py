from flask import Flask
from flask_restful import Resource, Api, reqparse
import datetime
from models.author import AuthorModel


class Author(Resource):

    def get(self, idd):
        author = AuthorModel.find_by_id(idd)
        if author:
            return {'author': author.json()}
        return {'message': "Author with id [{}] Not found".format(idd)}, 409

    def post(self):
        # Create a new author with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('birth_date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        exists = AuthorModel.find_by_name(data.name)
        if exists:
            return {'message': "Author already exists"}, 409

        # The ID is the following to the last one
        new_author = AuthorModel(data.get('name'), data.get('birth_date'), data.get('city'), data.get('country'))
        new_author.save_to_db()
        return {'message': "OK"}, 201

    def delete(self, idd):
        author = AuthorModel.find_by_id(idd)
        if author:
            author.delete_from_db()
            return {'message': "OK"}, 201
        return {'message': "Artist with id [{}] Not found".format(idd)}, 409

    def put(self, idd):

        # Create a new author with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('birth_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), required=True,
                            help="This field cannot be left blanck")
        parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        author = AuthorModel.find_by_id(idd)
        if author:
            author.delete_from_db()
            new_author = AuthorModel(data.get('name'), data.get('birth_date'), data.get('city'), data.get('country'))
            new_author.save_to_db()
            return {'message': "Author modified"}, 201
        return {'message': "Author with id [{}] Not found".format(idd)}, 409


class AuthorList(Resource):
    def get(self):
        return AuthorModel.get_author(), 200 if AuthorModel.get_author() else 404
