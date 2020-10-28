from db import db
from models.author import AuthorModel

genres = ('HUMANIDADES', 'TECNICO Y FORMACION', 'METODOS DE IDIOMAS', 'LITERATURA', 'INFANTIL', 'COMICS Y MANGA',
          'JUVENIL', 'OTRAS CATEGORIAS')
tags = db.Table('tags', db.Column('books_id', db.Integer, db.ForeignKey('books.id')),
                db.Column('authors_id', db.Integer, db.ForeignKey('authors.id')))


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)  # ISBN
    name = db.Column(db.String(30), nullable=False)
    author = db.relationship('AuthorModel', secondary=tags, backref=db.backref('books', lazy='dynamic'))
    genre = db.Column(db.Enum(*genres, name='genres_types'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(30), nullable=False)
    language = db.Column(db.String(30), nullable=False)
    synopsis = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    num_sales = db.Column(db.Integer, nullable=False)
    total_available = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, author, genre, year, editorial, language, price, synopsis, num_sales, total_available):
        self.id = id
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.editorial = editorial
        self.language = language
        self.synopsis = synopsis
        self.price = price
        self.num_sales = num_sales
        self.total_available = total_available

    @classmethod
    def find_by_id(cls, idd):
        return db.session.query(BookModel).filter_by(id=idd).first()

    @classmethod
    def find_by_name(cls, name):
        return db.session.query(BookModel).filter_by(name=" ".join(w.capitalize() for w in name.split(" "))).first()

    @classmethod
    def find_by_author(cls, author):
        return db.session.query(BookModel).filter_by(name=" ".join(w.capitalize() for w in [a.name for a in author].split(" ")))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.query(BookModel).filter_by(id=self.id).delete()
        db.session.commit()

    def json(self):
        return {"book": {
            "ISBN": self.id,
            "name": self.name,
            "author": [a.name for a in self.author],
            "genre": self.genre,
            "year": self.year,
            "editorial": self.editorial,
            "language": self.language,
            "price": self.price,
            "synopsis": self.synopsis,
            "num_sales": self.num_sales,
            "total_available": self.total_available
        }}