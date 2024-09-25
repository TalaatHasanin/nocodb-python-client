from typing import Union, Any

from pydantic import BaseModel


class SourceConfig(BaseModel):

    id: str
    base_id: str
    type: str
    inflection_column: str
    inflection_table: str
    alias: Union[str, None] = None
    integration_title: Union[str, None] = None
    fk_integration_id: Union[str, None] = None
    config: Any
    enabled: Union[str, bool, None] = None
    external: bool = False


class Source(SourceConfig):
    pass


