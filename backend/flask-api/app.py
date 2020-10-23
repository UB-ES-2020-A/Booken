from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

#models (necessary to make the migration correctly)
from models.accounts import AccountModel

#resourcers
from resources.account_rs import *
from resources.author import *
from resources.login_rs import *
from resources.book import *

from db import db

app = Flask(__name__)

api = Api(app)

#Cross-origin request config
CORS(app, resources={r'/*': {'origins': '*'}})

#Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


#EndPoints configuration

api.add_resource(Account, '/account/<string:username>', '/account')
api.add_resource(Accounts, '/accounts/')

api.add_resource(Login, '/login/')

api.add_resource(Book, '/book/<int:id>', '/book')
api.add_resource(BookList, '/books')
api.add_resource(BookArtist, '/book/<int:id>/author')

api.add_resource(Author, '/author/<int:id>', '/author')
api.add_resource(AuthorList, '/authors')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
