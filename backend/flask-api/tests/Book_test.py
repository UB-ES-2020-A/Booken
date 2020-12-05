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
        app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

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

        response = self.app.put('api/book/1', data=put_info, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Test modified', response.data)

    def test_put_book_error(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'

        response = response = self.app.put('api/book/2', data=put_info, follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_put_book_new_author(self):
        self.postBook(self.book_info)

        put_info = self.book_info.copy()
        put_info["name"] = 'Book Test modified'
        put_info["author_name"] = 'Jose Calvo'

        response = self.app.put('api/book/1', data=put_info, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        self.postBook(self.book_info)
        response = self.app.delete('api/book/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_book_error(self):
        self.postBook(self.book_info)
        response = self.app.delete('api/book/2', follow_redirects=True)
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
        return self.app.post('api/book', data=info, follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
