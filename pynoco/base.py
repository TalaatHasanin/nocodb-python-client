from typing import List, Union

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
            type: str = None,
            **kwargs
    ):
        self.api = client.api
        self.client = client
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.status = status
        self.type = type
        self.kwargs = kwargs

        self.sources = []

        for source in sources:
            src = Source(**source)
            self.sources.append(src)

    def info(self):
        data = self.api.get(f'/meta/bases/{self.id}/info')
        return data.json()

    def update(
            self,
            title: str,
            order: int,
            color: str,
            meta=None,
            linked_db_project_ids=None,
            status=None
    ):
        payload = {
            'title': title,
            'order': order,
            'color': color,
            'meta': meta,
            'status': status
        }

        if self.type == 'documentation':
            payload.update({'linked_db_project_ids': linked_db_project_ids})

        self.api.patch(
            f'/meta/bases/{self.id}',
            data=payload
        )

    def add_source(self, source: Union[Source, dict]):
        if isinstance(source, Source):
            self.api.post(
                f'/meta/bases/{self.id}/sources',
                data=source.__dict__
            )
            self.sources.append(source)
        else:
            self.api.post(
                f'/meta/bases/{self.id}/sources',
                data=source
            )
            self.sources.append(Source(**source))

    def delete_source(self, source: Union[str, Source]):
        if len(self.sources) > 1:
            if isinstance(source, str):
                self.api.delete(f'/meta/bases/{self.id}/sources/{source}')
            elif isinstance(source, Source):
                self.api.delete(f'/meta/bases/{self.id}/sources/{source.id}')
            else:
                raise ValueError(f'source must be either a string of source id or a Source object')
        else:
            raise Exception(f'There are no sources connected to {self.title}')


class Bases:
    def __init__(self, client):
        self.api = client.api
        self.client = client

    def get(self, base_id: str) -> Base:
        item = self.api.get(f'/meta/bases/{base_id}').json()
        return Base(self.client, **item)

    def list(self) -> List[Base]:
        data = self.api.get(f'/meta/bases').json()
        bases_list = []
        for base in data['list']:
            bases_list.append(Base(self.client, **base))
        return bases_list

    def create(
            self,
            base_name: str,
            sources=None,
            type: str = 'database',
            **kwargs
    ) -> Base:
        sources_list = []
        if sources:
            if sources is List[Source]:
                for src in sources:
                    source = src.__dict__
                    source = source.update(source.pop('kwargs'))
                    sources_list.append(source)
            else:
                sources_list = sources

        base = self.api.post(
            f'/meta/bases',
            data={
                'title': base_name,
                'sources': sources_list,
                'type': type,
                **kwargs
            }
        ).json()

        return self.get(base['id'])

    def drop(self, base_id: str) -> None:
        self.api.delete(f'/meta/bases/{base_id}')
