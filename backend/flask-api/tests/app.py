from flask import render_template
from flask_migrate import Migrate
from flask_restful import Api
from resources.account_rs import Account, Accounts, PasswordChange
from resources.author import AuthorList, Author
from resources.login_rs import Login
from resources.book import BookArtist, BookList, Book, SearchBook
from resources.contact_rs import Contact, ContactList
from resources.order import OrdersList, OrderUser, OrderArticlesList, OrderAddress, OrderArticles, OrderAddressList, InProgressOrders, InProgressOrdersList, Orders, ReceivedOrdersList, ReceivedOrders, SendOrders, SendOrdersList
from resources.article import Articles, ArticlesList
from resources.address_rs import Address, AddressList
from resources.payment_card_rs import Card, CardList
from resources.review import ReviewList, ReviewListBook, ReviewListUser, Review
from resources.wishlist import Wishlist
from resources.data_retriever_rs import Retriever
from db import db, create_app

# models (necessary to make the migration correctly)

def setupApp(test=False):
    #  deepcode ignore W0621: n/a

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
    app = create_app(test)
    app.app_context().push()
    api = Api(app)

    migrate = Migrate(app, db)

    # EndPoints configuration
    api.add_resource(Account, '/account/<int:idd>', '/account')
    api.add_resource(Accounts, '/accounts/')
    api.add_resource(PasswordChange, "/account/<int:idd>/change_password")

    api.add_resource(Address, '/account/<int:account_id>/address/<int:idd>', '/account/<int:account_id>/address')
    api.add_resource(AddressList, '/account/<int:account_id>/addresses')

    api.add_resource(Card, '/account/<int:account_id>/card/<int:idd>', '/account/<int:account_id>/card')
    api.add_resource(CardList, '/account/<int:account_id>/cards')

    api.add_resource(Login, '/login')

    api.add_resource(Book, '/book/<int:idd>', '/book')
    api.add_resource(BookList, '/books', '/books/<string:genre>')
    api.add_resource(BookArtist, '/book/<int:idd>/author')
    api.add_resource(SearchBook, '/search')

    api.add_resource(Author, '/author/<int:idd>', '/author')
    api.add_resource(AuthorList, '/authors')

    api.add_resource(Contact, '/contact_info/<int:idd>', '/contact_info')
    api.add_resource(ContactList, '/contact_list/')

    api.add_resource(OrdersList, '/orders')
    api.add_resource(Orders, '/order', '/order/<int:idd>')

    api.add_resource(ArticlesList, '/articles')
    api.add_resource(Articles, '/article/<int:idd>', '/article')

    api.add_resource(OrderArticlesList, '/articles-order/<int:idd>')
    api.add_resource(OrderArticles, '/article-order/<int:idd>/<int:id_article>', '/article-order/<int:idd>')

    api.add_resource(OrderAddressList, '/addresses-order/<int:idd>')
    api.add_resource(OrderAddress, '/address-order/<int:idd>/<int:id_sub>',
                     '/address-order/<int:idd>/<int:id_sub>/<int:address_id>')

    api.add_resource(InProgressOrders, '/orders-state-0/<int:id_user>')
    api.add_resource(SendOrders, '/orders-state-1/<int:id_user>')
    api.add_resource(ReceivedOrders, '/orders-state-2/<int:id_user>')
    api.add_resource(OrderUser, '/order-user/<int:id_user>', '/order-user/<int:id_user>/<int:id_order>')

    api.add_resource(Review, '/review/<int:idd>', '/review')
    api.add_resource(ReviewList, '/reviews')
    api.add_resource(ReviewListUser, '/reviewsUser/<int:user_id>')
    api.add_resource(ReviewListBook, '/reviewsBook/<int:book_id>')

    api.add_resource(InProgressOrdersList, '/orders-list-state-0')
    api.add_resource(SendOrdersList, '/orders-list-state-1')
    api.add_resource(ReceivedOrdersList, '/orders-list-state-2')

    api.add_resource(Wishlist, '/wishlist/<int:id_account>', '/wishlist/<int:id_account>/<int:id_book>')

    api.add_resource(Retriever,'/data_retriever/<string:needed_data>')
    return app

app = setupApp()
@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
