from flask import render_template
from flask_migrate import Migrate

# resourcers
from resources.account_rs import *
from resources.author import *
from resources.login_rs import *
from resources.book import *
from resources.contact_rs import *
from resources.order import *
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

migrate = Migrate(app, db)

# EndPoints configuration
api.add_resource(Account, '/account/<int:id>', '/account')
api.add_resource(Accounts, '/accounts/')

api.add_resource(Login, '/login')

api.add_resource(Book, '/book/<int:id>', '/book')
api.add_resource(BookList, '/books', '/books/<string:genre>')
api.add_resource(BookArtist, '/book/<int:id>/author')

api.add_resource(Author, '/author/<int:id>', '/author')
api.add_resource(AuthorList, '/authors')

api.add_resource(Contact, '/contact_info/<int:id>', '/contact_info')
api.add_resource(ContactList, '/contact_list/')

api.add_resource(OrdersList, '/orders')
api.add_resource(Orders, '/order/<string:email>', '/order', '/order/<int:id>')

@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
