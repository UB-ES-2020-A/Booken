# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import os
import unittest
import sys
import json

parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from models.accounts import AccountModel
from models.payment_card import CardModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

import json, base64

class CardModelTests(unittest.TestCase):

    card_info = {
        "id": 1,
        "card_owner": "test",
        "number": "4567",
        "date": "12/2025",
        "payment_method": "Visa"
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)
        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="tes2t@asd.com", password="test"),
                      follow_redirects=True)

    def test_model_save_to_db(self):
        card = CardModel(self.card_info['card_owner'], self.card_info['number'], self.card_info['date'],
                         self.card_info['payment_method'])
        account = AccountModel.query.first()
        account.cards.append(card)
        card.save_to_db()
        self.assertEqual(1, CardModel.find_by_id(1).id)


class CardResourceGetTests(unittest.TestCase):

    card_info = {
        "id": 1,
        "card_owner": "test",
        "number": "4567",
        "date": "12/2025",
        "payment_method": "Visa"
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)

        response = self.app.post('api/login',
                                 data=dict(email='test', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth1 = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="tes2t@asd.com", password="test"),
                      follow_redirects=True)

        response = self.app.post('api/login',
                                 data=dict(email='tes2t@asd.com', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth2 = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

    def test_get_existent_card_from_non_existent_account(self):
        card = CardModel(self.card_info['card_owner'], self.card_info['number'], self.card_info['date'],
                         self.card_info['payment_method'])
        account = AccountModel.query.first()
        account.cards.append(card)
        card.save_to_db()
        response = self.app.get('/api/account/3/card/1', headers=self.auth1, follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_get_existent_card_from_non_owner_account(self):
        card = CardModel(self.card_info['card_owner'], self.card_info['number'], self.card_info['date'],
                         self.card_info['payment_method'])
        account = AccountModel.query.first()
        account.cards.append(card)
        card.save_to_db()
        response = self.app.get('/api/account/2/card/1', headers=self.auth2, follow_redirects=True)
        self.assertEqual(409, response.status_code)

    def test_get_non_existent_card_from_account(self):
        response = self.app.get('/api/account/1/card/12', headers=self.auth1, follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_get_concrete_card(self):
        self.add_card(self.card_info)
        response = self.app.get('api/account/1/card/1', headers=self.auth1, follow_redirects=True)

        tmp = self.card_info.copy()
        tmp.pop("payment_method")
        tmp["method"] = self.card_info["payment_method"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tmp, json.loads(response.data)["card"])

    def test_get_cards(self):
        self.add_card(self.card_info)
        self.add_card(self.card_info)
        response = self.app.get('api/account/1/cards', headers=self.auth1, follow_redirects=True)

        tmp = self.card_info.copy()
        tmp.pop("payment_method")
        tmp["method"] = self.card_info["payment_method"]

        tmp_card_1 = tmp.copy()
        tmp_card_2 = tmp.copy()

        tmp_card_1["id"] = 1

        tmp_card_2["id"] = 2

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["accounts_cards"], [tmp_card_1, tmp_card_2])

    def add_card(self, info):
        return self.app.post('api/account/1/card',
                             data=info,
                             headers=self.auth1,
                             follow_redirects=True)


class CardResourcePostTests(unittest.TestCase):

    card_info = {
        "id": 1,
        "card_owner": "test",
        "number": "4567",
        "date": "12/2025",
        "payment_method": "Visa"
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)

        response = self.app.post('api/login',
                                 data=dict(email='test', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth1 = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="tes2t@asd.com", password="test"),
                      follow_redirects=True)

        response = self.app.post('api/login',
                                 data=dict(email='tes2t@asd.com', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth2 = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

    def test_post_card(self):
        response = self.add_card(self.card_info)
        self.assertEqual(response.status_code, 200)

    def test_post_account_to_non_existent_account(self):
        response = self.app.post('api/account/98/card', headers=self.auth1, data=self.card_info, follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_post_account_to_max_card_number_account(self):
        card = self.card_info
        for i in range(3):
            response = self.app.post('api/account/1/card', headers=self.auth1, data=self.card_info, follow_redirects=True)
        self.assertEqual(403, response.status_code)

    def add_card(self, info):
        return self.app.post('api/account/1/card',
                             data=info,
                             headers=self.auth1,
                             follow_redirects=True)


class CardResourceDeleteTests(unittest.TestCase):

    card_info = {
        "id": 1,
        "card_owner": "test",
        "number": "4567",
        "date": "12/2025",
        "payment_method": "Visa"
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)

        response = self.app.post('api/login',
                                 data=dict(email='test', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth1 = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="tes2t@asd.com", password="test"),
                      follow_redirects=True)

        response = self.app.post('api/login',
                                 data=dict(email='tes2t@asd.com', password='test'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth2 = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

    def test_delete_card(self):
        self.add_card(self.card_info)
        response = self.app.delete('api/account/1/card/1', headers=self.auth1, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_non_assigned_card(self):
        self.add_card(self.card_info)
        response = self.app.delete('api/account/2/card/1', headers=self.auth1, follow_redirects=True)
        self.assertEqual(409, response.status_code)

    def test_delete_non_existent_card(self):
        self.add_card(self.card_info)
        response = self.app.delete('api/account/2/card/15', headers=self.auth1, follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_delete_existent_card_from_non_existent_account(self):
        self.add_card(self.card_info)
        response = self.app.delete('api/account/251/card/1', headers=self.auth1, follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def add_card(self, info):
        return self.app.post('api/account/1/card',
                             data=info,
                             headers=self.auth1,
                             follow_redirects=True)

