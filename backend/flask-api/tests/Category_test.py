# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
#  deepcode ignore C0411: not an issue
import base64
import unittest
#  deepcode ignore C0411: not an issue
import sys
import json

#  deepcode ignore C0411: not an issue
sys.path.append('../')
from models.accounts import AccountModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db


class CategoryTest(unittest.TestCase):
    category_info = {
        'type': "Test",
    }

    account_dev_info = {
        "name": 'Dev',
        "lastname": 'Dev',
        "email": "s@s.com",
        "password": 'sm22'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.register(self.account_dev_info)
        self.acc = AccountModel.find_by_email("s@s.com")
        self.acc.type = 1
        self.acc.save_to_db()
        self.resp_account_dev = self.login('s@s.com', 'sm22')

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_category(self):
        response = self.add_category(self.category_info)
        resp = self.add_category(self.category_info)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 409)

    def test_get_category(self):
        self.add_category(self.category_info)
        response = self.app.get('api/category/1', follow_redirects=True)
        resp = self.app.get('api/category/1000', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def test_get_categories(self):
        self.add_category(self.category_info)
        self.add_category(self.category_info)
        response = self.app.get('api/categories', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def add_category(self, info):
        return self.app.post('api/category',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def register(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)
