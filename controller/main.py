import storage

from . import users, channels


class Controller:
    def __init__(self, storage_: storage.Storage):
        self.storage: storage.Storage = storage_

    users_signup = users.users_signup
    users_signin = users.users_signin
    users_get = users.users_get
    users_update = users.users_update

    channels_create = channels.channels_create
    channels_update = channels.channels_update


async def init(storage_: storage.Storage) -> Controller:
    controller = Controller(storage_)
    return controller
