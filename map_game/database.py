class DataBase:
    def __init__(self):
        self.FILENAME = 'map_base.data'

    def save(self, data: dict):
        packed_data = self._pack(data)

    def load(self):
        ...

    def _pack(self, data: dict):
        ...


def create():
    return DataBase()