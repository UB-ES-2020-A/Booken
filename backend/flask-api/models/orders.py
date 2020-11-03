from db import db
from models.book import BookModel
class OrdersModel(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), db.ForeignKey('accounts.email'), nullable=False)
    id_book = db.Column(db.Integer, nullable=False)
    num_books = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(30), nullable=False)

    def __init__(self, id ,id_book, num_books,state):
        self.id = id
        self.id_book = id_book
        self.num_books = num_books
        self.state = state

    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "id_book": self.id_book,
            "num_books": self.num_books
            "state": self.state
        }

    def json_filtered_by_book_id(self):
        book = BookModel.find_by_id(self.id_book)
        return {
            "id": self.id_book,
            "email": self.email,
            "book_naem": book.name,
            "num_books": self.num_books
            "state": self.state
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def change_order_state(self, new_state):

    @classmethod
    def find_by_email(cls, email):
        try:
            return OrdersModel.query.filter_by(email=email).all()
        except:
            return None

    @classmethod
    def find_by_id(cls, id):
        try:
            return OrdersModel.query.filter_by(id=id).first()
        except:
            return None

    @classmethod
    def num_orders(cls):
        return len(OrdersModel.query.all())

    @classmethod
    def get_orders(cls):
        list_orders = [order.json() for order in OrdersModel.query.all()]
        dicc = {"orders": list_orders}
        return dicc