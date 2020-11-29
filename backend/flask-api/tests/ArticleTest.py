import unittest
import sys
sys.path.append('../')
from app import setupApp
from db import db

class ArticleTest(unittest.TestCase):

    article_info = {
        'price': "Test",
        'categoria': "HUMANIDADES",
        'quant': 1
    }

    def setUp(self):
        self.app = setupApp().test_client()
        db.drop_all()
        db.create_all()

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
