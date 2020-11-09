from db import db

from models.accounts import AccountModel

class AddressModel(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key = True, unique = True)
    account_id = db.Column(db.String(30), db.ForeignKey('accounts.id'), nullable=False)

    label_name = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    surnames = db.Column(db.String(), nullable=False)

    street = db.Column(db.String(), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    #codigo postal
    cp = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    province = db.Column(db.String(), nullable=False)

    telf = db.Column(db.Integer)

    def __init__(self, label_name,name,surnames,street,number,cp,city,province,telf):
        self.label_name = label_name
        self.name = name
        self.surnames = surnames
        self.street = street
        self.number = number
        self.cp = cp
        self.city = city
        self.province = province
        self.telf = telf

    def json(self):
        body = {
            'label_name': self.label_name,
            'name': self.name,
            'surnames': self.surnames,
            'street': self.street,
            'number': self.number,
            'cp': self.cp,
            'city': self.city,
            'province': self.province,
            'telf': self.telf
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

    @classmethod
    def find_by_account_id(self, account_id):
        return self.query.filter_by(account_id=account_id).all()