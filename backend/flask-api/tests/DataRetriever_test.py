# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a

import unittest
import sys

sys.path.append('../')

from data import books
from models.author import AuthorModel
from models.book import BookModel

#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

import json

class MailTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                         data=dict(name='test', lastname='test', email='test', password='test'),
                         follow_redirects=True)

        response = self.app.post('api/login',
                         data=dict(email='test', password='test'),
                         follow_redirects=True)

        self.token = json.loads(response.data)['token']

        self.app.post('api/account/1/address',
                         data=dict(
                             label_name="Mi casa",
                             name="test",
                             surnames="tests",
                             street="La calle de mi casa",
                             number=32,
                             cp="08431",
                             city="Mi city",
                             province="Mi provincia",
                             telf=123456
                         ),
                         follow_redirects=True)

        self.app.post('api/account/1/card',
                         data=dict(
                             card_owner="test",
                             number="4567",
                             date="12/2025",
                             payment_method="Visa"
                         ),
                         follow_redirects=True)

        self.add_book()

        self.app.post('api/order/1',
                          data=dict(
                                date="29/11/2020 10:50",
                                total=1.,
                                shipping=1.,
                                taxes=1.,
                                state=0,
                                send_type=0,
                                card_id=1,
                                address_id=1
                          ),
                          follow_redirects=True)

        self.app.post('/api/article-order/1',
                        data=dict(
                            price=1,
                            quant=1,
                            id_book=1
                        ),
                        follow_redirects=True)

    def tearDown(self):
        # Executed after each test
        pass

    def test_get_data(self):
        response = self.retrieve("total_sales")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("sales_month")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("total_month")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("sales_year")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("sales_genre")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("total_gain")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("gain_month")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("gain_year")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("gain_genre")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("total_users")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("log_month")
        self.assertEqual(response.status_code, 200)

        response = self.retrieve("all")
        self.assertEqual(response.status_code, 200)


    def retrieve(self, data):
        return self.app.get('/api/data_retriever/' + data, follow_redirects=True)

    def add_book(self):
        b = books[0]
        authors = []
        author = b[2][0]
        author = AuthorModel(author[0], author[1], author[2], author[3])
        authors.append(author)
        book = BookModel(b[0], b[1], authors, b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10], b[11], b[12], b[13],
                         b[14], b[15])

        db.session.add(author)
        db.session.add(book)

        db.session.commit()
