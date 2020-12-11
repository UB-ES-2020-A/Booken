from flask import Flask
from decouple import config as config_decouple
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

secret_key = "McQfTjWnZr4u7x!A%D*G-KaPdRgUkXp2s5v8y/B?E(H+MbQeThVmYq3t6w9z$C&F"

email_templates = {
        "testing":False,
        "contact_response_template": "utils/email_templates/contact_response_email.html",
        "ticket_response_template": "utils/email_templates/ticket_response_email.html",
        "ticket_pdf_template": "utils/email_templates/ticket_pdf.html"
    }



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

        app.config['MAIL_SUPPRESS_SEND'] = False

        for key, value in email_templates.items():
            if key == "testing":
                if value:
                    break
                else:
                    email_templates[key] = True
            else:
                email_templates[key] = "backend/flask-api/" + value

    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Email configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = "booken.eshop@gmail.com"
    app.config['MAIL_PASSWORD'] = "asdxd123@"
    app.config['MAIL_DEFAULT_SENDER'] = ["","booken.eshop@gmail.com"] # 0: Nombre de encabezado / 1: Correo electronico

    app.config.from_object(__name__)

    if config_decouple('PRODUCTION', cast=bool, default=False):
        environment = config['production']
        app.config.from_object(environment)
    # Cross-origin request config
    CORS(app, resources={r'/*': {'origins': '*'}})
    # Database config

    app.config['SECRET_KEY'] = secret_key
    db = SQLAlchemy(app)
    return app