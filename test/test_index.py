"""Testing for Landing Page of bpmninja."""

import unittest
from bpmninja import app


class IndexTests(unittest.TestCase):

    def setUp(self):
        """Setting up client and response for subsequent tests."""
        self.client = app.test_client()
        self.client.testing = True
        self.response = self.client.get('/')

    def test_index_200_okay(self):
        """Response code index.html in English."""
        assert self.response.status_code == 200
