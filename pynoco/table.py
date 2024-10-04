from typing import List


class Table:
    def __init__(self,
                 client,
                 table_name: str,
                 columns: List[dict],
                 **kwargs):
        self.client = client
        self.table_name = table_name
        self.columns = columns
        self.kwargs = kwargs