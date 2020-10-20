from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#models
from models.accounts import AccountModel

from db import db

app = Flask(__name__)

#Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
