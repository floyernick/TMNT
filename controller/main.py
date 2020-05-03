import storage

from . import users


class Controller:
    def __init__(self, storage_: storage.Storage):
        self.storage: storage.Storage = storage_

    users_signup = users.users_signup


async def init(storage_: storage.Storage) -> Controller:
    controller = Controller(storage_)
    return controller
