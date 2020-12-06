import os
import sys
import unittest


parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from app import setupApp


class MyTestCase(unittest.TestCase):

    def test_index_gets(self):
        app = setupApp(True).test_client()
        response = app.get('/', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        response = app.get('/asd', follow_redirects=True)
        self.assertEqual(404, response.status_code)
