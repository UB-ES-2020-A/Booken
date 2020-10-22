from flask import Flask
from flask_restful import Resource, Api, reqparse
import datetime
from models.author import AuthorModel

class Author(Resource):

    def get(self, id):
        author = AuthorModel.find_by_id(id)
        if (author!=None):
            return {'author': author.json()}
        else:
            return {'message': "Author with id [{}] Not found".format(id)}, 409

    def post(self, id=None):
        # Create a new author with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('birth_date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        new_id = { 'id': AuthorModel.num_authors()}
        if (id != None):
            # If they passed an id, find out if already exists
            exists = AuthorModel.find_by_id(id)
            if exists:
                return {'message': "Author with id [{}] Not found".format(id)}, 409
            else:
                new_id = {'id': id}

        # The ID is the following to the last one
        new_author = AuthorModel(new_id['id'], data.name, data.birth_date, data.city, data.country)
        new_author.save_to_db()
        return {'message': "OK"}, 201

    def delete(self, id):
        author = AuthorModel.find_by_id(id)
        if author:
            author.delete_from_db()
            return {'message': "OK"}, 201
        else:
            return {'message': "Artist with id [{}] Not found".format(id)}, 409

    def put(self, id):

        # Create a new author with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('birth_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), required=True,
                            help="This field cannot be left blanck")
        parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        author = AuthorModel.find_by_id(id)
        if author:
            author.delete_from_db()
            new_author =  AuthorModel(id, data.name, data.birth_date, data.city, data.country)
            new_author.save_to_db()
            return {'message': "Author modified"}, 201
        else:
            return {'message': "Author with id [{}] Not found".format(id)}, 409

class AuthorList(Resource):
    def get(self):
        return AuthorModel.get_author(), 200 if AuthorModel.get_author() else 404