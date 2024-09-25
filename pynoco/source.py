

class Source:
    def __init__(
            self,
            id: str,
            base_id: str,
            type: str,
            inflection_column: str,
            inflection_table: str,
            order: int,
            **kwargs
    ):
        self.id = id
        self.base_id = base_id
        self.type = type
        self.inflection_column = inflection_column
        self.inflection_table = inflection_table
        self.order = order
        self.kwargs = kwargs



