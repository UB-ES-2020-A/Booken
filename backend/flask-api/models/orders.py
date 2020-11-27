from db import db
from models.book import BookModel

from models.payment_card import CardModel
articles = db.Table('relationship', db.Column('article_id', db.Integer, db.ForeignKey('articles.id')),
                    db.Column('order_id', db.Integer, db.ForeignKey('orders.id')))

address = db.Table('relationship2', db.Column('addresses_id', db.Integer, db.ForeignKey('addresses.id')),
                   db.Column('order_id', db.Integer, db.ForeignKey('orders.id')))


class OrdersModel(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.String(30), db.ForeignKey('accounts.id'), primary_key=False, nullable=False)
    date = db.Column(db.String(30), primary_key=False, unique=False, nullable=False)
    total = db.Column(db.Float, primary_key=False, nullable=False)
    shipping = db.Column(db.Float, primary_key=False, nullable=False)
    taxes = db.Column(db.Float, primary_key=False, nullable=False)
    state = db.Column(db.Integer, primary_key=False, nullable=False)  # 0:in progress,1:sending,2:Received
    send_type = db.Column(db.Integer, primary_key=False, nullable=False)  # 0:estandar,1:estandar plus,2:express
    # Address de la order
    address = db.relationship('AddressModel', secondary=address, backref=db.backref('orders', lazy='dynamic'))
    # Articles de la order
    articles = db.relationship('ArticlesModel', secondary=articles, backref=db.backref('orders', lazy='dynamic'))

    # Card de pagament
    card_id = db.Column(db.Integer, primary_key=False, nullable=False)

    def __init__(self, id_user, date, total, shipping, taxes, state, send_type,card_id):
        self.id_user = id_user
        self.date = date
        self.total = total
        self.shipping = shipping
        self.taxes = taxes
        self.state = state
        self.send_type = send_type
        self.card_id  = card_id

    def json(self):
        articles_json = [article.json() for article in self.articles]
        address_json = [address.json() for address in self.address]
        return {
            "id": self.id,
            "id_user": self.id_user,
            "date": self.date,
            "total": self.total,
            "shipping": self.shipping,
            "taxes": self.taxes,
            "state": self.state,
            "send_type": self.send_type,
            "card_id":self.card_id,
            "address": address_json,
            "articles": articles_json,
        }

    def json_with_address_id(self):
        articles_json = [article.json() for article in self.articles]
        address_json = [address.json_with_id() for address in self.address]
        card_json = [item.json() for item in self.card]
        return {
            "id": self.id,
            "id_user": self.id_user,
            "date": self.date,
            "total": self.total,
            "shipping": self.shipping,
            "taxes": self.taxes,
            "state": self.state,
            "send_type": self.send_type,
            "card_id": self.card_id,
            "address": address_json,
            "articles": articles_json,
            "card": card_json
        }

    def json_filtered_by_book_id(self):
        book = BookModel.find_by_id(self.id_book)
        return {
            "id": self.id_book,
            "id_user": self.id_user,
            "book_name": book.name,
            "num_books": self.num_books,
            "state": self.state,
            "send_type": self.send_type,
            "card_id": self.card_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def change_order_state(self, new_state):
        self.state = new_state

    @classmethod
    def find_by_state(cls, state, idd):
        try:
            return OrdersModel.query.filter_by(state=state, id_user=idd).all()
        except:
            return None

    @classmethod
    def find_by_id_user_and_orderid(cls, id_user, order_id):
        try:
            return OrdersModel.query.filter_by(id_user=id_user, id=order_id).all()
        except:
            return None

    @classmethod
    def find_by_id_user(cls, idd):
        try:
            return OrdersModel.query.filter_by(id_user=idd).all()
        except:
            return None

    @classmethod
    def find_by_id(cls, idd):
        try:
            return OrdersModel.query.filter_by(id=idd).first()
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

    def add_article(self, article):
        self.articles += [article]
        self.save_to_db()

    def delete_article(self, idd):
        index = [i for i in range(len(self.json()["articles"])) if self.json()["articles"][i]["id"] == int(idd)]
        if index:
            self.articles.pop(index[0])
            db.session.add(self)
            db.session.commit()
            return 1
        return 0

    def add_address(self, address):
        self.address += [address]
        self.save_to_db()

    def delete_address(self, idd):
        index = [i for i in range(len(self.json()["address"])) if self.json()["address"][i]["id"] == int(idd)]
        if index:
            self.address.pop(index[0])
            db.session.add(self)
            db.session.commit()
            return 1
        return 0

    def get_card(self):
        card = CardModel.find_by_id(self.card_id)
        return card.json()

    def get_num_articles(self):
        return len(self.articles)
