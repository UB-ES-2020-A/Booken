from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

secret_key = "McQfTjWnZr4u7x!A%D*G-KaPdRgUkXp2s5v8y/B?E(H+MbQeThVmYq3t6w9z$C&F"

def create_app(test=False):

    app = Flask(__name__,
                      static_folder="static",
                      template_folder="dist")
    if test:
        app.config['TESTING'] = True
        #  deepcode ignore DisablesCSRFProtection: n/a
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(__name__)
    # Cross-origin request config
    CORS(app, resources={r'/*': {'origins': '*'}})
    # Database config

    app.config['SECRET_KEY'] = secret_key
    db = SQLAlchemy(app)
    return app