import unittest
import sys
import json

sys.path.append('../')
from app import setupApp
from db import db


class AccountTests(unittest.TestCase):

    address_info = {
        "id":1,
        "label_name":"Mi casa",
        "name":"test",
        "surnames":"tests",
        "street":"La calle de mi casa",
        "number":32,
        "cp":"08431",
        "city":"Mi city",
        "province":"Mi provincia",
        "telf":123456
    }

    def setUp(self):

        self.app = setupApp().test_client()
        db.drop_all()
        db.create_all()

        self.app.post('/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_address(self):
        response = self.add_address(self.address_info)
        self.assertEqual(response.status_code, 200)

    def test_get_concrete_address(self):
        self.add_address(self.address_info)
        response = self.app.get('/account/1/address/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.address_info, json.loads(response.data)["address"])

    def test_get_addresses(self):
        self.add_address(self.address_info)
        self.add_address(self.address_info)
        response = self.app.get('/account/1/addresses', follow_redirects=True)

        tmp_address_1 = self.address_info.copy()
        tmp_address_2 = self.address_info.copy()

        tmp_address_1["id"] = 1
        tmp_address_2["id"] = 2

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["accounts_addresses"], [tmp_address_1,tmp_address_2])

    def test_modify_address(self):
        self.add_address(self.address_info)

        tmp_address = self.address_info.copy()
        tmp_address["label_name"] = "La casa del vecino"

        self.app.put('/account/1/address/1', data=tmp_address, follow_redirects=True)

        response = self.app.get('/account/1/address/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tmp_address, json.loads(response.data)["address"])


    def test_delete_address(self):
        self.add_address(self.address_info)

        response = self.app.delete('/account/1/address/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)


    def add_address(self, info):
        return self.app.post('/account/1/address',
                             data=info,
                             follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
