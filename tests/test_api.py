import unittest
import requests
from requests.exceptions import HTTPError
from pynoco import Api


class TestApi(unittest.TestCase):

    def setUp(self):
        # Set up the API client with a valid API key for testing
        self.api = Api(api_key="test_api_key")

    def test_get_bases(self):
        """
        Test retrieving bases (example endpoint).
        """
        try:
            url = self.api.build_url('meta/bases')
            response = self.api.get(url)
            self.assertIsInstance(response, requests.Response)
        except HTTPError as e:
            self.fail(f"HTTPError occurred: {str(e)}")
