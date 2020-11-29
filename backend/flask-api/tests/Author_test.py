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


class AuthorTest(unittest.TestCase):

    author_info = {
        'name': "Test",
        'birth_date': "29/11/2020",
        'city': "Barcelona",
        'country': "Spain"
    }

    def setUp(self):

        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_author(self):
        response = self.add_author(self.author_info)
        self.assertEqual(response.status_code, 201)


    def test_get_author(self):
        self.add_author(self.author_info)
        response = self.app.get('/author/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_get_authors(self):
        self.add_author(self.author_info)
        self.add_author(self.author_info)
        response = self.app.get('/authors', follow_redirects=True)

        author_1 = self.author_info.copy()
        author_2 = self.author_info.copy()

        author_1["id"] = 1
        author_2["id"] = 2

        self.assertEqual(response.status_code, 200)

    def test_put_author(self):
        self.add_author(self.author_info)
        info = {
        'name': "TestPut",
        'birth_date': date.today().strftime('%Y-%m-%d'),
        'city': "Barcelona",
        'country': "Spain"
        }
        response = self.app.put('/author/1', data=info,follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_delete_author(self):
        self.add_author(self.author_info)

        response = self.app.delete('/author/1', follow_redirects=True)

        self.assertEqual(response.status_code, 201)


    def add_author(self, info):
        return self.app.post('/author',
                             data=info,
                             follow_redirects=True)
if __name__ == '__main__':
    unittest.main()
