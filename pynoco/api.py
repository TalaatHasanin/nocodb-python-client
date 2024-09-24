from functools import partialmethod
from typing import Optional, Dict, Any

import requests
from requests import exceptions


class Api:
    """
    Represents a NocoDB API instance
    """

    VERSION = 'v2'

    def __init__(
            self,
            api_key: str,
            endpoint_url: str = 'https://app.nocodb.com',
    ):
        self.api_key = api_key
        self.endpoint_url = endpoint_url

    def build_url(self, path: str) -> str:
        """
        Build a complete URL by joining the endpoint with the given path components.
        :param path: The given URL path
        :return: A string of the complete URL
        """
        return f'{self.endpoint_url}/api/{self.VERSION}/{path}'

    def request(
            self,
            method: str,
            url: str,
            params: Optional[Dict[str, Any]] = None,
            timeout: Optional[int] = 10
    ) -> Any:
        """
        Make a request to the NocoDB API with a timeout
        :param params: Additional query parameters to pass to the request
        :param method: HTTP method
        :param url: The url to call
        :param timeout: How long to wait
        """
        requested_params = {**params} if params else {}

        try:
            response = requests.request(method=method,
                                        url=url,
                                        params=requested_params,
                                        timeout=timeout,
                                        headers={'xc-token': self.api_key}
                                        )
            return response

        except exceptions.Timeout:
            raise Exception("Request timed out. Please try again.")

    get = partialmethod(request, 'GET')

