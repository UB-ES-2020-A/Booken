#  deepcode ignore C0411: not an issue
import unittest
#  deepcode ignore C0411: not an issue
import sys
#  deepcode ignore C0411: not an issue
import random

sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db


#  deepcode ignore C0411: not an issue


class BookTests(unittest.TestCase):
    book_info1 = {
        "isbn": 12345678911,
        "name": 'The secret of the Stones',
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
        "isbn": 12345679736,
        "name": 'The secret of the A',
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
        self.app = setupApp(test=True).test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_search_by_name(self):
        self.postBook(self.book_info1)
        self.postBook(self.book_info2)
        lista = ['the', 'sec', 'secret', 'of', 'stones']
        rand = random.choices(lista)
        response = self.search(rand)
        self.assertEqual(response.status_code, 200)
        if rand == ['stones']:
            self.assertIn(b'The secret of the Stones', response.data)
        else:
            self.assertIn(b'The secret of the Stones', response.data)
            self.assertIn(b'The secret of the A', response.data)

    def test_search_by_isbn(self):
        self.postBook(self.book_info1)
        self.postBook(self.book_info2)
        lista = [12, 123, 567, 123456789]
        rand = random.choices(lista)
        response = self.search(rand)
        self.assertEqual(response.status_code, 200)
        if rand == [123456789]:
            self.assertIn(b'12345678911', response.data)
            self.assertIn(b'The secret of the Stones', response.data)
        else:
            self.assertIn(b'12345679736', response.data)
            self.assertIn(b'The secret of the A', response.data)
            self.assertIn(b'The secret of the Stones', response.data)

    def test_search_by_author_name(self):
        self.postBook(self.book_info1)
        self.postBook(self.book_info2)
        lista = ['kim', 'foll', 'follet']
        response = self.search(random.choices(lista))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kim Follet', response.data)
        self.assertIn(b'The secret of the A', response.data)
        self.assertIn(b'The secret of the Stones', response.data)

    def postBook(self, info):
        return self.app.post('/book', data=info, follow_redirects=True)

    def search(self, name):
        return self.app.get('/search', data={'name': name}, follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
