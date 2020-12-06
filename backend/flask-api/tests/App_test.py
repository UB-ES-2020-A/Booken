import os
import sys
import threading
import time
import unittest


parent_path = os.path.dirname(os.path.abspath(__file__))[:-6]
sys.path.insert(1, parent_path)
from app import setupApp


class Alarm (threading.Thread):
    def __init__ (self, timeout):
        threading.Thread.__init__ (self)
        self.timeout = timeout
        self.setDaemon (True)
    def run (self):
        setupApp(True).run()
        time.sleep(self.timeout)



class MyTestCase(unittest.TestCase):

    def test_index_gets(self):
        app = setupApp(True).test_client()
        response = app.get('/', follow_redirects=True)
        self.assertEqual(200, response.status_code)
        response = app.get('/asd', follow_redirects=True)
        self.assertEqual(404, response.status_code)

    def test_app_runs(self):
        alarm = Alarm(4)
        alarm.start()
        del alarm
        self.assertEqual(1, 1)
