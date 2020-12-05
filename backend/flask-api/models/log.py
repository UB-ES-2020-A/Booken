from db import db
from datetime import datetime


class LogModel(db.Model):
    __tablename__ = 'loginlog'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer)
    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    minutes = db.Column(db.Integer)

    def __init__(self, uid):
        self.user_id = uid
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = datetime.now().year
        self.hour = datetime.now().hour
        self.minutes = datetime.now().minute

    def json(self):
        body = {
            'id': self.id,
            'user_id': self.user_id,
            'day': self.day,
            'year': self.year,
            'month': self.month,
            'hour': self.hour,
            'minutes': self.minutes,
        }
        return body

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, idd):
        return cls.query.filter_by(id=idd).first()

    @classmethod
    def find_by_year(cls, y):
        return cls.query.filter_by(year=y).all()

    @classmethod
    def find_by_month_year(cls, y, m):
        return cls.query.filter_by(year=y, month=m).all()
