from db import db

METHOD = ('VISA', 'MASTERCARD', 'AMERICAN EXPRESS', 'JCB', 'DISCOVER')

class CardModel(db.Model):
    __table_name__ = 'payment_card'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    account_id = db.Column(db.String(30), db.ForeignKey('accounts.id'), nullable=False)

    card_owner = db.Column(db.String(), nullable=False)
    number = db.Column(db.String(), nullable=False)
    date = db.Column(db.String(), nullable=False)
    payment_method = db.Column(db.Enum(*METHOD, name='payment_method'), nullable=False)

    def __init__(self, card_owner, number, date, method):
        self.card_owner = card_owner
        self.number = number
        self.date = date
        self.payment_method = method

    def json(self):
        body = {
            'id': self.id,
            'card_owner': self.card_owner,
            'number': self.number[-4:],
            'date': self.date,
            'method': self.payment_method
        }

        return body


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_id(self, id):
        return self.query.filter_by(id=id).first()