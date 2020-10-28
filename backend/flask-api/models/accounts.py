from db import db, secret_key
from flask import g

from flask_httpauth import HTTPBasicAuth

from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

auth = HTTPBasicAuth()

class AccountModel(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    email = db.Column(db.String(30), unique = True, nullable = False)

    name = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)

    password = db.Column(db.String(), nullable = False)

    type = db.Column(db.Integer, nullable = False) # 0 = client / 1 = develop-manager / 2 = stock-manager
    available_money = db.Column(db.Integer)

    #orders = db.relationship('OrdersModel', backref='orders, lazy = True)
    #wish_list = db.relationship('BookModel', backref='books', lazy = True)

    def __init__(self, email, name, lastname, password):
        self.email = email
        self.name = name
        self.lastname = lastname
        self.hash_password(password)
        self.type = 0
        self.available_money = 0

    def json(self):
        body = {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'available_money': self.available_money,
            'type': self.type
        }

        return body

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(self, id):
        return self.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(self, email):
        return self.query.filter_by(email=email).first()

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'email':self.email})

    @classmethod
    def verify_auth_token(cls, token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = cls.query.filter_by(email=data['email']).first()

        return user


@auth.verify_password
def verify_password(id, token):
    id = int(id)
    user = AccountModel.verify_auth_token(token)
    if(user and user.id == id):
        g.user = user
        return user

@auth.get_user_roles
def get_user_roles(user):
    roles = {
        0: 'client',
        1: 'dev_manager',
        2: 'stock_manager'
    }
    return roles[user.type]
