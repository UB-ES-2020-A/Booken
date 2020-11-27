from flask import render_template
from flask_migrate import Migrate

# resourcers
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
from models.wishlist import WishlistModel

migrate = Migrate(app, db)

# EndPoints configuration
api.add_resource(Account, '/account/<int:id>', '/account')
api.add_resource(Accounts, '/accounts/')
api.add_resource(PasswordChange, "/account/<int:id>/change_password")

api.add_resource(Address, '/account/<int:account_id>/address/<int:id>', '/account/<int:account_id>/address')
api.add_resource(AddressList, '/account/<int:account_id>/addresses')

api.add_resource(Card, '/account/<int:account_id>/card/<int:id>', '/account/<int:account_id>/card')
api.add_resource(CardList, '/account/<int:account_id>/cards')

api.add_resource(Login, '/login')

api.add_resource(Book, '/book/<int:id>', '/book')
api.add_resource(BookList, '/books', '/books/<string:genre>')
api.add_resource(BookArtist, '/book/<int:id>/author')
api.add_resource(SearchBook, '/search')

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

api.add_resource(InProgressOrders, '/orders-state-0/<int:id_user>')
api.add_resource(SendOrders, '/orders-state-1/<int:id_user>')
api.add_resource(ReceivedOrders, '/orders-state-2/<int:id_user>')
api.add_resource(OrderUser, '/order-user/<int:id_user>', '/order-user/<int:id_user>/<int:id_order>')

api.add_resource(Review, '/review/<int:id>', '/review')
api.add_resource(ReviewList, '/reviews')
api.add_resource(ReviewListUser, '/reviewsUser/<int:user_id>')
api.add_resource(ReviewListBook, '/reviewsBook/<int:book_id>')

api.add_resource(InProgressOrdersList, '/orders-list-state-0')
api.add_resource(SendOrdersList, '/orders-list-state-1')
api.add_resource(ReceivedOrdersList, '/orders-list-state-2')

api.add_resource(Wishlist, '/wishlist/<int:id_account>', '/wishlist/<int:id_account>/<int:id_book>')


@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
