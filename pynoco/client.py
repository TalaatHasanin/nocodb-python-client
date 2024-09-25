from pynoco.api import API


class Client:

    def __init__(self, api_key: str, base_url: str = None):
        self.api = API(api_key, base_url)
