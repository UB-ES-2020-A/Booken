from db import db
from models.address import AddressModel
from models.book import BookModel
from models.accounts import AccountModel
from models.articles import ArticlesModel
from flask_restful import Resource, reqparse
from models.accounts import auth, g
from models.orders import OrdersModel

class Orders(Resource):

    #@auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id):
        order = OrdersModel.find_by_id(id)
        if order:
            return {"orders": order.json()}, 200
        else:
            return {'message': "Order with id [{}] doesn't exist".format(id)}, 409

   # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def post(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('total', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('shipping', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('taxes', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blanck")
        data = parser.parse_args()
        #acc = AccountModel.find_by_id(id)

        if (data.state < 0 or data.state>2):
            return {'message': "Order with state [{}] not supported".format(data.state)}, 400
        #if (acc == None):
         #   return {'message': "There isn't a user with this id"}, 409

        #new_id = OrdersModel.num_orders()
        new_order = OrdersModel(id, data.date, data.total,data.shipping,data.taxes,data.state)
        #acc.orders.append(new_order)
        db.session.add(new_order)
        db.session.commit()
        return new_order.id, 200


    # @auth.login_required(role=['dev_manager', 'stock_manager', 'client'])
    def delete(self, id):
        order = OrdersModel.find_by_id(id)
        if order:
            order.delete_from_db()
            return {'message': "OK"}, 200
        else:
            return {'message': "Order with id [{}] Not found".format(id)}, 409

    # @auth.login_required(role=['dev_manager', 'stock_manager'])
    def put(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type

        parser.add_argument('date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('total', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('shipping', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('taxes', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('state', type=int, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        order = OrdersModel.find_by_id(id)

        if ( order ) :
            id_user = order.id_user
            order.delete_from_db()
            new_order = OrdersModel(id_user,data.date, data.total, data.shipping, data.taxes, data.state)
            db.session.add(new_order)
            db.session.commit()
            return new_order.json(), 200
        else:
            return {'message': "Order not found"}, 400



# @auth.login_required(role=['dev_manager', 'stock_manager'])
class OrdersList(Resource):
    def get(self):
        orders = OrdersModel.get_orders()
        return orders, 200 if orders else 404


#articles list of an order
class OrderArticlesList(Resource):
    def get(self, id):
        try:
            return {"articles": OrdersModel.find_by_id(id).json()["articles"]}
        except:
            return {"message": "Order with id [{}] Not Found".format(id)}, 404

# articles of an order
class OrderArticles(Resource):

    def get(self, id, id_article):
        order = OrdersModel.find_by_id(id)
        if ( order == None):
            return {"message": "Order with id [{}] not found ".format(id)}, 404
        articles = order.json()["articles"]
        article_list = [articles[i] for i in range(len(articles)) if articles[i]["id"] == int(id_article)]
        try:
            article = article_list[0]
            return article, 200
        except:
            return {"message": "Article with id [{}] Not found in Order with id [{}]".format(id_article, id)}, 404

    #@auth.login_required(role='admin')
    def post(self, id):
        order = OrdersModel.find_by_id(id)
        if order is None:
            return {"message": "Order with id [{}] not found ".format(id)}, 404

        parser = reqparse.RequestParser()  # create parameters parser from request
        # define all input parameters need and its type
        parser.add_argument('price', type=float, required=True, help="This field cannot be left blanck")
        data = parser.parse_args()
        article = ArticlesModel(data.price)
        order.add_article(article)
        article.save_to_db()
        return article.id, 200


   # @auth.login_required(role='admin')
    def delete(self, id, id_article):
        order = OrdersModel.find_by_id(id)
        list = [order.json()["articles"][i]["id"] == int(id_article) for i in
                range(len(order.json()["articles"]))]
        if len(list) == 0:
            return {"message": "Article with id [{}] not in Order with id [{}]".format(id_article, id)}
        if not True in list:
            return {"message": "Article with id [{}] not in Order with id [{}]".format(id_article, id)}
        index = list.index(True)
        if index is not None:
            deleted = order.delete_article(id_article)
            if deleted:
                return {'message': "OK"}, 201

        return {'message': "Article with id [{}] Not found in order with id [{}]".format(id_article, id)}, 409


#adress list of an order
class OrderAddressList(Resource):
    def get(self, id):
        try:
            return {"addresses": OrdersModel.find_by_id(id).json()["address"]}
        except:
            return {"message": "Order with id [{}] Not Found".format(id)}, 404

# articles of an order
class OrderAddress(Resource):

    def get(self, id, id_sub):
        order = OrdersModel.find_by_id(id)
        if ( order == None):
            return {"message": "Order with id [{}] not found ".format(id)}, 404
        addresses = order.json_with_address_id()["address"]
        address_list = [addresses[i] for i in range(len(addresses)) if addresses[i]["id"] == int(id_sub)]
        try:
            address = address_list[0]
            return address, 200
        except:
            return {"message": "Address with id [{}] Not found in Order with id [{}]".format(id_sub, id)}, 404

    #@auth.login_required(role='admin')
    def post(self, id, id_sub, address_id=None):
        order = OrdersModel.find_by_id(id)
        account = AccountModel.find_by_id(id_sub)
        if (account == None):
            return {'message': "Account with id [{}] Not found".format(id_sub)}, 404
        if (order == None):
            return {"message": "Order with id [{}] not found ".format(id)}, 404
        #Si no pasamos address id por parametro pedimos los parametros para crear una nueva direccion
        address = None
        if ( address_id == None ):
            if (len(account.addresses) == 3):
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
        #Si pasamos la id de la direccion la buscamos en la cuenta
        else:
            address = account.find_addres_by_id(address_id)
        if( address != None):
            order.add_address(address)
            order.save_to_db()
            return {'message': "OK"}, 200
        else:
            return {'message': "Address with id [{}] Not found".format(address_id)}, 404



   # @auth.login_required(role='admin')
    def delete(self, id, id_sub):
        order = OrdersModel.find_by_id(id)
        list = [order.json()["address"][i]["id"] == int(id_sub) for i in
                range(len(order.json()["address"]))]
        if len(list) == 0:
            return {"message": "Address with id [{}] not in Order with id [{}]".format(id_sub, id)}
        if not True in list:
            return {"message": "Address with id [{}] not in Order with id [{}]".format(id_sub, id)}
        index = list.index(True)
        if index is not None:
            deleted = order.delete_address(id_sub)
            if deleted:
                return {'message': "OK"}, 201

        return {'message': "Address with id [{}] Not found in order with id [{}]".format(id_sub, id)}, 409


class OrderUser(Resource):
    def get(self, id_user):

        orders = [order.json() for order in OrdersModel.find_by_id_user(id_user)]
        if orders:
            return {"orders": orders}, 200
        else:
            return {'message': "This user hasn't got orders".format(id)}, 409


class InProgressOrders(Resource):

    #@auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_state(0, id_user)]
        if orders:
            return {"orders": orders}, 200
        else:
            return {'message': "No orders in progress".format(id)}, 409

class SendOrders(Resource):

    #@auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_state(1, id_user)]
        if orders:
            return {"orders": orders}, 200
        else:
            return {'message': "No orders send".format(id)}, 409


class ReceivedOrders(Resource):

    #@auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id_user):
        orders = [order.json() for order in OrdersModel.find_by_state(2, id_user)]
        if orders:
            return {"orders": orders}, 200
        else:
            return {'message': "No orders received".format(id)}, 409
