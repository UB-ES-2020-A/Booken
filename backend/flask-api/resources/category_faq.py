from flask_restful import Resource, reqparse
from models.category_faq import CategoryModel


class Category_FAQ(Resource):

    def get(self, idd):
        cat = CategoryModel.find_by_id(idd)
        if cat:
            return {'Category': cat.json()},200
        return {'message': "Category with id [{}] Not found".format(idd)}, 409

    def post(self):
        # Create a new faq with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('type', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        # The ID is the following to the last one
        if CategoryModel.type_exist(data.get('type')):
            return {'message': "Category with type [{}] exists  ".format(data.get('type'))}, 409
        else:
            new_cat = CategoryModel(data.get('type'))
            new_cat.save_to_db()
            return {'message': "OK"}, 200


class Category_FAQ_list(Resource):
    def get(self):
        return CategoryModel.get_categories(), 200 if CategoryModel.get_categories() else 404