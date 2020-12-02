from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from db import db
from models.book import BookModel


class ArticlesModel(db.Model):
    __tablename__ = 'articles'  # This is table name

    id = db.Column(db.Integer, unique=False, primary_key=True)
    book_id = db.Column(db.Integer, unique=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    categoria = db.Column(db.String, unique=False, nullable=False)
    quant = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, price, categoria, quant, book_id):
        self.price = price
        self.categoria = categoria
        self.quant = quant
        self.book_id = book_id

    def json(self):
        book = BookModel.find_by_id(self.book_id)
        return {
            "id": self.id,
            "price": self.price,
            "categoria": self.categoria,
            "quant": self.quant,
            "book_title": book.name
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, idd):
        try:
            return ArticlesModel.query.filter_by(id=idd).first()
        except:
            return None

    @classmethod
    def num_articles(cls):
        return len(ArticlesModel.query.all())

    @classmethod
    def get_articles(cls):

        list_articles = [article.json() for article in ArticlesModel.query.all()]
        dicc = {"articles": list_articles}
        return dicc

    @classmethod
    def get_articles_list(cls):
        list_articles = [article.json() for article in ArticlesModel.query.all()]
        return list_articles
