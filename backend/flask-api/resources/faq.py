from flask_restful import Resource, reqparse
from models.faq import FAQModel
from models.category_faq import CategoryModel

class FAQ(Resource):

    def get(self, idd):
        faq = FAQModel.find_by_id(idd)
        if faq:
            return {'faq': faq.json()},200
        return {'message': "Faq with id [{}] Not found".format(idd)}, 404

    def post(self):
        # Create a new faq with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('category', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('question', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('answer', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        if CategoryModel.type_exist(data.get('category')):
            cat = CategoryModel.find_by_type(data.get('category'))
            cat.add_faq()
            cat.save_to_db()
        else:
            cat = CategoryModel(data.get('category'))
            cat.add_faq()
            cat.save_to_db()
        new_faq = FAQModel(cat,data.get('question'), data.get('answer'))
        new_faq.save_to_db()
        return {'message': "OK"}, 200

    def delete(self, idd):
        faq = FAQModel.find_by_id(idd)
        if faq:
            id_cat = faq.category[0].id
            cat_aux = CategoryModel.find_by_id(id_cat)
            cat_aux.num_faq -= 1
            cat_aux.save_to_db()
            if cat_aux.num_faq <= 0:
                # Si no tiene faq la eliminamos
                cat_aux.delete_from_db()
            faq.delete_from_db()

            return {'message': "OK"}, 200
        return {'message': "Faq with id [{}] Not found".format(idd)}, 404

    def put(self, idd):

        # Create a new faq with the data passed to us.
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        # define all input parameters need and its type
        parser.add_argument('category', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('question', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('answer', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        faq = FAQModel.find_by_id(idd)
        if faq:
            id_cat = faq.category[0].id
            cat_aux = CategoryModel.find_by_id(id_cat)
            cat_aux.num_faq -= 1
            cat_aux.save_to_db()
            if cat_aux.num_faq <= 0:
                # Si no tiene faq la eliminamos
                cat_aux.delete_from_db()

            if CategoryModel.type_exist(data.get('category')):
                cat = CategoryModel.find_by_type(data.get('category'))
            else:
                cat = CategoryModel(data.get('category'))
            cat.num_faq += 1
            faq.category += [cat]
            faq.question = data.get('question')
            faq.answer = data.get('answer')
            cat.save_to_db()
            faq.save_to_db()
            return {'message': "FAQ modified"}, 200
        return {'message': "FAQ with id [{}] Not found".format(idd)}, 404

class FAQList(Resource):
    def get(self):
        return FAQModel.get_faqs(), 200