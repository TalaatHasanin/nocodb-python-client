

class Api:
    """
    Represents a NocoDB API instance
    """

    VERSION = "v2"

    def __init__(
            self,
            token: str,
            endpoint_url: str = 'https://app.nocodb.com'
    ):
        self.token = token
