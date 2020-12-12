# file deepcode ignore C0413: shut it deepcode
import base64
import json
import os
import sys
import unittest
parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)

from models.review import ReviewModel
from models.accounts import AccountModel
from app import setupApp
from db import db


class ReviewModelTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')


    def test_model_find_review_by_book(self):

        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        self.assertEqual(201, response.status_code)
        rev = ReviewModel.find_by_book(1)
        self.assertEqual("lel", rev[0].comment)

    def test_model_find_review_by_user(self):
        response = self.app.post('api/review',
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"}, follow_redirects=True)
        self.assertEqual(201, response.status_code)
        rev = ReviewModel.find_by_user(1)
        self.assertEqual("lel", rev[0].comment)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)


    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class ReviewListUserResourceGetTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_get_review_list_by_user(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.get('api/reviewsUser/1', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual("lel", json.loads(response.data)['reviews'][0]['comment'])

    def test_get_review_list_by_non_exisintg_user(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.get('api/reviewsUser/92', follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class ReviewListBookResourceGetTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_get_review_list_by_book(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.get('api/reviewsBook/1', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual("lel", json.loads(response.data)['reviews'][0]['comment'])

    def test_get_review_list_by_book_non_existing_book(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.get('api/reviewsBook/92', follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class ReviewListResourceGetTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_get_review_list(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.get('api/reviews', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual("lel", json.loads(response.data)['reviews'][0]['comment'])

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)

class ReviewResourceGetTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_get_review(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.get('api/review/1', follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_get_non_existent_review(self):
        response = self.app.get('api/review/59', follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class ReviewResourcePostTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_post_review(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        self.assertEqual(201, response.status_code)

    def test_post_review_non_existent_account(self):
        response = self.app.post('api/review', data={"user_id": 92, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_post_review_non_existent_book(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 92, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)
    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)


    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class ReviewResourcePutTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_put_review(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.put('api/review/1', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                      "date": "25/11/2090 11:25", "valuation": 4,
                                                      "comment": "lel"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        rev = ReviewModel.find_by_id(1)
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, rev.valuation)

    def test_put_non_existing_review(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.put('api/review/92', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                       "date": "25/11/2090 11:25", "valuation": 4,
                                                       "comment": "lel"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        rev = ReviewModel.find_by_id(1)
        self.assertEqual(404, response.status_code)

    def test_put_review_non_existing_account(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.put('api/review/1', data={"user_id": 92, "book_id": 1, "title": "asd",
                                                      "date": "25/11/2090 11:25", "valuation": 4,
                                                      "comment": "lel"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        rev = ReviewModel.find_by_id(1)
        self.assertEqual(404, response.status_code)

    def test_put_review_non_existing_book(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.put('api/review/1', data={"user_id": 1, "book_id": 92, "title": "asd",
                                                      "date": "25/11/2090 11:25", "valuation": 4,
                                                      "comment": "lel"},
                                headers={'Authorization': 'Basic ' + base64.b64encode(
                                    bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                          'ascii')).decode(
                                    'ascii')},
                                follow_redirects=True)
        rev = ReviewModel.find_by_id(1)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)


class ReviewResourceDeleteTests(unittest.TestCase):

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
        self.register_info(self.account_admin_info)
        self.acc = AccountModel.find_by_email("a@a.com")
        self.acc.type = 2
        self.acc.save_to_db()
        self.resp_account_admin = self.login('a@a.com', 'sm22')
        self.app.post('api/book', data=self.book_info,
                      headers={'Authorization': 'Basic ' + base64.b64encode(
                          bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                'ascii')).decode(
                          'ascii')},
                      follow_redirects=True)
        self.register('Cristobal', 'Colon', 'tengo@barcos.tech', 'america16')

    def test_delete_review(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.delete('api/review/1',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(200, response.status_code)

    def test_delete_non_existent_review(self):
        response = self.app.post('api/review', data={"user_id": 1, "book_id": 1, "title": "asd",
                                                     "date": "25/11/2090 11:25", "valuation": 5,
                                                     "comment": "lel"},
                                 headers={'Authorization': 'Basic ' + base64.b64encode(
                                     bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                           'ascii')).decode(
                                     'ascii')},
                                 follow_redirects=True)
        response = self.app.delete('api/review/92',
                                   headers={'Authorization': 'Basic ' + base64.b64encode(
                                       bytes(str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                                             'ascii')).decode(
                                       'ascii')},
                                   follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def register(self, name, lname, email, password):
        return self.app.post('api/account',
                             data=dict(name=name, lastname=lname, email=email, password=password),
                             follow_redirects=True)

    def register_info(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)
