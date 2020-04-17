import storage


class Controller:
    def __init__(self, storage_: storage.Storage):
        self.storage: storage.Storage = storage_


async def init(storage_: storage.Storage) -> Controller:
    controller = Controller(storage_)
    return controller
