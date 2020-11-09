from db import db
from models.book import BookModel
from models.accounts import AccountModel
from models.orders import OrdersModel
from flask_restful import Resource, reqparse
from models.accounts import auth, g


class Orders(Resource):
    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, email):
        orders = [a.json() for a in OrdersModel.find_by_email(email)]
        if orders:
            return {"orders": orders}, 200
        else:
            return {'message': "The user with email [{}] hasn't got any order".format(email)}, 409

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def post(self, email):
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('id_book', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('num_books', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=str, required=True, help="This field cannot be left blank")
        data = parser.parse_args()
        acc = AccountModel.find_by_email(email)
        book = BookModel.find_by_id(data.id_book)
        if not book:
            return {'message': "There isn't book with this id"}, 409
        if not acc:
            return {'message': "There isn't a user with this email"}, 409

        tickets = book.total_available - data.num_books
        book.total_available = tickets
        new_id = OrdersModel.num_orders()
        new_order = OrdersModel(new_id, email, data.id_book, data.num_books, data.state)
        acc.orders.append(new_order)
        db.session.add(new_order)
        db.session.add(book)
        db.session.add(acc)

        if book.total_available < 0:
            db.session.rollback()
            return {'message': "There isn't enough books"}, 409
        else:
            db.session.commit()
            return new_order.json(), 200

    # @auth.login_required(role=['dev_manager', 'stock_manager', 'client'])
    def delete(self, id):
        order = OrdersModel.find_by_id(id)
        if order:
            order.delete_from_db()
            return {'message': "OK"}, 200
        else:
            return {'message': "Event with id [{}] Not found".format(id)}, 409

    # @auth.login_required(role=['dev_manager', 'stock_manager'])
    def put(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('id_book', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('num_books', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('state', type=str, required=True, help="This field cannot be left blank")
        data = parser.parse_args()
        order = OrdersModel.find_by_id(id)
        email = order.email
        order.delete_from_db()
        new_order = OrdersModel(id, email, data.id_book, data.num_books, data.state)
        db.session.add(new_order)
        db.session.commit()
        return new_order.json(), 200


# @auth.login_required(role=['dev_manager', 'stock_manager'])
class OrdersList(Resource):
    def get(self):
        orders = OrdersModel.get_orders()
        return orders, 200 if orders else 404
