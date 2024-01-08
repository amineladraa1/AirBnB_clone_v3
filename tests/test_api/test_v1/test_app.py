#!/usr/bin/python3
"""Unitest module for flask app"""

from api.v1.app import app
from unittest import TestCase


class TestApp(TestCase):
    """Test Class for app"""

    def setUp(self):
        """setup app"""
        self.app = app.test_client()

    def test_404_error_handler(self):
        """test_error404"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Not found"})
