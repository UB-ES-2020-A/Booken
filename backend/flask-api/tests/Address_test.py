# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import base64
import os
import unittest
import sys
import json

parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from models.address import AddressModel
from models.accounts import AccountModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db


class AddressModelTests(unittest.TestCase):
    address_info = {
        "id": 1,
        "label_name": "Mi casa",
        "name": "test",
        "surnames": "tests",
        "street": "La calle de mi casa",
        "number": 32,
        "cp": "08431",
        "city": "Mi city",
        "province": "Mi provincia",
        "telf": 123456
    }

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_find_address_in_account(self):
        response = self.add_address(self.address_info)
        self.assertEqual(response.status_code, 200)
        add = AddressModel.find_by_account_id(1)[0]
        self.assertEqual(self.address_info['city'], add.city)

    def test_model_address_json(self):
        response = self.add_address(self.address_info)
        self.assertEqual(response.status_code, 200)
        add = AddressModel.find_by_id(1)
        self.assertEqual(add.json(),
                         {"id": 1, "label_name": "Mi casa", "name": "test", "surnames": "tests", "street": "La calle de"
                                                                                                           + " mi casa",
                          "number": 32, "cp": "08431", "city": "Mi city", "province": "Mi provincia",
                          "telf": 123456})

    def add_address(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
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


class AddressResourceGetTests(unittest.TestCase):
    address_info = {
        "id": 1,
        "label_name": "Mi casa",
        "name": "test",
        "surnames": "tests",
        "street": "La calle de mi casa",
        "number": 32,
        "cp": "08431",
        "city": "Mi city",
        "province": "Mi provincia",
        "telf": 123456
    }

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_get_non_assigned_address_in_account(self):
        self.add_address(self.address_info)
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test2", password="test"),
                      follow_redirects=True)
        response = self.app.get('api/account/2/address/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(409, response.status_code)

    def test_get_non_existing_address_from_account(self):
        self.add_address(self.address_info)
        response = self.app.get('api/account/1/address/95',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_get_concrete_address(self):
        self.add_address(self.address_info)
        response = self.app.get('api/account/1/address/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.address_info, json.loads(response.data)["address"])

    def test_get_addresses(self):
        self.add_address(self.address_info)
        self.add_address(self.address_info)
        response = self.app.get('api/account/1/addresses',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)

        tmp_address_1 = self.address_info.copy()
        tmp_address_2 = self.address_info.copy()

        tmp_address_1["id"] = 1
        tmp_address_2["id"] = 2

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["accounts_addresses"], [tmp_address_1, tmp_address_2])

    def add_address(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
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


class AddressResourcePostTests(unittest.TestCase):
    address_info = {
        "id": 1,
        "label_name": "Mi casa",
        "name": "test",
        "surnames": "tests",
        "street": "La calle de mi casa",
        "number": 32,
        "cp": "08431",
        "city": "Mi city",
        "province": "Mi provincia",
        "telf": 123456
    }

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_post_address(self):
        response = self.add_address(self.address_info)
        self.assertEqual(response.status_code, 200)

    def test_post_address_non_existing_account(self):
        response = self.app.post('api/account/25/address',
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 data=self.address_info, follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_post_address_max_amount_address(self):
        for i in range(4):
            response = self.app.post('api/account/1/address',
                                     headers={'Authorization': 'Basic ' + base64.b64encode(
                                         bytes(
                                             str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                         'ascii')},
                                     data=self.address_info, follow_redirects=True)
        self.assertEqual(403, response.status_code)

    def add_address(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
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


class AddressResourcePutTests(unittest.TestCase):
    address_info = {
        "id": 1,
        "label_name": "Mi casa",
        "name": "test",
        "surnames": "tests",
        "street": "La calle de mi casa",
        "number": 32,
        "cp": "08431",
        "city": "Mi city",
        "province": "Mi provincia",
        "telf": 123456
    }

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_put_address_non_existing_account(self):
        response = self.app.put('api/account/25/address/1', data=self.address_info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_put_address_non_existing_address(self):
        response = self.app.put('api/account/1/address/25', data=self.address_info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_put_address_non_assigned_address(self):
        response = self.add_address(self.address_info)
        self.assertEqual(response.status_code, 200)
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test2", password="test"),
                      follow_redirects=True)
        response = self.app.put('api/account/2/address/1', data=self.address_info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(409, response.status_code)

    def test_put_address(self):
        self.add_address(self.address_info)

        tmp_address = self.address_info.copy()
        tmp_address["label_name"] = "La casa del vecino"

        self.app.put('api/account/1/address/1', data=tmp_address,
                     headers={'Authorization': 'Basic ' + base64.b64encode(
                         bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                               'ascii')).decode(
                         'ascii')},
                     follow_redirects=True)

        response = self.app.get('api/account/1/address/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tmp_address, json.loads(response.data)["address"])

    def add_address(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
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


class AddressResourceDeleteTests(unittest.TestCase):
    address_info = {
        "id": 1,
        "label_name": "Mi casa",
        "name": "test",
        "surnames": "tests",
        "street": "La calle de mi casa",
        "number": 32,
        "cp": "08431",
        "city": "Mi city",
        "province": "Mi provincia",
        "telf": 123456
    }

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_delete_non_assigned_address_in_account(self):
        self.add_address(self.address_info)
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test2", password="test"),
                      follow_redirects=True)
        response = self.app.delete('api/account/2/address/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(409, response.status_code)

    def test_delete_address_non_existing_address(self):
        response = self.app.delete('api/account/1/address/25', data=self.address_info,
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_delete_address(self):
        self.add_address(self.address_info)
        response = self.app.delete('api/account/1/address/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def add_address(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
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
