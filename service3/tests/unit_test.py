from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_float(self):
        response = self.client.get(url_for('get_float'))
        flo =  response.data.decode('utf-8')
        isfloat = flo[0].isnumeric()
        self.assertTrue(isfloat)
