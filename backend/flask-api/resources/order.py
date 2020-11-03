from db import db
from models.book import BookModel
from models.accounts import AccountModel
from models.orders import OrdersModel
from flask_restful import Resource, reqparse
from models.accounts import auth, g

class Orders(Resource):
    def get(self, email):
        order = OrdersModel.find_by_email(email)
        if order:
            list = []
            for i in order:
                list.append(i.json())
            return {"orders": list}, 200
        else:
            return {'message': "The user with email [{}] hasn't got any order".format(email)}, 409
    def post(self, email):
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('id_book', type=int, required=True, help="This field cannot be left blanck")
        parser.add_argument('num_books', type=int, required=True, help="This field cannot be left blanck")
        data = parser.parse_args()
        acc = AccountModel.find_by_email(email)
        book = BookModel.find_by_id(data.id_book)
        if (book == None):
            return {'message': "There isn't book with this id"}, 409
        if (acc == None):
            return {'message': "There isn't a user with this email"}, 409

        tickets = book.total_available - data.num_books
        book.total_available = tickets
        new_order = OrdersModel(data.id_book, data.num_books)
        acc.orders.append(new_order)
        db.session.add(new_order)
        db.session.add(book)
        db.session.add(acc)

        if ( book.total_available < 0 ) :
            db.session.rollback()
            return {'message': "There isn't enought books"}, 409

        else:
            db.session.commit()
            return new_order.json(), 200

    @auth.login_required(role=['dev_manager', 'stock_manager', 'client'])
    def delete(self, id):
        order = OrdersModel.find_by_id(id)
        if order:
            order.delete_from_db()
            return {'message': "OK"}, 200
        else:
            return {'message': "Event with id [{}] Not found".format(id)}, 409

class OrdersList(Resource):
    def get(self):
        orders = OrdersModel.get_orders()
        return orders, 200 if orders else 404