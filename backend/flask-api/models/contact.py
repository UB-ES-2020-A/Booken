from db import db
from datetime import date


class ContactModel(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(30), nullable=False)
    full_name = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.Integer)
    contact_query = db.Column(db.String(), nullable=False)
    contact_date = db.Column(db.String(), nullable=False)

    def __init__(self, full_name, email, phone_number, contact_query):
        self.email = email
        self.full_name = full_name
        self.phone_number = phone_number
        self.contact_query = contact_query
        self.contact_date = date.today().strftime("%d/%m/%Y")

    def json(self):
        body = {
            'id': self.id,
            'email': self.email,
            'full_name': self.full_name,
            'phone_number': self.phone_number,
            'contact_query': self.contact_query,
            'contact_date': self.contact_date
        }
        return body

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
