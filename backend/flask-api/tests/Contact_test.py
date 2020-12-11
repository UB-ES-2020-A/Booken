# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import os
import unittest
import sys
import json
parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from models.contact import ContactModel
from models.accounts import AccountModel

import base64
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0411: stupid issue
from db import db
from datetime import date


class ContactTests(unittest.TestCase):

    contact_info = {
        'id': 1,
        'email': "test@gmail.com",
        'full_name': "My name",
        'phone_number': 123456789,
        'contact_query': "Tengo una pregunta jaja",
        'contact_date': date.today().strftime("%d/%m/%Y")
    }

    def setUp(self):

        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)

        acc = AccountModel.query.first()
        acc.type = 1
        acc.save_to_db

        response = self.app.post('api/login',
                                 data=dict(email='test', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_contact(self):
        response = self.add_contact(self.contact_info)
        self.assertEqual(response.status_code, 200)

    def test_get_concrete_contact(self):
        self.add_contact(self.contact_info)
        response = self.app.get('api/contact_info/1', headers=self.auth, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.contact_info, json.loads(response.data)["contact"])

    def test_get_non_existent_contact(self):
        response = self.app.get('api/contact_info/1', headers=self.auth,  follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_model_find_contact_by_email(self):
        self.add_contact(self.contact_info)
        cont = ContactModel.find_by_email("test@gmail.com")
        self.assertEqual("test@gmail.com", cont.email)

    def test_get_contacts(self):
        self.add_contact(self.contact_info)
        self.add_contact(self.contact_info)
        response = self.app.get('api/contact_list', headers=self.auth,  follow_redirects=True)

        tmp_contact_1 = self.contact_info.copy()
        tmp_contact_2 = self.contact_info.copy()

        tmp_contact_1["id"] = 1
        tmp_contact_2["id"] = 2

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["contacts"], [tmp_contact_1, tmp_contact_2])

    def test_delete_contact(self):
        self.add_contact(self.contact_info)
        response = self.app.delete('api/contact_info/1', headers=self.auth,  follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_non_existent_contact(self):
        response = self.app.delete('api/contact_info/1', headers=self.auth,  follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def add_contact(self, info):
        return self.app.post('api/contact_info',
                             data=info,
                             follow_redirects=True)
