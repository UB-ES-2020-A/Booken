from db import db
from models.book import BookModel
from models.accounts import AccountModel
from models.articles import ArticlesModel
from models.orders import OrdersModel,states
from flask_restful import Resource, reqparse
from models.accounts import auth, g


class Orders(Resource):

    #@auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def get(self, id):
        order = OrdersModel.find_by_id(id)
        if order:
            return {"orders": order.json()}, 200
        else:
            return {'message': "The user with id [{}] hasn't got any order".format(id)}, 409

   # @auth.login_required(role=['dev_manager', 'stock_manager','client'])
    def post(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        parser.add_argument('date', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('total', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('shipping', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('taxes', type=float, required=True, help="This field cannot be left blanck")
        parser.add_argument('state', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('adress', type=str, required=True, help="This field cannot be left blanck")
        data = parser.parse_args()
        acc = AccountModel.find_by_id(id)

        if data.state not in states:
            return {'message': "Order with state [{}] not supported".format(data.state)}, 400
        #if (acc == None):
         #   return {'message': "There isn't a user with this id"}, 409

        new_id = OrdersModel.num_orders()
        new_order = OrdersModel(new_id,id, data.date, data.total,data.shipping,data.taxes,data.state,data.adress)
        #acc.orders.append(new_order)
        db.session.add(new_order)
        db.session.commit()
        return new_order.json(), 200


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
        parser.add_argument('state', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('adress', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()

        if data.state not in states:
            return {'message': "Order with state [{}] not supported".format(data.state)}, 400

        order = OrdersModel.find_by_id(id)

        if ( order ) :
            id_user = order.id_user
            order.delete_from_db()
            new_order = OrdersModel(id,id_user,data.date, data.total, data.shipping, data.taxes, data.state, data.adress)
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
        #Create article and add to order
        id_article = ArticlesModel.num_articles()+1
        article = ArticlesModel(id_article,data.price)
        order.add_article(article)
        article.save_to_db()
        return id_article, 200


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

