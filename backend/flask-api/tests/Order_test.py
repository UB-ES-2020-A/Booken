# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import base64
import unittest
import sys
import json

sys.path.append('../')
from models.accounts import AccountModel, get_user_roles, verify_account
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

#  deepcode ignore C0413: stupid issue

class OrderTest(unittest.TestCase):

    order_info = {
        "date": "29/11/2020 10:50",
        "total": 1.,
        "shipping": 1.,
        "taxes": 1.,
        "state": 0,
        "send_type": 0,
        "card_id": 1,
        "address_id": 1
    }

    account_info = {
        "name": "Test",
        "lastname": "Test",
        "email": "prueba@gmail.com",
        "password": "EsTo123Prueba"
    }

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    card_info = {
        "card_owner": "Bender Bending Rodríguez",
        "number": "4475482935309482",
        "date": "02/2558",
        "payment_method": "Visa"
    }

    address_order_info = {
        "label_name": "Test",
        "name": "Test",
        "surnames": "Test",
        "street": "Test",
        "number": 1,
        "cp": "08080",
        "city": "Barcelona",
        "province": "Barcelona",
        "telf": 666666666,
    }


    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.register(self.account_admin_info)
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_address(self.address_order_info)

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        response = self.add_order(self.order_info)
        resp = self.app.post('api/order/1000',
                             data=self.order_info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 409)

    def test_get_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/order/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'], 'ascii')).decode(
                                 'ascii')},
                                follow_redirects=True)
        resp = self.app.get('api/order/1000',
                            headers={'Authorization': 'Basic ' + base64.b64encode(
                             bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'], 'ascii')).decode(
                             'ascii')},
                            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 409)

    def test_get_orders(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'], 'ascii')).decode(
                                 'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_put_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        info_put = {
            "state": 1
        }
        response = self.app.put('api/order/1', data=info_put,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'], 'ascii')).decode(
                                 'ascii')},
                                follow_redirects=True)
        resp = self.app.put('api/order/1000', data=info_put,
                            headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'], 'ascii')).decode(
                                 'ascii')},
                            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 400)

    def test_delete_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.delete('api/order/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        resp = self.app.delete('api/order/1000',
                               headers={'Authorization': 'Basic ' + base64.b64encode(
                                   bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                         'ascii')).decode(
                                   'ascii')},
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 409)

    def test_get_order_user(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/order-user/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_order_user(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.delete('api/order-user/1/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        resp = self.app.delete('api/order-user/1/1000',
                               headers={'Authorization': 'Basic ' + base64.b64encode(
                                   bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                         'ascii')).decode(
                                   'ascii')},
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 409)

    def test_get_orders_inprogress(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders-state-0/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_send(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders-state-1/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_received(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders-state-2/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_inprogress_list(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders-list-state-0',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_send_list(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders-list-state-1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_received_list(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_order(self.order_info)
        response = self.app.get('api/orders-list-state-2',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def add_order(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/order/1',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def add_address(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)


    def add_card(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/account/1/card',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def create_account(self, info):
        return self.register(info)

    def register(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)