from flask import render_template
from flask_migrate import Migrate

# resourcers
from resources.account_rs import *
from resources.author import *
from resources.login_rs import *
from resources.book import *
from resources.contact_rs import *
from resources.order import *
from resources.article import *
from resources.address_rs import *
from resources.payment_card_rs import *
from resources.review import *
from db import db, create_app


app = create_app()
app.app_context().push()
api = Api(app)

# models (necessary to make the migration correctly)
from models.accounts import AccountModel
from models.author import AuthorModel
from models.book import BookModel
from models.contact import ContactModel
from models.orders import OrdersModel
from models.articles import ArticlesModel
from models.address import AddressModel
from models.payment_card import CardModel
from models.review import ReviewModel

migrate = Migrate(app, db)

# EndPoints configuration
api.add_resource(Account, '/account/<int:id>', '/account')
api.add_resource(Accounts, '/accounts/')

api.add_resource(Address, '/account/<int:account_id>/address/<int:id>', '/account/<int:account_id>/address')
api.add_resource(AddressList, '/account/<int:account_id>/addresses')

api.add_resource(Card, '/account/<int:account_id>/card/<int:id>', '/account/<int:account_id>/card')
api.add_resource(CardList, '/account/<int:account_id>/cards')

api.add_resource(Login, '/login')

api.add_resource(Book, '/book/<int:id>', '/book')
api.add_resource(BookList, '/books', '/books/<string:genre>')
api.add_resource(BookArtist, '/book/<int:id>/author')

api.add_resource(Author, '/author/<int:id>', '/author')
api.add_resource(AuthorList, '/authors')

api.add_resource(Contact, '/contact_info/<int:id>', '/contact_info')
api.add_resource(ContactList, '/contact_list/')

api.add_resource(OrdersList, '/orders')
api.add_resource(Orders, '/order', '/order/<int:id>')

api.add_resource(ArticlesList, '/articles')
api.add_resource(Articles, '/article/<int:id>', '/article')

api.add_resource(OrderArticlesList, '/articles-order/<int:id>')
api.add_resource(OrderArticles, '/article-order/<int:id>/<int:id_article>', '/article-order/<int:id>')

api.add_resource(OrderAddressList, '/addresses-order/<int:id>')
api.add_resource(OrderAddress, '/address-order/<int:id>/<int:id_sub>',
                 '/address-order/<int:id>/<int:id_sub>/<int:address_id>')

api.add_resource(InProgressOrders, '/orders-state-0')
api.add_resource(SendOrders, '/orders-state-1')
api.add_resource(ReceivedOrders, '/orders-state-2')

api.add_resource(Review, '/review/<int:id>', '/review')
api.add_resource(ReviewList, '/reviews')
api.add_resource(ReviewListUser, '/reviewsUser/<int:user_id>')
api.add_resource(ReviewListBook, '/reviewsBook/<int:book_id>')

@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
