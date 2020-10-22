from db import db, secret_key
from flask import g

from flask_httpauth import HTTPBasicAuth

from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

auth = HTTPBasicAuth()

class AccountModel(db.Model):
    __tablename__ = 'accounts'

    username = db.Column(db.String(30), primary_key = True, unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

    type = db.Column(db.Integer, nullable = False) # 0 = client / 1 = develop-manager / 2 = stock-manager
    available_money = db.Column(db.Integer)

    #orders = db.relationship('OrdersModel', backref='orders, lazy = True)

    def __init__(self, username, available_money = 250, type = 0):
        self.username = username
        self.available_money = available_money
        self.type = type
        #self.password = "test"

    def json(self):
        body = {
            'username': self.username,
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
    def find_by_username(self, username):
        return self.query.filter_by(username=username).first()

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'username':self.username})

    @classmethod
    def verify_auth_token(cls, token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = cls.query.filter_by(username=data['username']).first()

        return user


@auth.verify_password
def verify_password(username, token):
    user = AccountModel.verify_auth_token(token)
    if(user and user.username == username):
        g.user = user
        return user

@auth.get_user_roles
def get_user_roles(user):
    roles = {
        0: 'user',
        1: 'dev_manager',
        2: 'stock_manager'
    }
    return roles[user.type]
