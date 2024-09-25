import requests


def _raise_for_status(response):
    if 400 <= response.status_code < 600:
        raise requests.HTTPError(f'{response.reason}: {response.text}', response=response)


class API:
    """
    Represents a NocoDB API instance
    """
    VERSION = 'v2'

    def __init__(self, api_key: str, base_url: str = None):
        """
        Args:
            api_key (str): The NocoDB access token
            base_url (str): The NocoDB URL
        """
        if base_url is None:
            base_url = 'https://app.nocodb.com'

        base_url.rstrip('/')
        if not base_url.endswith('/api'):
            base_url = base_url + '/api'

        self.api_key = api_key
        self.base_url = base_url

    def _headers(self) -> dict[str, str]:
        return {'xc-token': self.api_key}

    def get(self, url: str) -> requests.Response:
        resp = requests.get(self.base_url + url, headers=self._headers())

        _raise_for_status(resp)
        return resp

    def delete(self, url: str) -> requests.Response:
        resp = requests.delete(self.base_url + url, headers=self._headers())

        _raise_for_status(resp)
        return resp

    def post(self, url: str, data: dict) -> requests.Response:
        resp = requests.post(
            self.base_url + url,
            headers=self._headers(),
            json=data,
        )

        _raise_for_status(resp)
        return resp

    def patch(self, url: str, data: dict) -> requests.Response:
        resp = requests.patch(
            self.base_url + url,
            headers=self._headers(),
            json=data,
        )

        _raise_for_status(resp)
        return resp


