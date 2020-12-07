from db import db

interface = db.Table('interface', db.Column('interface_id', db.Integer, db.ForeignKey('interfaces.id')),
                     db.Column('book_id', db.Integer, db.ForeignKey('books.id')))


class InterfaceModel(db.Model):
    __tablename__ = 'interfaces'

    id = db.Column(db.Integer, primary_key=True)
    front_type = db.Column(db.Integer, nullable=False)
    t1BackgndURL = db.Column(db.String(100))
    t1BackgndCOL = db.Column(db.String(30), nullable=False)
    t1LinkTo = db.Column(db.String(100), nullable=False)
    t1Tit = db.Column(db.String(100), nullable=False)
    t1Sub = db.Column(db.String(30), nullable=False)
    t1Small = db.Column(db.String(30), nullable=False)
    line = db.Column(db.Integer, nullable=False)  # 0->True, 1->False
    t2RowTitle = db.Column(db.String(50), nullable=False)
    t2RowNumber = db.Column(db.String(30), nullable=False)
    books = db.relationship('BookModel', secondary=interface, backref=db.backref('book_interface', lazy='dynamic'))

    def __init__(self, front_type, t1BackgndURL, t1BackgndCOL, t1LinkTo, t1Tit, t1Sub, t1Small, line, t2RowTitle,
                 t2RowNumber):
        self.front_type = front_type
        self.t1BackgndURL = t1BackgndURL
        self.t1BackgndCOL = t1BackgndCOL
        self.t1LinkTo = t1LinkTo
        self.t1Tit = t1Tit
        self.t1Sub = t1Sub
        self.t1Small = t1Small
        self.line = line
        self.t2RowTitle = t2RowTitle
        self.t2RowNumber = t2RowNumber

    @classmethod
    def find_by_id(cls, idd):
        return db.session.query(InterfaceModel).filter_by(id=idd).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.query(InterfaceModel).filter_by(id=self.id).delete()
        db.session.commit()

    def json(self):
        return {"book": {
            "id": self.id,
            "front_type": self.front_type,
            "t1BackgndURL": self.t1BackgndURL,
            "t1BackgndCOL": self.t1BackgndCOL,
            "t1LinkTo": self.t1LinkTo,
            "t1Tit": self.t1Tit,
            "t1Sub": self.t1Sub,
            "t1Small": self.t1Small,
            "line": self.line,
            "t2RowTitle": self.t2RowTitle,
            "t2RowNumber": self.t2RowNumber,
            "books": [a.json()['book'] for a in self.books]
        }}
