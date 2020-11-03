from db import db
from models.author import AuthorModel

genres = ('HUMANIDADES', 'TECNICO Y FORMACION', 'METODOS DE IDIOMAS', 'LITERATURA', 'INFANTIL', 'COMICS Y MANGA',
          'JUVENIL', 'OTRAS CATEGORIAS')
tags = db.Table('tags', db.Column('books_id', db.Integer, db.ForeignKey('books.id')),
                db.Column('authors_id', db.Integer, db.ForeignKey('authors.id')))


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    author = db.relationship('AuthorModel', secondary=tags, backref=db.backref('books', lazy='dynamic'))
    genre = db.Column(db.Enum(*genres, name='genres_types'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(30), nullable=False)
    language = db.Column(db.String(30), nullable=False)
    synopsis = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    num_pages = db.Column(db.Integer, nullable=False)
    cover_type = db.Column(db.Integer, nullable=False)  # 0-> tapa blanda , 1-> tapa dura
    price = db.Column(db.Integer, nullable=False)
    num_sales = db.Column(db.Integer, nullable=False)
    total_available = db.Column(db.Integer, nullable=False)
    cover_image_url = db.Column(db.String(100))
    back_cover_image_url = db.Column(db.String(100))

    def __init__(self, isbn, name, author, genre, year, editorial, language, price, synopsis, description, num_pages,
                 cover_type, num_sales, total_available, cover_image_url, back_cover_image_url, id=None):
        if id:
            self.id = id
        self.isbn = isbn
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.editorial = editorial
        self.language = language
        self.synopsis = synopsis
        self.description = description
        self.num_pages = num_pages
        self.cover_type = cover_type
        self.price = price
        self.num_sales = num_sales
        self.total_available = total_available
        self.cover_image_url = cover_image_url
        self.back_cover_image_url = back_cover_image_url

    @classmethod
    def find_by_id(cls, idd):
        return db.session.query(BookModel).filter_by(id=idd).first()

    @classmethod
    def find_by_isbn(cls, isbn):
        return db.session.query(BookModel).filter_by(isbn=" ".join(w.capitalize() for w in isbn.split(" "))).first()

    @classmethod
    def find_by_name(cls, name):
        return db.session.query(BookModel).filter_by(name=" ".join(w.capitalize() for w in name.split(" "))).first()

    @classmethod
    def find_by_genre(cls, genre):
        return db.session.query(BookModel).filter_by(genre=genre).all()

    @classmethod
    def find_by_author(cls, author):
        return db.session.query(BookModel).filter_by(
            name=" ".join(w.capitalize() for w in [a.name for a in author].split(" ")))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.query(BookModel).filter_by(id=self.id).delete()
        db.session.commit()

    def json(self):
        return {"book": {
            "id": self.id,
            "ISBN": self.isbn,
            "name": self.name,
            "author": [a.name for a in self.author],
            "genre": self.genre,
            "year": self.year,
            "editorial": self.editorial,
            "language": self.language,
            "price": self.price,
            "num_pages": self.num_pages,
            "cover_type": self.cover_type,
            "synopsis": self.synopsis,
            "description": self.description,
            "num_sales": self.num_sales,
            "total_available": self.total_available,
            "cover_image_url": self.cover_image_url,
            "back_cover_image_url": self.back_cover_image_url
        }}
