# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import base64
import unittest
import sys
import os
import json
parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)

from models.accounts import AccountModel, get_user_roles, verify_account
#  deepcode ignore C0413: stupid issue
from app import setupApp
from db import db


class AccountModelTests(unittest.TestCase):

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

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_model_account_json(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual(acc.json(), {'id': 1, 'name': 'Cristobal', 'lastname': 'Colon', 'email': 'tengo@barcos.tech',
                                      'available_money': 0, 'type': 0})

    def test_model_account_json_addresses(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual(acc.json_with_address(),
                         {'id': 1, 'name': 'Cristobal', 'lastname': 'Colon', 'email': 'tengo@barcos.tech',
                          'available_money': 0, 'type': 0, 'addresses': []})

    def test_model_find_non_existent_account(self):
        acc = AccountModel.find_by_id(92)
        self.assertEqual(None, acc)

    def test_model_rollback_function(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        accMod = acc
        accMod.email = 'lel@asd.com'
        accMod.db_rollback()
        self.assertEqual(accMod.email, acc.email)

    def test_model_get_user_role(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual('client', get_user_roles(acc))

    def test_model_delete_from_db(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        acc.delete_from_db()
        self.assertEqual(None, AccountModel.find_by_email('tengo@barcos.tech'))

    def test_model_account_number(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(AccountModel.get_users()['users']))

    def test_model_find_address_id(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)

        response = self.app.post('api/login',
                                 data=dict(email='tengo@barcos.tech', password='america16'),
                                 follow_redirects=True)
        my_id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        my_auth = auth(my_id,token)

        response = self.add_address(self.address_info,my_auth)
        self.assertEqual(self.address_info['city'],
                         AccountModel.find_by_email('tengo@barcos.tech').find_address_by_id(1).city)

    def test_model_find_non_existent_address_id(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(None, AccountModel.find_by_email('tengo@barcos.tech').find_address_by_id(1))

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def add_address(self, info,auth):
        return self.app.post('api/account/1/address',
                             data=info,
                             headers=auth,
                             follow_redirects=True)


class AccountClassAuxFuncTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_valid_user_login(self):
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(json.loads(response.data)['token'], '')

    def test_valid_token_validity(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        response = self.login('tengo@barcos.tech', 'america16')
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual(acc.id, AccountModel.verify_auth_token(json.loads(response.data)['token']).id)

    def test_invalid_token_validity(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        response = self.login('tengo@barcos.tech', 'america16')
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual(None, AccountModel.verify_auth_token('askldjaofhsah'))

    def test_expired_token_validity(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual(None, AccountModel.verify_auth_token(acc.generate_auth_token(expiration=-1)))

    def test_verify_account(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        self.assertEqual(acc.id, verify_account(acc.id, acc.generate_auth_token()).id)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class AccountResourceGetTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_get_non_existent_account(self):
        response = self.app.get('api/account/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_get_existent_account(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('api/account/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_accounts(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        acc = AccountModel.query.first()
        acc.type = 2
        acc.save_to_db()
        response = self.app.post('api/login',
                                 data=dict(email='tengo@barcos.tech', password='america16'),
                                 follow_redirects=True)

        my_id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        my_auth = auth(my_id,token)
        response = self.app.get('api/accounts', headers=my_auth, follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)


class LoginResourceTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_non_registered_login(self):
        response = self.login('lelaco@ub.edu', '12354asuidjh')
        self.assertEqual(response.status_code, 404)

    def test_register_account(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)

    def test_register_account_with_registered_email(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(200, response.status_code)
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(409, response.status_code)

    def test_login_wrong_password(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.login('tengo@barcos.tech', 'asdasdasdas')
        self.assertEqual(400, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class AccountResourcePutTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_put_account(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/1', follow_redirects=True, data={"name": "CEp", "lastname": "asdas",
                                                                              "email": "lel@a.com"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(200, response.status_code)

    def test_put_non_existent_account(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/99', follow_redirects=True, data={"name": "CEp", "lastname": "asdas",
                                                                               "email": "lel@a.com"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(404, response.status_code)

    def test_put_unauthorized_account(self):
        response = self.register('Cristoasdbal', 'Coloasdn', 'tengo@barcasds.tech', 'amerasdica16')
        self.assertEqual(response.status_code, 200)
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/1', follow_redirects=True, data={"name": "CEp", "lastname": "asdas",
                                                                              "email": "lel@a.com"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(401, response.status_code)

    def test_put_change_password(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/' + str(acc.id) + '/change_password',
                                follow_redirects=True, data={"old_password": "america16", "new_password": "asdas"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(200, response.status_code)

    def test_put_change_email_already_registered_email(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos1.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/2', follow_redirects=True, data={"name": "CEp", "lastname": "asdas",
                                                                              "email": "tengo@barcos1.tech"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(409, response.status_code)

    def test_put_change_password_mismatching_password(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/' + str(acc.id) + '/change_password',
                                follow_redirects=True, data={"old_password": "asidjao", "new_password": "asdas"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(406, response.status_code)

    def test_put_unauthorized_account_change_password(self):
        response = self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        self.assertEqual(response.status_code, 200)
        response = self.register('Cristoasdbal', 'Coloasdn', 'tengo@barcasds.tech', 'amerasdica16')
        self.assertEqual(response.status_code, 200)
        acc = AccountModel.find_by_email('tengo@barcos.tech')
        response = self.login('tengo@barcos.tech', 'america16')
        response = self.app.put('api/account/' + str(2) + '/change_password',
                                follow_redirects=True, data={"old_password": "america16", "new_password": "asdas"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(response.data)['token'], 'ascii')).decode(
                                    'ascii')})
        self.assertEqual(401, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class AccountResourceDeleteTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')
        response = self.app.post('api/login',
                                 data=dict(email='tengo@barcos.tech', password='america16'),
                                 follow_redirects=True)

        id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}

    def test_delete_account_from_db(self):
        response = self.app.delete('api/account/1',
                                   headers=self.auth,
                                   follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_delete_non_existent_account_from_db(self):
        response = self.app.delete('api/account/2',
                                   headers=self.auth,
                                   follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)


def auth(id,token):
    return {'Authorization': 'Basic ' + base64.b64encode(bytes(str(id) + ":" + token, 'ascii'))
            .decode('ascii')}