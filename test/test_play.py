"""Testing for Play Page of bpmninja."""

import unittest
from bpmninja import app


class PlayTests(unittest.TestCase):

    def setUp(self):
        """Setting up client and response for subsequent tests."""
        self.client = app.test_client()
        self.client.testing = True
        self.response = self.client.get('/play')

    def test_play_200_okay(self):
        """Response code play.html in English."""
        assert self.response.status_code == 200
