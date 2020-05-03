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
        self.id: int = id_
        self.name: str = name
        self.username: str = username
        self.photo: str = photo
        self.password: str = password

    def exists(self) -> bool:
        return self.id != 0
