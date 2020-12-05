# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import unittest
import sys

sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db



class WishlistTest(unittest.TestCase):

    account_info = {
        "name": "Test",
        "lastname": "Test",
        "email": "prueba@gmail.com",
        "password": "EsTo123Prueba"
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

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_wishlist(self):
        self.create_account(self.account_info)
        self.postBook(self.book_info)
        response = self.add_wishlist()
        self.assertEqual(response.status_code, 200)


    def test_get_wishlist(self):
        self.create_account(self.account_info)
        self.add_wishlist()
        response = self.app.get('api/wishlist/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_delete_wishlist(self):
        self.create_account(self.account_info)
        self.postBook(self.book_info)
        self.add_wishlist()

        response = self.app.delete('api/wishlist/1/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)


    def add_wishlist(self):
        return self.app.post('api/wishlist/1/1',
                             follow_redirects=True)

    def create_account(self, info):
        return self.register(info)

    def register(self, info):
        return self.app.post('api/account',
                             data=info,
                             follow_redirects=True)

    def postBook(self, info):
        return self.app.post('api/book', data=info, follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
