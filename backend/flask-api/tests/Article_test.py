# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
#  deepcode ignore C0411: not an issue
import base64
import unittest
#  deepcode ignore C0411: not an issue
import sys
import json
#  deepcode ignore C0411: not an issue
sys.path.append('../')
from models.accounts import AccountModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db
#  deepcode ignore C0413: stupid issue


class ArticleTest(unittest.TestCase):

    article_info = {
        'price': 1,
        'categoria': "HUMANIDADES",
        'quant': 1,
        'book_id': 1
    }
    book_info = {
        "isbn": 12345678911,
        "name": 'Book post',
        "author_name": 'Kim Follet',
        "author_bd": '10/10/1979',
        "author_city": "BCN",
        "author_country": "Spain",
        "genre": 'HUMANIDADES',
        "year": 2020,
        "editorial": 'Santillana',
        "language": 'Castellano',
        "price": 10.9,
        "synopsis": 'Synopsis',
        "description": 'Descripcion',
        "num_pages": 130,
        "cover_type": 0,
        "num_sales": 0,
        "total_available": 15,
        "cover_image_url": 'asd',
        "back_cover_image_url": 'asd'
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
        self.postBook(self.book_info)


    def postBook(self, info):
        self.register(self.account_admin_info)
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/book', data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_article(self):
        response = self.add_article(self.article_info)
        self.assertEqual(response.status_code, 201)


    def test_get_article(self):
        self.register(self.account_admin_info)
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_article(self.article_info)
        response = self.app.get('api/article/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        resp = self.app.get('api/article/1000',
                            headers={'Authorization': 'Basic ' + base64.b64encode(
                                bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                      'ascii')).decode(
                                'ascii')},
                            follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def test_get_articles(self):
        self.register(self.account_admin_info)
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_article(self.article_info)
        self.add_article(self.article_info)
        response = self.app.get('api/articles',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)

        article_1 = self.article_info.copy()
        article_2 = self.article_info.copy()

        article_1["id"] = 1
        article_2["id"] = 2

        self.assertEqual(response.status_code, 200)

    def test_delete_article(self):
        self.register(self.account_admin_info)
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_article(self.article_info)

        response = self.app.delete('api/article/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        resp = self.app.delete('api/article/1000',
                               headers={'Authorization': 'Basic ' + base64.b64encode(
                                   bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                         'ascii')).decode(
                                   'ascii')},
                               follow_redirects=True)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp.status_code, 404)

    def add_article(self, info):
        self.register(self.account_admin_info)
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/article',
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

