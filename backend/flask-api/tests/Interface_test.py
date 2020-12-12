#  deepcode ignore C0411: not an issue
import unittest
#  deepcode ignore C0411: not an issue
import sys

#  deepcode ignore C04
#  11: not an issue
sys.path.append('../')
import json
from models.accounts import AccountModel
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db

import base64

#  deepcode ignore C0411: not an issue


class InterfaceTests(unittest.TestCase):
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

    interface_info = {
        "front_type": 1,
        "t2BookMode": -1,
        "t1BackgndURL": 'asd',
        "t1BackgndCOL": 'asd',
        "t1LinkTo": 'asd',
        "t1Tit": 'asd',
        "t1Separator": 'false',
        "t1Sub": "asd",
        "t1Small": 'asd',
        "t2RowTitle": 'asd',
        "t2RowNumber": 1,
        "t1TxtColor": '#fff'
    }

    interface_info_2 = {
        "front_type": 2,
        "t2BookMode": -2,
        "t1BackgndURL": 'asdasd',
        "t1BackgndCOL": 'asdasd',
        "t1LinkTo": 'asdasd',
        "t1Tit": 'asdasd',
        "t1Separator": 'false',
        "t1Sub": "asdasd",
        "t1Small": 'asdasd',
        "t2RowTitle": 'asdasd',
        "t2RowNumber": 1,
        "t1TxtColor": '#fff'
    }

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

        self.app.post('api/account',
                      data=dict(name="test", lastname="test", email="test", password="test"),
                      follow_redirects=True)

        acc = AccountModel.query.first()
        acc.type = 2
        acc.save_to_db()

        response = self.app.post('api/login',
                                 data=dict(email='test', password='test'),
                                 follow_redirects=True)

        my_id = json.loads(response.data)['id']
        token = json.loads(response.data)['token']
        self.auth = {'Authorization': 'Basic ' + base64.b64encode(bytes(str(my_id) + ":" + token, 'ascii'))
            .decode('ascii')}

    def tearDown(self):
        # Executed after each test
        pass

    def test_get_interfaces(self):
        response = self.app.get('api/interfaces', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_interface(self):
        response = self.postInterface(self.interface_info)
        self.assertEqual(response.status_code, 200)

    def test_get_interface(self):
        self.postInterface(self.interface_info)
        response = self.app.get('api/interface/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_interface_error(self):
        self.postInterface(self.interface_info)
        response = self.app.get('api/interface/4', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_put_interface(self):
        self.postInterface(self.interface_info)
        response = self.app.put('/api/interface/1', data=self.interface_info, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_put_interface_error(self):
        self.postInterface(self.interface_info)
        response = self.app.put('/api/interface/4', data=self.interface_info, follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_interface(self):
        self.postInterface(self.interface_info)
        response = self.app.delete('/api/interface/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_interface_error(self):
        self.postInterface(self.interface_info)
        response = self.app.delete('/api/interface/4', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_post_book_interface(self):
        response = self.postBook(self.book_info)
        response = self.postInterface(self.interface_info)
        response = self.app.post('api/interface_books/1/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_book_interface_error_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        response = self.app.post('api/interface_books/2/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_post_book_interface_error_book(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        response = self.app.post('api/interface_books/1/2', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_get_book_list_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1', follow_redirects=True)
        response = self.app.get('api/interface_books/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_book_list_interface_error(self):
        response = self.app.get('api/interface_books/2', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_book_interface(self):
        respone = self.postBook(self.book_info)
        respone = self.postInterface(self.interface_info)
        respone = self.app.post('api/interface_books/1/1', follow_redirects=True)
        response = self.app.delete('api/interface_books/1/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book_interface_error_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1', follow_redirects=True)
        response = self.app.delete('api/interface_books/4/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_book_interface_error_book(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1', follow_redirects=True)
        response = self.app.delete('api/interface_books/1/4', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_change_id_banner(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.post('api/changeposition/1/2', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_change_id_banner_error_1(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.post('api/changeposition/4/2', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_change_id_banner_error_2(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.post('api/changeposition/1/4', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def postBook(self, info):
        return self.app.post('api/book', data=info, headers=self.auth, follow_redirects=True)

    def postInterface(self, info):
        return self.app.post('/api/interface', data=info, follow_redirects=True)
