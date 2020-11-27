from db import db
from models.address import AddressModel
from models.book import BookModel
from models.accounts import AccountModel
from models.articles import ArticlesModel
from flask_restful import Resource, reqparse
from models.orders import OrdersModel


class Orders(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, idd):
        order = OrdersModel.find_by_id(idd)
        if order:
            return {"orders": order.json()}, 200
        return {'message': "Order with id [{}] doesn't exist".format(idd)}, 409

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def post(self, idd):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('total', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('shipping', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('taxes', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blanck")
        parser.add_argument('send_type', type=int, required=True, help="This field cannot be left blanck")
        parser.add_argument('card_id', type=int, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        acc = AccountModel.find_by_id(idd)

        if (data.state < 0 or data.state > 2):
            return {'message': "Order with state [{}] not supported".format(data.state)}, 400
        if (data.send_type < 0 or data.send_type > 2):
            return {'message': "Order with send type [{}] not supported".format(data.state)}, 400
        if not acc:
            return {'message': "There isn't a user with this id"}, 409

        # new_id = OrdersModel.num_orders()
        new_order = OrdersModel(idd, data.date, data.total, data.shipping, data.taxes, data.state, data.send_type,
                                data.card_id)
        acc.orders.append(new_order)
        db.session.add(new_order)
        db.session.commit()
        return new_order.id, 200

    # @auth.login_required(role=['dev_manager', 'stock_manager', 'client'])
    def delete(self, idd):
        order = OrdersModel.find_by_id(idd)
        if order:
            order.delete_from_db()
            return {'message': "OK"}, 200
        return {'message': "Order with id [{}] Not found".format(idd)}, 409

    # @auth.login_required(role=['dev_manager', 'stock_manager'])
    def put(self, idd):
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type

        parser.add_argument('state', type=int, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        order = OrdersModel.find_by_id(idd)

        if order:
            id_user = order.id_user
            order.delete_from_db()
            new_order = OrdersModel(id_user, order.date, order.total, order.shipping, order.taxes, data.state,
                                    order.send_type, order.card_id)
            db.session.add(new_order)
            db.session.commit()
            return new_order.json(), 200
        return {'message': "Order not found"}, 400


# @auth.login_required(role=['dev_manager', 'stock_manager'])
class OrdersList(Resource):
    def get(self):
        orders = OrdersModel.get_orders()
        return orders, 200 if orders else 404


# articles list of an order
class OrderArticlesList(Resource):
    def get(self, idd):
        try:
            return {"articles": OrdersModel.find_by_id(idd).json()["articles"]}, 200
        except:
            return {"message": "Order with id [{}] Not Found".format(idd)}, 404


# articles of an order
class OrderArticles(Resource):

    def get(self, idd, id_article):
        order = OrdersModel.find_by_id(idd)
        if order is None:
            return {"message": "Order with id [{}] not found ".format(idd)}, 404
        articles = order.json()["articles"]
        article_list = [articles[i] for i in range(len(articles)) if articles[i]["id"] == int(id_article)]
        try:
            article = article_list[0]
            return article, 200
        except:
            return {"message": "Article with id [{}] Not found in Order with id [{}]".format(id_article, idd)}, 404

    # @auth.login_required(role='admin')
    def post(self, idd):
        order = OrdersModel.find_by_id(idd)
        if order is None:
            return {"message": "Order with id [{}] not found ".format(idd)}, 404

        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('id_book', type=int, required=True, help="This field cannot be left blanck")
        parser.add_argument('quant', type=int, required=True, help="This field cannot be left blanck")
        data = parser.parse_args()
        book = BookModel.find_by_id(data.id_book)
        if book:
            if book.total_available > data.quant:
                book.num_sales += data.quant
                book.total_available -= data.quant
                book.save_to_db()
                article = ArticlesModel(data.price)
                order.add_article(article)
                article.save_to_db()
                return article.id, 200
            return {"message": "Not enought books with id [{}] for the order".format(data.id_book)}, 404
        return {"message": "Book with id [{}] not found ".format(data.id_book)}, 404

    # @auth.login_required(role='admin')
    def delete(self, idd, id_article):
        order = OrdersModel.find_by_id(idd)
        listt = [order.json()["articles"][i]["id"] == int(id_article) for i in
                 range(len(order.json()["articles"]))]
        if len(listt) == 0:
            return {"message": "Article with id [{}] not in Order with id [{}]".format(id_article, idd)}
        if not True in listt:
            return {"message": "Article with id [{}] not in Order with id [{}]".format(id_article, idd)}
        index = listt.index(True)
        if index is not None:
            deleted = order.delete_article(id_article)
            if deleted:
                return {'message': "OK"}, 201

        return {'message': "Article with id [{}] Not found in order with id [{}]".format(id_article, id)}, 409


# adress list of an order
class OrderAddressList(Resource):
    def get(self, idd):
        try:
            return {"addresses": OrdersModel.find_by_id(idd).json()["address"]}, 200
        except:
            return {"message": "Order with id [{}] Not Found".format(idd)}, 404


# articles of an order
class OrderAddress(Resource):

    def get(self, idd, id_sub):
        order = OrdersModel.find_by_id(idd)
        if order is None:
            return {"message": "Order with id [{}] not found ".format(idd)}, 404
        addresses = order.json_with_address_id()["address"]
        address_list = [addresses[i] for i in range(len(addresses)) if addresses[i]["id"] == int(id_sub)]
        try:
            address = address_list[0]
            return address, 200
        except:
            return {"message": "Address with id [{}] Not found in Order with id [{}]".format(id_sub, id)}, 404

    # @auth.login_required(role='admin')
    def post(self, idd, id_sub, address_id=None):
        order = OrdersModel.find_by_id(idd)
        account = AccountModel.find_by_id(id_sub)
        if account is None:
            return {'message': "Account with id [{}] Not found".format(id_sub)}, 404
        if order is None:
            return {"message": "Order with id [{}] not found ".format(idd)}, 404
        # Si no pasamos address id por parametro pedimos los parametros para crear una nueva direccion
        address = None
        if address_id is None:
            if len(account.addresses) == 3:
                return {'message': "Account with id [{}] cannot have more addresses".format(id_sub)}, 404
            parser = reqparse.RequestParser()
            # define the input parameters need and its type
            parser.add_argument('label_name', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('surnames', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('street', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('number', type=int, required=True, help="This field cannot be left blanck")
            parser.add_argument('cp', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('city', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('province', type=str, required=True, help="This field cannot be left blanck")
            parser.add_argument('telf', type=int, required=True, help="This field cannot be left blanck")

            data = parser.parse_args()
            address = AddressModel(data['label_name'], data['name'], data['surnames'], data['street'], data['number'],
                                   data['cp'], data['city'], data['province'], data['telf'])
            account.addresses.append(address)
        # Si pasamos la id de la direccion la buscamos en la cuenta
        else:
            address = account.find_addres_by_id(address_id)
        if address is not None:
            order.add_address(address)
            order.save_to_db()
            return {'message': "OK"}, 200
        return {'message': "Address with id [{}] Not found".format(address_id)}, 404

    # @auth.login_required(role='admin')
    def delete(self, idd, id_sub):
        order = OrdersModel.find_by_id(idd)
        listt = [order.json()["address"][i]["id"] == int(id_sub) for i in
                 range(len(order.json()["address"]))]
        if len(listt) == 0:
            return {"message": "Address with id [{}] not in Order with id [{}]".format(id_sub, idd)}
        if True not in listt:
            return {"message": "Address with id [{}] not in Order with id [{}]".format(id_sub, idd)}
        index = listt.index(True)
        if index is not None:
            deleted = order.delete_address(id_sub)
            if deleted:
                return {'message': "OK"}, 201
        return {'message': "Address with id [{}] Not found in order with id [{}]".format(id_sub, idd)}, 409


class OrderUser(Resource):
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_id_user(id_user)]
        return {"orders": orders}, 200

    def delete(self, id_user, id_order):
        order = OrdersModel.find_by_id_user_and_orderid(id_user, id_order)
        if order:
            order.delete_from_db()
            return {'message': "OK"}, 200
        return {'message': "Order not found".format(id)}, 409


class InProgressOrders(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_state(0, id_user)]
        return {"orders": orders}, 200


class SendOrders(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_state(1, id_user)]
        return {"orders": orders}, 200


class ReceivedOrders(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_state(2, id_user)]
        return {"orders": orders}, 200


class InProgressOrdersList(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self):
        orders = OrdersModel.get_orders()['orders']
        orders_list = [order for order in orders if order['state'] == 0]
        return {'orders': orders_list}, 200


class SendOrdersList(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self):
        orders = OrdersModel.get_orders()['orders']
        orders_list = [order for order in orders if order['state'] == 1]
        return {'orders': orders_list}, 200


class ReceivedOrdersList(Resource):

    # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self):
        orders = OrdersModel.get_orders()['orders']
        orders_list = [order for order in orders if order['state'] == 2]
        return {'orders': orders_list}, 200
