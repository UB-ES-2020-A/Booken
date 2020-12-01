from db import db



class FAQModel(db.Model):
    __tablename__ = 'faq'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    question = db.Column(db.String(30), unique=False, nullable=False)
    answer = db.Column(db.String(30), unique=False, nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


    def json(self):
        return {
            "id": self.id,
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
