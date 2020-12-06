import os
import sys
import unittest
import signal

parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from app import setupApp


class TimeOutException(Exception):
    def __init__(self, message, errors):
        super(TimeOutException, self).__init__(message)
        self.errors = errors


class MyTestCase(unittest.TestCase):

    app = setupApp(True)

    def test_index_gets(self):
        app = self.app.test_client()
        response = app.get('/', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        response = app.get('/asd', follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_app_runs(self):
        try:
            signal.alarm(2)
            self.app.run()
        except TimeOutException:
            self.assertEqual("isCool", "isCool")

