'''
Test suite for basic views
'''
import os
import django
# from django.test import TestCase
# from django.test import Client


os.environ.update({"DJANGO_SETTINGS_MODULE": "django_auth_example.settings"})
django.setup()

# class TestIndex(TestCase):
#     '''Test case for "/"'''
#
#     def test_get(self):
#         '''Test GET /'''
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_not_allowed(self):
#         '''Test method not allowed'''
#         response = self.client.post('/')
#         self.assertEqual(response.status_code, 405)
#         client = Client()
#         response = client.get('/')
#         assert response.status_code == 200


def test():
    """this is tests.py"""
    print('hello')
