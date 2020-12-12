#  deepcode ignore C0411: not an issue
import base64
import json
import unittest
#  deepcode ignore C0411: not an issue
import sys

#  deepcode ignore C0411: not an issue


sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db
from models.accounts import AccountModel


#  deepcode ignore C0411: not an issue


class InterfaceTests(unittest.TestCase):
    account_admin_info = {
        "name": 'Admin',
        "lastname": 'Admin',
        "email": "a@a.com",
        "password": 'sm22'
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
    interface_info_with_books = {
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
        "t1TxtColor": '#fff',
        "t2Books": [1]
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
        self.authorization = {'Authorization': 'Basic ' + base64.b64encode(
            bytes(
                str(self.acc.id) + ":" + json.loads(self.resp_account_admin.data)['token'],
                'ascii')).decode(
            'ascii')}

    def tearDown(self):
        # Executed after each test
        pass

    def test_get_interfaces(self):
        response = self.app.get('api/interfaces',
                                headers=self.authorization,
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_interface(self):
        response = self.postInterface(self.interface_info)
        self.assertEqual(response.status_code, 200)

    def test_post_interface_with_books(self):
        self.postBook(self.book_info)
        response = self.postInterface(self.interface_info_with_books)
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
        response = self.app.put('/api/interface/1',
                                data=self.interface_info,
                                headers=self.authorization,
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_put_interface_with_books(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info_with_books)
        response = self.app.put('/api/interface/1',
                                data=self.interface_info_with_books,
                                headers=self.authorization,
                                follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_put_interface_error(self):
        self.postInterface(self.interface_info)
        response = self.app.put('/api/interface/4',
                                data=self.interface_info_with_books,
                                headers=self.authorization,
                                follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_interface(self):
        self.postInterface(self.interface_info)
        response = self.app.delete('/api/interface/1',
                                   headers=self.authorization,
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_interface_2(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.delete('/api/interface/1',
                                   headers=self.authorization,
                                   follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_delete_interface_error(self):
        self.postInterface(self.interface_info)
        response = self.app.delete('/api/interface/4',
                                   headers=self.authorization,
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_post_book_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        response = self.app.post('api/interface_books/1/1',
                                 headers=self.authorization,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_book_interface_error_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        response = self.app.post('api/interface_books/2/1',
                                 headers=self.authorization,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_post_book_interface_error_book(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        response = self.app.post('api/interface_books/1/2',
                                 headers=self.authorization,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_get_book_list_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1',
                      headers=self.authorization,
                      follow_redirects=True)
        response = self.app.get('api/interface_books/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_book_list_interface_error(self):
        response = self.app.get('api/interface_books/2', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_book_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1',
                      headers=self.authorization,
                      follow_redirects=True)
        response = self.app.delete('api/interface_books/1/1',
                                   headers=self.authorization,
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book_interface_error_interface(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1',
                      headers=self.authorization,
                      follow_redirects=True)
        response = self.app.delete('api/interface_books/4/1',
                                   headers=self.authorization,
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_book_interface_error_book(self):
        self.postBook(self.book_info)
        self.postInterface(self.interface_info)
        self.app.post('api/interface_books/1/1',
                      headers=self.authorization,
                      follow_redirects=True)
        response = self.app.delete('api/interface_books/1/4',
                                   headers=self.authorization,
                                   follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_change_id_banner(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.post('api/changeposition/1/2',
                                 headers=self.authorization,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_change_id_banner_error_1(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.post('api/changeposition/4/2',
                                 headers=self.authorization,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_change_id_banner_error_2(self):
        self.postInterface(self.interface_info)
        self.postInterface(self.interface_info_2)
        response = self.app.post('api/changeposition/1/4',
                                 headers=self.authorization,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def postBook(self, info):
        return self.app.post('api/book',
                             data=info,
                             headers=self.authorization,
                             follow_redirects=True)

    def postInterface(self, info):
        return self.app.post('/api/interface',
                             data=info,
                             headers=self.authorization,
                             follow_redirects=True)

    def register(self, info):
        return self.app.post('api/account', data=info, follow_redirects=True)

    def login(self, email, password):
        return self.app.post('api/login',
                             data=dict(email=email, password=password),
                             follow_redirects=True)

