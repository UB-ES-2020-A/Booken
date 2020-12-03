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



class CategoryTest(unittest.TestCase):

    category_info = {
        'type': "Test",
    }

    def setUp(self):

        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_category(self):
        response = self.add_category(self.category_info)
        self.assertEqual(response.status_code, 200)


    def test_get_category(self):
        self.add_category(self.category_info)
        response = self.app.get('/category/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_get_categories(self):
        self.add_category(self.category_info)
        self.add_category(self.category_info)
        response = self.app.get('/categories', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def add_category(self, info):
        return self.app.post('/category',
                             data=info,
                             follow_redirects=True)
if __name__ == '__main__':
    unittest.main()
