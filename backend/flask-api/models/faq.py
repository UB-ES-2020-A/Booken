from db import db


category = db.Table('cat_relation', db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
                    db.Column('faq_id', db.Integer, db.ForeignKey('faq.id')))
class FAQModel(db.Model):
    __tablename__ = 'faq'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    category = db.relationship('CategoryModel', secondary=category, backref=db.backref('faq', lazy='dynamic'))
    question = db.Column(db.String(30), unique=False, nullable=False)
    answer = db.Column(db.String(30), unique=False, nullable=False)

    def __init__(self, faq_category,question, answer):
        self.question = question
        self.answer = answer
        self.category.append(faq_category)

    def json(self):
        categor = [cat.json() for cat in self.category]
        return {
            "id": self.id,
            "category": categor,
            "question": self.question,
            "answer": self.answer,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, idd):
        return FAQModel.query.filter_by(id=idd).first()

    @classmethod
    def num_faq(cls):
        return len(FAQModel.query.all())

    @classmethod
    def get_faqs(cls):
        list_faq = [faq.json() for faq in FAQModel.query.all()]
        dicc = {"FAQ": list_faq}
        return dicc
