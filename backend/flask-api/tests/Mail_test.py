# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a

import unittest
import sys

sys.path.append('../')
from models.contact import ContactModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db


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
        contact.email=""
        contact.save_to_db()

        response = self.send_email(1)
        self.assertEqual(response.status_code, 500)

    def send_email(self, contact_id):
        return self.app.post('api/send_contact_response',
                             data=dict(
                                 contact_id=contact_id,
                                 contact_response="Test response"
                             ),
                             follow_redirects=True)

