# file deepcode ignore C0411: n/a
# file deepcode ignore C0413: n/a
import unittest
import sys

sys.path.append('../')
#  deepcode ignore C0413: stupid issue
from app import setupApp
#  deepcode ignore C0413: stupid issue
from db import db



class FaqTest(unittest.TestCase):

    faq_info = {
        'category': "Test",
        'question': "test",
        'answer': "test",
    }

    category_info = {
        'type': "test2",
    }

    def setUp(self):

        self.app = setupApp(True).test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_faq(self):
        response = self.add_faq(self.faq_info)
        self.assertEqual(response.status_code, 200)


    def test_get_faq(self):
        self.add_faq(self.faq_info)
        response = self.app.get('api/faq/1', follow_redirects=True)
        resp = self.app.get('api/faq/1000', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)

    def test_get_faqs(self):
        self.add_faq(self.faq_info)
        self.add_faq(self.faq_info)
        response = self.app.get('api/faqs', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_put_faq(self):
        self.add_faq(self.faq_info)
        info = {
            'category': "Test2",
            'question': "test2",
            'answer': "test2",
        }
        response = self.app.put('api/faq/1', data=info,follow_redirects=True)
        resp = self.app.put('api/faq/1000', data=info, follow_redirects=True)
        self.add_category(self.category_info)
        info_aux = {
            'category': "test2",
            'question': "test2",
            'answer': "test2",
        }
        resp_cat_exist = self.app.put('api/faq/1', data=info_aux,follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp_cat_exist.status_code, 200)

    def test_delete_faq(self):
        self.add_faq(self.faq_info)

        response = self.app.delete('api/faq/1', follow_redirects=True)
        resp = self.app.delete('api/faq/1000', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp.status_code, 404)


    def add_faq(self, info):
        return self.app.post('api/faq',
                             data=info,
                             follow_redirects=True)

    def add_category(self, info):
        return self.app.post('api/category',
                             data=info,
                             follow_redirects=True)
