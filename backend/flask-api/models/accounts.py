from flask_httpauth import HTTPBasicAuth
from db import db

auth = HTTPBasicAuth()

class AccountModel(db.Model):
    __tablename__ = 'accounts'

    username = db.Column(db.String(30), primary_key = True, unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

    type = db.Column(db.Integer, nullable = False) # 0 = client / 1 = admin /
    available_money = db.Column(db.Integer)

    #orders = db.relationship('OrdersModel', backref='orders, lazy = True)

    def __init__(self, username, available_money = 250, type = 0):
        self.username = username
        self.available_money = available_money
        self.type = type
        self.password = "test"

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