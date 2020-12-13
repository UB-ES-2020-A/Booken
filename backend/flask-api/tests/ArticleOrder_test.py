# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import base64
import unittest
import sys
import json

sys.path.append('../')
from models.accounts import AccountModel, get_user_roles, verify_account
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

#  deepcode ignore C0413: stupid issue

class ArticleOrderTest(unittest.TestCase):

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

    article_order_info = {
        "price": 1.,
        "id_book": 1,
        "quant": 1
    }

    article_order_2_info = {
        "price": 1.,
        "id_book": 1,
        "quant": 99999999
    }

    article_order_3_info = {
        "price": 1.,
        "id_book": 100,
        "quant": 1
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

    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
    }

    card_info = {
        "card_owner": "Bender Bending Rodríguez",
        "number": "4475482935309482",
        "date": "02/2558",
        "payment_method": "Visa"
    }

    book_info = {
        "isbn": 12345678910,
        "name": 'Book Test',
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

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.register(self.account_admin_info)
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_address(self.address_order_info)
        self.add_order(self.order_info)
        self.postBook(self.book_info)

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_article_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        response = self.add_article_order(self.article_order_info)
        resp = self.add_article_order(self.article_order_2_info)
        resp_order = self.app.post('api/article-order/1000',
                                   data=self.article_order_info,
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)

        resp_book = self.add_article_order(self.article_order_3_info)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp_order.status_code, 404)
        self.assertEqual(resp_book.status_code, 404)

    def test_get_article_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_article_order(self.article_order_info)
        response = self.app.get('api/article-order/1/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        resp = self.app.get('api/article-order/1000/1',
                            headers={'Authorization': 'Basic ' + base64.b64encode(
                                bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                      'ascii')).decode(
                                'ascii')},
                            follow_redirects=True)
        resp_article = self.app.get('api/article-order/1/1000',
                                    headers={'Authorization': 'Basic ' + base64.b64encode(
                                        bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                              'ascii')).decode(
                                        'ascii')},
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp_article.status_code, 404)

    def test_get_articles_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        response = self.app.get('api/articles-order/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        resp = self.app.get('api/articles-order/1000',
                            headers={'Authorization': 'Basic ' + base64.b64encode(
                                bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                      'ascii')).decode(
                                'ascii')},
                            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def test_delete_article_order(self):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        self.add_article_order(self.article_order_info)
        response = self.app.delete('api/article-order/1/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        resp = self.app.delete('api/article-order/1/1000',
                               headers={'Authorization': 'Basic ' + base64.b64encode(
                                   bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                         'ascii')).decode(
                                   'ascii')},
                               follow_redirects=True)
        resp_not_order = self.app.delete('api/article-order/100/1',
                                         headers={'Authorization': 'Basic ' + base64.b64encode(
                                             bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                                   'ascii')).decode(
                                             'ascii')},
                                         follow_redirects=True)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp_not_order.status_code, 404)


    def add_order(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/order/1',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def add_address(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/account/1/address',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def add_article_order(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/article-order/1',
                             data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(acc.id) + ":" + json.loads(resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def add_card(self, info):
        acc = AccountModel.find_by_email("a@a.com")
        acc.type = 2
        acc.save_to_db()
        resp_account_admin = self.login('a@a.com', 'sm22')
        return self.app.post('api/account/1/card',
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

    def postBook(self, info):
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

