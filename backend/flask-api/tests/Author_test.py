# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
#  deepcode ignore C0411: not an issue
import base64
import os
import unittest
import json
#  deepcode ignore C0411: not an issue
import sys

parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
#  deepcode ignore C0411: not an issue
from models.author import AuthorModel
from models.accounts import AccountModel

sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db
#  deepcode ignore C0411: not an issue
from datetime import date


#  deepcode ignore C0413: stupid issue


class AuthorModelTest(unittest.TestCase):
    author_info = {
        'name': "Test",
        'birth_date': "29/11/2020",
        'city': "Barcelona",
        'country': "Spain"
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def test_model_no_authors_length(self):
        self.assertEqual(0, AuthorModel.num_authors())


class AuthorResourceGetTest(unittest.TestCase):
    author_info = {
        'name': "Test",
        'birth_date': "29/11/2020",
        'city': "Barcelona",
        'country': "Spain"
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
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_get_author(self):
        self.add_author(self.author_info)
        response = self.app.get('api/author/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_author(self):
        self.add_author(self.author_info)
        response = self.app.get('api/author/59', follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    def test_get_authors(self):
        self.add_author(self.author_info)
        self.add_author(self.author_info)
        response = self.app.get('api/authors', follow_redirects=True)

        author_1 = self.author_info.copy()
        author_2 = self.author_info.copy()

        author_1["id"] = 1
        author_2["id"] = 2

        self.assertEqual(response.status_code, 200)

    def add_author(self, info):
        return self.app.post('api/author', data=info,
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


class AuthorResourcePostTest(unittest.TestCase):
    author_info = {
        'name': "Test",
        'birth_date': "29/11/2020",
        'city': "Barcelona",
        'country': "Spain"
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
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_post_author(self):
        response = self.add_author(self.author_info)
        self.assertEqual(response.status_code, 201)

    def add_author(self, info):
        return self.app.post('api/author', data=info,
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


class AuthorResourcePutTest(unittest.TestCase):
    author_info = {
        'name': "Test",
        'birth_date': "29/11/2020",
        'city': "Barcelona",
        'country': "Spain"
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
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_put_author(self):
        self.add_author(self.author_info)
        info = {
            'name': "TestPut",
            'birth_date': date.today().strftime('%Y-%m-%d'),
            'city': "Barcelona",
            'country': "Spain"
        }
        response = self.app.put('api/author/1', data=info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_put_non_existent_author(self):
        self.add_author(self.author_info)
        info = {
            'name': "TestPut",
            'birth_date': date.today().strftime('%Y-%m-%d'),
            'city': "Barcelona",
            'country': "Spain"
        }
        response = self.app.put('api/author/59', data=info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    def add_author(self, info):
        return self.app.post('api/author', data=info,
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


class AuthorResourceDeleteTest(unittest.TestCase):
    author_info = {
        'name': "Test",
        'birth_date': "29/11/2020",
        'city': "Barcelona",
        'country': "Spain"
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
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def test_delete_author(self):
        self.add_author(self.author_info)
        response = self.app.delete('api/author/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_delete_non_existent_author(self):
        self.add_author(self.author_info)
        response = self.app.delete('api/author/59',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    def add_author(self, info):
        return self.app.post('api/author', data=info,
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
