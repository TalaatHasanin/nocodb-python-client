import unittest
from pynoco import Api


class TestApi(unittest.TestCase):

    def test_api_request(self):
        """
        Test api request method
        """
        self.api = Api('test_token', 'http://localhost:8080')
        url = self.api.build_url('meta/bases')
        response = self.api.get(url)
        self.assertIsNotNone(response)

