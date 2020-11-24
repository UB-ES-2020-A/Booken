import unittest
import sys

sys.path.append('../')
from app import setupApp, AuthorModel, BookModel
from db import db


class BookTests(unittest.TestCase):

    def setUp(self):
        self.app = setupApp().test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_add_book(self):
        response = self.addBook(12345678910, 'Book A', 'Kim Follet', '10/10/1979', 'BCN', 'Spain', 'HUMANIDADES', 2020,
                                'Santillana', 'Castellano', 10.9, 'Synopsis', 'Descripcion', 130, 0, 0, 15, 'asd',
                                'asd')
        self.assertEqual(response.status_code, 200)
        assert b'Book A' in response.data

    def test_getBook(self):
        response = self.getBook()
        #print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.name, 'Book A')

    def test_deleteBook(self):
        response = self.app.delete('/book/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def addBook(self, isbn, name, author_n, author_bd, author_c, author_co, genre, year, editorial, language, price,
                synopsis, description, num_pages, cover_type, num_sales, total_available, cover_image_url,
                back_cover_image_url):
        # author = AuthorModel(author_n, author_bd, author_c, author_co)
        # book = BookModel(isbn, name, [author], genre, year, editorial, language, price,
        #                 synopsis, description, num_pages, cover_type, num_sales, total_available, cover_image_url,
        #                 back_cover_image_url)
        # book.save_to_db()
        return self.app.post('/book',
                             data=dict(isbn=isbn, name=name, author_name=author_n, author_bd=author_bd,
                                       author_city=author_c, author_country=author_co, genre=genre, year=year,
                                       editorial=editorial, language=language, price=price, synopsis=synopsis,
                                       description=description, num_pages=num_pages, cover_type=cover_type,
                                       num_sales=num_sales, total_available=total_available,
                                       cover_image_url=cover_image_url, back_cover_image_url=back_cover_image_url),
                             follow_redirects=True)

    def getBook(self):
        return self.app.get('/book/1', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
