from pynoco.client import Client


class Base:
    """
    NocoDB base
    """
    def __init__(
            self,
            client: Client,
            base_id: str,
            sources: dict = None,
            title: str = None,
            description: str = None,
            created_at: str = None,
            status: str = None
    ):
        pass
