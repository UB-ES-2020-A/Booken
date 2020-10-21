from flask import Flask
from flask_restful import Resource, Api, reqparse
import datetime
from data import authors

class Author(Resource):

    def get(self, id):
        author = next(filter(lambda x: x['id'] == id, authors), None)
        return {'author': author}, 200 if author else 404

    def post(self, id=None):
        # Create a new author with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('birth_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), required=True, help="This field cannot be left blanck")
        parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        new_id = { 'id': len(authors)}

        if (id != None):
            # If they passed an id, find out if already exists
            exists = any([id == dictio['id'] for dictio in authors])
            if exists:
                return {'message': "Author with id [{}] Not found".format(id)}, 409
            else:
                new_id = {'id': id}

        # The ID is the following to the last one
        new_author = dict()
        new_author.update(new_id)
        new_author.update(data)
        authors.append(new_author)
        return {'message': "OK"}, 201

    def delete(self, id):
        exists_list = [id == dictio['id'] for dictio in authors]
        exists = any(exists_list)
        if exists:
            authors.pop(exists_list.index(True))
            return {'message': "OK"}, 201
        else:
            return {'message': "Artist with id [{}] Not found".format(id)}, 409

    def put(self, id):

        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('birth_date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), required=True,
                            help="This field cannot be left blanck")
        parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        exists_list = [id == dictio['id'] for dictio in authors]
        exists = any(exists_list)
        if exists:
            new_id = {'id': id}
            new_author = dict()
            new_author.update(new_id)
            new_author.update(data)
            authors[exists_list.index(True)].update(new_author)
            return {'message': "Author modified"}, 201
        else:
            # The ID is the following to the last one
            new_id = {'id': len(authors)}
            new_artist = dict()
            new_artist.update(new_id)
            new_artist.update(data)
            authors.append(new_artist)
            return {'message': "Author created with id [{}]".format(new_id['id'])}, 201