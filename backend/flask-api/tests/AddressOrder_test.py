# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import unittest
import sys

sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

#  deepcode ignore C0413: stupid issue

class AddressOrderTest(unittest.TestCase):
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


    account_info = {
        "name": "Test",
        "lastname": "Test",
        "email": "prueba@gmail.com",
        "password": "EsTo123Prueba"
    }

    card_info = {
        "card_owner": "Bender Bending Rodríguez",
        "number": "4475482935309482",
        "date": "02/2558",
        "payment_method": "Visa"
    }
    address_info = {
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

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_address_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_address(self.address_order_info)
        response = self.add_address_order(self.address_order_info)
        resp_notorder = self.app.post('api/address-order/1000/1',
                                      data=self.address_order_info,
                                      follow_redirects=True)
        resp_notacc = self.app.post('api/address-order/1/1000',
                                    data=self.address_order_info,
                                    follow_redirects=True)
        resp_notaddress = self.app.post('api/address-order/1/1/1000',
                                        data=self.address_order_info,
                                        follow_redirects=True)
        resp_address = self.app.post('api/address-order/1/1/1',
                                     data=self.address_order_info,
                                     follow_redirects=True)

        self.add_address_account(self.address_info)
        self.add_address_account(self.address_info)
        self.add_address_account(self.address_info)

        resp_max_address = self.app.post('api/address-order/1/1',
                                         data=self.address_order_info,
                                         follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp_notorder.status_code, 404)
        self.assertEqual(resp_notacc.status_code, 404)
        self.assertEqual(resp_notaddress.status_code, 404)
        self.assertEqual(resp_address.status_code, 200)
        self.assertEqual(resp_max_address.status_code, 404)

    def test_get_address_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_address_order(self.address_order_info)
        response = self.app.get('api/address-order/1/1', follow_redirects=True)
        res_notorder = self.app.get('api/address-order/1000/1', follow_redirects=True)
        res_notaddress = self.app.get('api/address-order/1/1000', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_notorder.status_code, 404)
        self.assertEqual(res_notaddress.status_code, 404)

    def test_get_addresses_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_address(self.address_order_info)
        self.add_order(self.order_info)
        response = self.app.get('api/addresses-order/1', follow_redirects=True)
        resp = self.app.get('api/addresses-order/1000', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def test_delete_address_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_address_order(self.address_order_info)
        response = self.app.delete('api/address-order/1/1', follow_redirects=True)
        resp = self.app.delete('api/address-order/1000/1', follow_redirects=True)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp.status_code, 409)

    def add_order(self, info):
        return self.app.post('api/order/1',
                             data=info,
                             follow_redirects=True)

    def add_address(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             follow_redirects=True)

    def add_address_order(self, info):
        return self.app.post('api/address-order/1/1',
                             data=info,
                             follow_redirects=True)

    def add_card(self, info):
        return self.app.post('api/account/1/card',
                             data=info,
                             follow_redirects=True)

    def create_account(self, info):
        return self.register(info)

    def register(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def add_address_account(self, info):
        return self.app.post('api/account/1/address',
                             data=info,
                             follow_redirects=True)
