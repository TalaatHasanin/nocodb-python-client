from pynoco.source import Source


class Base:
    """
    NocoDB base
    """
    def __init__(
            self,
            client,
            id: str,
            sources: list[dict] = None,
            title: str = None,
            description: str = None,
            created_at: str = None,
            status: str = None,
            **kwargs
    ):
        self.client = client
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.status = status
        self.kwargs = kwargs

        self.sources = []
        if sources is not None:
            for source in sources:
                src = Source(**source)
                self.sources.append(src)


class Bases:
    def __init__(self, client):
        self.api = client.api
        self.client = client

    def get(self, base_id: str):
        item = self.api.get(f'/meta/bases/{base_id}').json()
        return Base(self.client, **item)

