from __future__ import annotations

import app
import models

from typing import TYPE_CHECKING


class User:
    def __init__(self,
                 id_: int = 0,
                 name: str = "",
                 username: str = "",
                 photo: str = "",
                 password: str = ""):
        self.id = id_
        self.name = name
        self.username = username
        self.photo = photo
        self.password = password

    def exists(self) -> bool:
        return self.id != 0
