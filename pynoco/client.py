from pynoco.api import API
from pynoco.base import Bases


class Client:

    def __init__(self, api_key: str, base_url: str = None):
        self.api = API(api_key, base_url)

        self.bases = Bases(self)
