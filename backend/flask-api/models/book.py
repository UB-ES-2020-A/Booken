from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    author = db.relationship('AuthorModel', backref=db.backref('books', lazy='dynamic'))
    year = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(30), nullable=False)
    language = db.Column(db.String(30), nullable=False)
    synopsis = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, id, name, year, editorial, language, synopsis, price):
        self.id = id
        self.name = name
        self.year = year
        self.editorial = editorial
        self.language = language
        self.synopsis = synopsis
        self.price = price

    @classmethod
    def find_by_id(cls, idd):
        return db.session.query(BookModel).filter_by(id=idd).first()

    @classmethod
    def find_by_name(cls, name):
        return db.session.query(BookModel).filter_by(name=" ".join(w.capitalize() for w in name.split(" "))).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.query(BookModel).filter_by(id=self.id).delete()
        db.session.commit()

    def json(self):
        return {"event": {
            "id": self.id,
            "name": self.name,
            "author": self.author.name,
            "year": self.year,
            "editorial": self.editorial,
            "language": self.language,
            "price": self.price,
            "synopsis": self.synopsis
        }}