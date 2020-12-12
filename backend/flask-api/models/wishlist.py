from db import db

b = db.Table('b', db.Column('wishlist_id', db.Integer, db.ForeignKey('wishlists.id')),
             db.Column('book_id', db.Integer, db.ForeignKey('books.id')))


class WishlistModel(db.Model):
    __tablename__ = 'wishlists'

    id = db.Column(db.Integer, primary_key=True)
    id_account = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    # books = db.relationship('BookModel', backref='books_wl', lazy=True)
    books = db.relationship('BookModel', secondary=b, backref=db.backref('book_wl', lazy='dynamic'))

    def __init__(self, id_account):
        self.id_account = id_account

    @classmethod
    def find_by_id(cls, idd):
        return db.session.query(WishlistModel).filter_by(id=idd).first()

    @classmethod
    def find_by_account(cls, id_account):
        return db.session.query(WishlistModel).filter_by(id_account=id_account).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.query(WishlistModel).filter_by(id=self.id).delete()
        db.session.commit()

    def json(self):
        return {"Wishlist": {
            "id": self.id,
            "id_account": self.id_account,
            "books": [a.json()['book'] for a in self.books]
        }}
