# file deepcode ignore C0413: shut it deepcode
import base64
import json
import os
import sys
import unittest
from datetime import datetime

parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from app import setupApp
from db import db
from models.log import LogModel
from models.accounts import AccountModel


class LogModelTests(unittest.TestCase):
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
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.authorization = {'Authorization': 'Basic ' + base64.b64encode(
            bytes(
                str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                'ascii')).decode(
            'ascii')}

    def test_model_json(self):
        log = LogModel.find_by_id(1)
        self.assertEqual(1, log.json()['id'])

    def test_model_find_by_year(self):
        log = LogModel.find_by_month_year(datetime.now().year, datetime.now().month)[0].user_id
        eq = LogModel.find_by_year(datetime.now().year)[0].user_id
        self.assertEqual(1, eq)

    def test_get_logs(self):
        response = self.app.get('api/logs',
                                headers=self.authorization,
                                follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_model_delete_to_db(self):
        log = LogModel.find_by_id(1).delete_from_db()
        self.assertEqual(None, LogModel.find_by_id(1))

    def register(self, info):
        return self.app.post('api/account', data=info, follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)
