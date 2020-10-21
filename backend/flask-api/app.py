from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from decouple import config as config_decouple
#models
from models.author import AuthorModel

from resources.author import Author,AuthorList


app = Flask(__name__)
api = Api(app)

# SQL configuration;
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api.add_resource(Author, '/author/<int:id>', '/author')
api.add_resource(AuthorList, '/authors')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
