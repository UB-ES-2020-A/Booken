# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
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
#  deepcode ignore C0413: stupid issue


class ArticleTest(unittest.TestCase):

    article_info = {
        'price': 1,
        'categoria': "HUMANIDADES",
        'quant': 1,
        'book_id': 1
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

    def setUp(self):
        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()
        self.postBook(self.book_info)

    def postBook(self, info):
        return self.app.post('/book', data=info, follow_redirects=True)

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_article(self):
        response = self.add_article(self.article_info)
        self.assertEqual(response.status_code, 201)


    def test_get_article(self):
        self.add_article(self.article_info)
        response = self.app.get('/article/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_get_articles(self):
        self.add_article(self.article_info)
        self.add_article(self.article_info)
        response = self.app.get('/articles', follow_redirects=True)

        article_1 = self.article_info.copy()
        article_2 = self.article_info.copy()

        article_1["id"] = 1
        article_2["id"] = 2

        self.assertEqual(response.status_code, 200)

    def test_delete_article(self):
        self.add_article(self.article_info)

        response = self.app.delete('/article/1', follow_redirects=True)

        self.assertEqual(response.status_code, 201)


    def add_article(self, info):
        return self.app.post('/article',
                             data=info,
                             follow_redirects=True)
if __name__ == '__main__':
    unittest.main()
