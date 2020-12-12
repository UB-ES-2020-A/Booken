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


#  deepcode ignore C0411: not an issue


class BookTests(unittest.TestCase):
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
        self.register(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')

    def tearDown(self):
        # Executed after each test
        pass

    def test_post_book(self):
        response = self.postBook(self.book_info)
        self.assertEqual(response.status_code, 200)

    def test_post_book_error(self):
        self.postBook(self.book_info)
        response = self.postBook(self.book_info)
        self.assertEqual(response.status_code, 409)

    def test_post_book_same_author(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'

        response = self.postBook(put_info)
        self.assertEqual(response.status_code, 200)

    def test_get_Book(self):
        self.postBook(self.book_info)
        response = self.app.get('api/book/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book post', response.data)

    def test_get_book_error(self):
        self.postBook(self.book_info)
        response = self.app.get('api/book/2', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_put_book(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'

        response = self.app.put('api/book/1', data=put_info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Test modified', response.data)

    def test_put_book_error(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'

        response = self.app.put('api/book/2', data=put_info,
                                           headers={'Authorization': 'Basic ' + base64.b64encode(
                                               bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)[
                                                   'token'],
                                                     'ascii')).decode(
                                               'ascii')},
                                           follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_put_book_new_author(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'
        put_info["author_name"] = 'Jose Calvo'

        response = self.app.put('api/book/1', data=put_info,
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        self.postBook(self.book_info)
        response = self.app.delete('api/book/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book_error(self):
        self.postBook(self.book_info)
        response = self.app.delete('api/book/2',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_get_book_list_genre(self):
        self.postBook(self.book_info)
        response = self.app.get('/api/books/HUMANIDADES', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'HUMANIDADES', response.data)

    def test_get_book_list(self):
        self.postBook(self.book_info)
        response = self.app.get('/api/books', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book post', response.data)

    def test_book_author(self):
        self.postBook(self.book_info)
        response = self.app.get('/api/book/1/author', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_book_author_error(self):
        self.postBook(self.book_info)
        response = self.app.get('/api/book/4/author', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def postBook(self, info):
        return self.app.post('api/book', data=info,
                             headers={'Authorization': 'Basic ' + base64.b64encode(
                                 bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
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
