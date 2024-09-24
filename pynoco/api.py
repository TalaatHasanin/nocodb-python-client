import posixpath
from functools import partialmethod
from typing import Optional, Dict, Any

import requests
from requests import Request
from requests.sessions import Session


class Api:
    """
    Represents a NocoDB API instance
    """

    VERSION = 'v2'

    endpoint_url: str
    session: Session

    def __init__(
            self,
            api_key: str,
            endpoint_url: str = 'https://app.nocodb.com',
    ):
        self.session = Session()
        self.api_key = api_key
        self.endpoint_url = endpoint_url + '/api'

    @property
    def api_key(self) -> str:
        """
        NocoDB access token.
        """
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        self.session.headers.update({'xc-token': value})
        self._api_key = value

    def base(self):
        pass

    def build_url(self, *components: str) -> str:
        """
        Build a URL to the NocoDB API endpoint with the given URL components,
        including the API version number.
        """
        return posixpath.join(self.endpoint_url, self.VERSION, *components)

    def request(
            self,
            method: str,
            url: str,
            params: Optional[Dict[str, Any]] = None,
            timeout: Optional[int] = 10
    ) -> Any:
        """
        Make a request to the NocoDB API using the session with a timeout.
        :param params: Additional query parameters to pass to the request
        :param method: HTTP method
        :param url: The url to call
        :param timeout: How long to wait
        """
        requested_params = {**params} if params else {}

        request = self.session.prepare_request(
            Request(
                method=method,
                url=url,
                params=requested_params
            )
        )

        response = self.session.send(request, timeout=timeout)

        return self.handle_response(response)

    get = partialmethod(request, 'GET')

    def handle_response(self, response: requests.Response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:

            try:
                error_dict = response.json()
            except ValueError:
                pass
            else:
                if "error" in error_dict:
                    exc.args = (*exc.args, repr(error_dict["error"]))
            raise exc

        if not response.text:
            return None

        return response.json()
