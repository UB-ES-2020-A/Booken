# file deepcode ignore C0413: <comment the reason here>
# file deepcode ignore W0611: stupid deepcode
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('././')
from flask import render_template
from flask_migrate import Migrate
from flask_restful import Api
from resources.account_rs import Account, Accounts, PasswordChange
from resources.author import AuthorList, Author
from resources.login_rs import Login
from resources.book import BookArtist, BookList, Book, SearchBook
from resources.contact_rs import Contact, ContactList
from resources.order import OrdersList, OrderUser, OrderArticlesList, OrderAddress, OrderArticles, OrderAddressList, \
    InProgressOrders, InProgressOrdersList, Orders, ReceivedOrdersList, ReceivedOrders, SendOrders, SendOrdersList
from resources.article import Articles, ArticlesList
from resources.address_rs import Address, AddressList
from resources.payment_card_rs import Card, CardList
from resources.review import ReviewList, ReviewListBook, ReviewListUser, Review
from resources.wishlist import Wishlist
from resources.data_retriever_rs import Retriever
from resources.faq import FAQ, FAQList
from resources.category_faq import Category_FAQ, Category_FAQ_list
from resources.mail_sender_rs import SendContactResponse
from resources.logs_rs import LoginLogs
from db import db, create_app

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
from models.wishlist import WishlistModel
from models.faq import FAQModel
from models.category_faq import CategoryModel
from models.log import LogModel


def setupApp(test=False):
    #  deepcode ignore W0621: n/a
    app = create_app(test)
    app.app_context().push()
    api = Api(app)

    migrate = Migrate(app, db)

    # EndPoints configuration
    api.add_resource(Account, '/api/account/<int:idd>', '/api/account')
    api.add_resource(Accounts, '/api/accounts/')
    api.add_resource(PasswordChange, "/api/account/<int:idd>/change_password")

    api.add_resource(Address, '/api/account/<int:account_id>/address/<int:idd>', '/api/account/<int:account_id>/address')
    api.add_resource(AddressList, '/api/account/<int:account_id>/addresses')

    api.add_resource(Card, '/api/account/<int:account_id>/card/<int:idd>', '/api/account/<int:account_id>/card')
    api.add_resource(CardList, '/api/account/<int:account_id>/cards')

    api.add_resource(Login, '/api/login')

    api.add_resource(Book, '/api/book/<int:idd>', '/api/book')
    api.add_resource(BookList, '/api/books', '/api/books/<string:genre>')
    api.add_resource(BookArtist, '/api/book/<int:idd>/author')
    api.add_resource(SearchBook, '/api/search')

    api.add_resource(Author, '/api/author/<int:idd>', '/api/author')
    api.add_resource(AuthorList, '/api/authors')

    api.add_resource(Contact, '/api/contact_info/<int:idd>', '/api/contact_info')
    api.add_resource(ContactList, '/api/contact_list/')

    api.add_resource(OrdersList, '/api/orders')
    api.add_resource(Orders, '/api/order', '/api/order/<int:idd>')

    api.add_resource(ArticlesList, '/api/articles')
    api.add_resource(Articles, '/api/article/<int:idd>', '/api/article')

    api.add_resource(OrderArticlesList, '/api/articles-order/<int:idd>')
    api.add_resource(OrderArticles, '/api/article-order/<int:idd>/<int:id_article>', '/api/article-order/<int:idd>')

    api.add_resource(OrderAddressList, '/api/addresses-order/<int:idd>')
    api.add_resource(OrderAddress, '/api/address-order/<int:idd>/<int:id_sub>',
                     '/api/address-order/<int:idd>/<int:id_sub>/<int:address_id>')

    api.add_resource(InProgressOrders, '/api/orders-state-0/<int:id_user>')
    api.add_resource(SendOrders, '/api/orders-state-1/<int:id_user>')
    api.add_resource(ReceivedOrders, '/api/orders-state-2/<int:id_user>')
    api.add_resource(OrderUser, '/api/order-user/<int:id_user>', '/api/order-user/<int:id_user>/<int:id_order>')

    api.add_resource(Review, '/api/review/<int:idd>', '/api/review')
    api.add_resource(ReviewList, '/api/reviews')
    api.add_resource(ReviewListUser, '/api/reviewsUser/<int:user_id>')
    api.add_resource(ReviewListBook, '/api/reviewsBook/<int:book_id>')

    api.add_resource(InProgressOrdersList, '/api/orders-list-state-0')
    api.add_resource(SendOrdersList, '/api/orders-list-state-1')
    api.add_resource(ReceivedOrdersList, '/api/orders-list-state-2')

    api.add_resource(Wishlist, '/api/wishlist/<int:id_account>', '/api/wishlist/<int:id_account>/<int:id_book>')

    api.add_resource(Retriever, '/api/data_retriever/<string:needed_data>')

    api.add_resource(FAQ, '/api/faq/<int:idd>', '/api/faq')
    api.add_resource(FAQList, '/api/faqs')

    api.add_resource(Category_FAQ, '/api/category/<int:idd>', '/api/category')
    api.add_resource(Category_FAQ_list, '/api/categories')

    api.add_resource(SendContactResponse, '/api/send_contact_response')

    api.add_resource(LoginLogs, '/api/logs')

    return app


app = setupApp()


@app.route('/')
def render_vue():
    return render_template("index.html"), 200


@app.errorhandler(404)
def return_index(e):
    return render_template("index.html"), 200


if __name__ == '__main__':
    app.run()
