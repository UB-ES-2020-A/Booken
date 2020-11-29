#  deepcode ignore C0411: not an issue
import unittest
#  deepcode ignore C0411: not an issue
import sys
#  deepcode ignore C0411: not an issue
sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0411: not an issue
from db import db
#  deepcode ignore C0411: not an issue


class ArticleTest(unittest.TestCase):

    article_info = {
        'price': 1,
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
