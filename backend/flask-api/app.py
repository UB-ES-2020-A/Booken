from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from decouple import config as config_decouple
#models
from models.author import AuthorModel

app = Flask(__name__)
api = Api(app)

# SQL configuration;
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
