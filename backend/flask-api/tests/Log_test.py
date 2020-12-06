import os
import sys
import unittest
from datetime import datetime

from models.log import LogModel

parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from app import setupApp
from db import db


class LogModelTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_model_json(self):
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'america16')
        log = LogModel.find_by_id(1)
        self.assertEqual(1, log.json()['id'])

    def test_model_delete_to_db(self):
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'america16')
        asd = LogModel.find_by_id(1).delete_from_db()
        self.assertEqual(None, LogModel.find_by_id(1))

    def test_model_find_by_year(self):
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'america16')
        self.assertEqual(1, LogModel.find_by_year(datetime.now().year)[0].user_id)

    def test_get_logs(self):
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.get('api/logs', follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)
