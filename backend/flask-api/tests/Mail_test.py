# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a

import unittest
import sys

sys.path.append('../')

from data import books
from models.accounts import AccountModel
from models.author import AuthorModel
from models.book import BookModel
from models.contact import ContactModel

#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

import json, base64


class MailTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/contact_info',
                      data=dict(
                          full_name="Unit Test",
                          email="booken.eshop@gmail.com",
                          phone_number=0,
                          contact_query="This is a test"
                      ),
                      follow_redirects=True)

        self.app.post('api/account',
                      data=dict(name='test', lastname='test', email='booken.eshop@gmail.com', password='test'),
                      follow_redirects=True)

        acc = AccountModel.query.first()
        acc.type = 1
        acc.save_to_db()

        response = self.app.post('api/login',
                                 data=dict(email='booken.eshop@gmail.com', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

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
                      headers=self.auth,
                      follow_redirects=True)

        self.app.post('api/account/1/card',
                      data=dict(
                          card_owner="test",
                          number="4567",
                          date="12/2025",
                          payment_method="Visa"
                      ),
                      headers=self.auth,
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
                      headers=self.auth,
                      follow_redirects=True)

        self.app.post('/api/article-order/1',
                      data=dict(
                          price=1,
                          quant=1,
                          id_book=1
                      ),
                      headers=self.auth,
                      follow_redirects=True)


    def tearDown(self):
        # Executed after each test
        pass

    def test_send_email_correctly(self):
        response = self.send_email(1)
        self.assertEqual(response.status_code, 200)

    def test_send_email_with_not_contact(self):
        response = self.send_email(2)
        self.assertEqual(response.status_code, 404)

    def test_send_email_with_not_existent_email(self):
        contact = ContactModel.query.first()
        contact.email = ""
        contact.save_to_db()

        response = self.send_email(1)
        self.assertEqual(response.status_code, 500)
    
    def test_send_ticket_correctly(self):
        response = self.send_ticket(1,1)
        self.assertEqual(response.status_code, 200)

    def test_send_ticket_with_not_contact(self):
        response = self.send_ticket(2, 1)
        self.assertEqual(response.status_code, 404)

    def test_send_ticket_with_not_order(self):
        response = self.send_ticket(1, 2)
        self.assertEqual(response.status_code, 404)

    def test_send_ticket_with_not_email(self):
        account = AccountModel.query.first()
        account.email="test_fail"
        account.save_to_db()

        response = self.app.post('api/login',
                                 data=dict(email='test_fail', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

        response = self.send_ticket(1,1)
        self.assertEqual(response.status_code, 500)

    def send_email(self, contact_id):
        return self.app.post('api/send_contact_response',
                             data=dict(
                                 contact_id=contact_id,
                                 contact_response="Test response"
                             ),
                             headers=self.auth,
                             follow_redirects=True)

    def send_ticket(self, account_id, order_id):
        return self.app.post('api/send_ticket',
                             data=dict(
                                 account_id=account_id,
                                 order_id=order_id
                             ),
                             headers=self.auth,
                             follow_redirects=True)

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
