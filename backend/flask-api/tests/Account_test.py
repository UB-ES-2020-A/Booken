# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import unittest
import sys
import json
sys.path.append('../*')
sys.path.append('../models/*')
sys.path.append('../resources')
#  deepcode ignore C0413: stupid issue
from app import setupApp
from db import db


class AccountTests(unittest.TestCase):

    def setUp(self):

        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_non_registered_login(self):
        response = self.login('lelaco@ub.edu', '12354asuidjh')
        self.assertEqual(response.status_code, 404)

    def test_register_account(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(json.loads(response.data)['token'], '')

    def register(self, name, lname, email, password):
        return self.app.post('/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
