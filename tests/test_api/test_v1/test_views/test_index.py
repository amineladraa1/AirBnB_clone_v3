#!/usr/bin/python3
"""Unitest module for flask app"""

from api.v1.app import app
from unittest import TestCase


class TestApp(TestCase):
    """Test Class for app"""

    def setUp(self):
        """setup app"""
        self.app = app.test_client()

    def test_index_status(self):
        """Test index status enpoint"""
        response = self.app.get('http://0.0.0.0:5000/api/v1/status')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "OK"})

    def test_index_status(self):
        """Test index stats enpoint"""
        response = self.app.get('http://0.0.0.0:5000/api/v1/stats')
        print(response)
        self.assertEqual(response.status_code, 200)
