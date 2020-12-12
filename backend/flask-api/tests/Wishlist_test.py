# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import base64
import unittest
import sys
import json

sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db
#  deepcode ignore C0413: stupid issue
from models.wishlist import WishlistModel
from models.accounts import AccountModel


class WishlistTest(unittest.TestCase):
    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
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

    book_info2 = {
        "isbn": 12345678910,
        "name": 'Book Test 2',
        "author_name": 'Kim Follet',
        "author_bd": '10/10/1979',
        "author_city": "BCN",
        "author_country": "Spain",
        "genre": 'HUMANIDADES',
        "year": 2020,
        "editorial": 'Santillana',
        "language": 'Castellano',
        "price": 11.9,
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
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_wishlist(self):
        self.postBook(self.book_info)
        response = self.add_wishlist()
        resp_not_acc = self.app.post('api/wishlist/1000/1',
                                     headers={'Authorization': 'Basic ' + base64.b64encode(
                                         bytes(
                                             str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                         'ascii')},
                                     follow_redirects=True)
        resp_not_book = self.app.post('api/wishlist/1/1000',
                                      headers={'Authorization': 'Basic ' + base64.b64encode(
                                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                              'token'],
                                                'ascii')).decode(
                                          'ascii')},
                                      follow_redirects=True)
        response_book_exist = self.add_wishlist()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp_not_acc.status_code, 404)
        self.assertEqual(resp_not_book.status_code, 404)
        self.assertEqual(response_book_exist.status_code, 400)

    def test_get_wishlist(self):
        self.add_wishlist()
        response = self.app.get('api/wishlist/1',
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                        'token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_delete_wishlist(self):
        self.postBook(self.book_info)
        self.add_wishlist()

        response = self.app.delete('api/wishlist/1/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                           'token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        resp_not_acc = self.app.delete('api/wishlist/1000/1',
                                       headers={'Authorization': 'Basic ' + base64.b64encode(
                                           bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                               'token'],
                                                 'ascii')).decode(
                                           'ascii')},
                                       follow_redirects=True)
        resp_not_book = self.app.delete('api/wishlist/1/1000',
                                        headers={'Authorization': 'Basic ' + base64.b64encode(
                                            bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                                'token'],
                                                  'ascii')).decode(
                                            'ascii')},
                                        follow_redirects=True)
        self.postBook(self.book_info2)
        response_book_exist = self.app.delete('api/wishlist/1/2',
                                              headers={'Authorization': 'Basic ' + base64.b64encode(
                                                  bytes(
                                                      str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                                          'token'],
                                                      'ascii')).decode(
                                                  'ascii')},
                                              follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp_not_acc.status_code, 404)
        self.assertEqual(resp_not_book.status_code, 404)
        self.assertEqual(response_book_exist.status_code, 400)

    def test_get_wishlist_by_id(self):
        self.postBook(self.book_info)
        resp = self.add_wishlist()
        response = WishlistModel.find_by_id(1)
        self.assertEqual(response.json(), json.loads(resp.data)["wl"])

    def add_wishlist(self):
        return self.app.post('api/wishlist/1/1',
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def register(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def postBook(self, info):
        return self.app.post('api/book', data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                       'ascii')).decode(
                                 'ascii')},
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)
