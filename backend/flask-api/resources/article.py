from flask import Flask
from flask_restful import Resource, Api, reqparse

from models.articles import ArticlesModel

from models.accounts import auth, g

class Articles(Resource):

    def get(self, id):
        article = ArticlesModel.find_by_id(id)
        if article:
            return {"article": article.json()}, 200
        else:
            return {'message': "Article with id [{}] Not found".format(id)}, 409

    #@auth.login_required(role='admin')
    def post(self):
        # Create a new artist with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        new_article = ArticlesModel(data.price)
        new_article.save_to_db()
        return {'message': "OK"}, 201

    #@auth.login_required(role='admin')
    def delete(self, id):
        article = ArticlesModel.find_by_id(id)
        if article:
            article.delete_from_db()
            return {'message': "OK"}, 201
        else:
            return {'message': "Article with id [{}] Not found".format(id)}, 409



class ArticlesList(Resource):

    def get(self):
        return ArticlesModel.get_articles(), 200 if ArticlesModel.get_articles() else 404