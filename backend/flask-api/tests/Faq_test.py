# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import base64
import unittest
import sys
import json

sys.path.append('../')
from models.accounts import AccountModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db


class FaqTest(unittest.TestCase):
    faq_info = {
        'category': "Test",
        'question': "test",
        'answer': "test",
    }

    category_info = {
        'type': "test2",
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

    def test_create_faq(self):
        response = self.add_faq(self.faq_info)
        self.assertEqual(response.status_code, 200)

    def test_get_faq(self):
        self.add_faq(self.faq_info)
        response = self.app.get('api/faq/1', follow_redirects=True)
        resp = self.app.get('api/faq/1000', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def test_get_faqs(self):
        self.add_faq(self.faq_info)
        self.add_faq(self.faq_info)
        response = self.app.get('api/faqs', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_put_faq(self):
        self.add_faq(self.faq_info)
        info = {
            'category': "Test2",
            'question': "test2",
            'answer': "test2",
        }
        response = self.app.put('api/faq/1', data=info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        resp = self.app.put('api/faq/1000', data=info,
                            headers={'Authorization': 'Basic ' + base64.b64encode(
                                bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                      'ascii')).decode(
                                'ascii')},
                            follow_redirects=True)
        self.add_category(self.category_info)
        info_aux = {
            'category': "test2",
            'question': "test2",
            'answer': "test2",
        }
        resp_cat_exist = self.app.put('api/faq/1', data=info_aux,
                                      headers={'Authorization': 'Basic ' + base64.b64encode(
                                          bytes(
                                              str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                              'ascii')).decode(
                                          'ascii')},
                                      follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp_cat_exist.status_code, 200)

    def test_delete_faq(self):
        self.add_faq(self.faq_info)

        response = self.app.delete('api/faq/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        resp = self.app.delete('api/faq/1000',
                               headers={'Authorization': 'Basic ' + base64.b64encode(
                                   bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                         'ascii')).decode(
                                   'ascii')},
                               follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def add_faq(self, info):
        return self.app.post('api/faq',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_dev.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

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
