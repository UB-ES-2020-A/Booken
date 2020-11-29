import unittest
import sys
import json

sys.path.append('../')
from app import setupApp
from db import db


class CardTests(unittest.TestCase):

    card_info = {
        "id": 1,
        "card_owner": "test",
        "number": "4567",
        "date": "12/2025",
        "payment_method": "Visa"
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

    def test_create_card(self):
        response = self.add_card(self.card_info)
        self.assertEqual(response.status_code, 200)

    def test_get_concrete_card(self):
        self.add_card(self.card_info)
        response = self.app.get('/account/1/card/1', follow_redirects=True)

        tmp = self.card_info.copy()
        tmp.pop("payment_method")
        tmp["method"] = self.card_info["payment_method"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tmp, json.loads(response.data)["card"])

    def test_get_cards(self):
        self.add_card(self.card_info)
        self.add_card(self.card_info)
        response = self.app.get('/account/1/cards', follow_redirects=True)

        tmp = self.card_info.copy()
        tmp.pop("payment_method")
        tmp["method"] = self.card_info["payment_method"]

        tmp_card_1 = tmp.copy()
        tmp_card_2 = tmp.copy()

        tmp_card_1["id"] = 1

        tmp_card_2["id"] = 2

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["accounts_cards"], [tmp_card_1,tmp_card_2])

    def test_delete_card(self):
        self.add_card(self.card_info)

        response = self.app.delete('/account/1/card/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)


    def add_card(self, info):
        return self.app.post('/account/1/card',
                             data=info,
                             follow_redirects=True)

if __name__ == '__main__':
    unittest.main()