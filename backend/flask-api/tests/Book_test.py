#  deepcode ignore C0411: not an issue
import unittest
#  deepcode ignore C0411: not an issue
import sys
#  deepcode ignore C0411: not an issue
sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db
#  deepcode ignore C0411: not an issue
from datetime import date
#  deepcode ignore C0413: stupid issue


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

    def setUp(self):
        self.app = setupApp().test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_post_book(self):
        response = self.postBook(self.book_info)
        self.assertEqual(response.status_code, 200)

    def test_get_Book(self):
        self.postBook(self.book_info)
        response = self.getBook()

        self.assertEqual(response.status_code, 200)
        assert b'Book post' in response.data

    def test_put_book(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'

        response = self.putBook(put_info)
        self.assertEqual(response.status_code, 200)
        assert b'Book Test modified' in response.data

    def test_delete_Book(self):
        self.postBook(self.book_info)
        response = self.deleteBook()
        self.assertEqual(response.status_code, 200)

    def postBook(self, info):
        return self.app.post('/book', data=info, follow_redirects=True)

    def getBook(self):
        return self.app.get('/book/1', follow_redirects=True)

    def putBook(self, info):
        return self.app.put('/book/1', data=info, follow_redirects=True)

    def deleteBook(self):
        return self.app.delete('/book/1', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()