from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db
from flask import g, current_app

class AuthorModel(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(30), primary_key=True, unique=False, nullable=False)
    birth_date = db.Column(db.String(30), primary_key=True, unique=False, nullable=False)
    city = db.Column(db.String(30), primary_key=True, unique=False, nullable=False)
    country = db.Column(db.String(30), primary_key=True, unique=False, nullable=False)

    def __init__(self, id, name, birth_date, city, country):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.city = city
        self.country = country

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_date": self.birth_date,
            "country": self.country,
            "city": self.city

        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        try:
            return AuthorModel.query.filter_by(id=id).first()
        except:
            return None

    @classmethod
    def num_authors(cls):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db = SQLAlchemy(app)
        db.init_app(app)

        return len(AuthorModel.query.all())

    @classmethod
    def get_author(cls):
        list_authors = [author.json() for author in AuthorModel.query.all()]
        dicc = {"authors": list_authors}
        return dicc