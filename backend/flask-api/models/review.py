from db import db
from models.accounts import AccountModel
from models.book import BookModel


class ReviewModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    valuation = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(250))

    def __init__(self, title, user_id, book_id, date, valuation, comment):
        self.title = title
        self.user_id = user_id
        self.book_id = book_id
        self.date = date
        self.valuation = valuation
        self.comment = comment

    @classmethod
    def find_by_id(cls, idd):
        return db.session.query(ReviewModel).filter_by(id=idd).first()

    @classmethod
    def find_by_user(cls, user_id):
        return db.session.query(ReviewModel).filter_by(user_id=user_id).all()

    @classmethod
    def find_by_book(cls, book_id):
        return db.session.query(ReviewModel).filter_by(book_id=book_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        account = AccountModel.find_by_id(self.user_id)
        return {"review": {
            "name": "" + account.name + " " + account.lastname[0] + ".",
            "id": self.id,
            "title": self.title,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "date": self.date,
            "valuation": self.valuation,
            "comment": self.comment
        }}