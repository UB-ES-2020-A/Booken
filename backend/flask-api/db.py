from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

secret_key = "McQfTjWnZr4u7x!A%D*G-KaPdRgUkXp2s5v8y/B?E(H+MbQeThVmYq3t6w9z$C&F"

def create_app():
    app = app = Flask(__name__,
                static_folder="../front-end/dist/static",
                template_folder="../front-end/dist")
    app.config.from_object(__name__)
    # Cross-origin request config
    CORS(app, resources={r'/*': {'origins': '*'}})
    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key
    db = SQLAlchemy(app)
    return app
