'''
Test suite for basic views
'''
from django.test import TestCase


class TestIndex(TestCase):
    '''Test case for "/"'''

    def test_get(self):
        '''Test GET /'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_not_allowed(self):
        '''Test method not allowed'''
        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)
