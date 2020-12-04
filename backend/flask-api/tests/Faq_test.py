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

        self.assertEqual(response.status_code, 200)

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
        self.assertEqual(response.status_code, 200)

    def test_delete_faq(self):
        self.add_faq(self.faq_info)

        response = self.app.delete('api/faq/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)


    def add_faq(self, info):
        return self.app.post('api/faq',
                             data=info,
                             follow_redirects=True)
if __name__ == '__main__':
    unittest.main()
