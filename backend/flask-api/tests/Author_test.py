# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
#  deepcode ignore C0411: not an issue
import os
import unittest
#  deepcode ignore C0411: not an issue
import sys
parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
#  deepcode ignore C0411: not an issue
from models.author import AuthorModel

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

    def test_model_no_authors_length(self):
        self.assertEqual(0, AuthorModel.num_authors())

    def test_create_author(self):
        response = self.add_author(self.author_info)
        self.assertEqual(response.status_code, 201)

    def test_get_author(self):
        self.add_author(self.author_info)
        response = self.app.get('api/author/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_non_existent_author(self):
        self.add_author(self.author_info)
        response = self.app.get('api/author/59', follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    def test_get_authors(self):
        self.add_author(self.author_info)
        self.add_author(self.author_info)
        response = self.app.get('api/authors', follow_redirects=True)

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
        response = self.app.put('api/author/1', data=info, follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_put_non_existent_author(self):
        self.add_author(self.author_info)
        info = {
            'name': "TestPut",
            'birth_date': date.today().strftime('%Y-%m-%d'),
            'city': "Barcelona",
            'country': "Spain"
        }
        response = self.app.put('api/author/59', data=info, follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    def test_delete_author(self):
        self.add_author(self.author_info)
        response = self.app.delete('api/author/1', follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_delete_non_existent_author(self):
        self.add_author(self.author_info)
        response = self.app.delete('api/author/59', follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    def add_author(self, info):
        return self.app.post('api/author', data=info, follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
