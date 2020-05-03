from __future__ import annotations

import app
import models

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User


class Post:
    def __init__(self,
                 id_: int = 0,
                 creator_id: int = 0,
                 channel_id: int = 0,
                 name: str = "",
                 text: str = "",
                 photo: str = ""):
        self.id = id_
        self.creator_id = creator_id
        self.channel_id = channel_id
        self.name = name
        self.text = text
        self.photo = photo

    def exists(self) -> bool:
        return self.id != 0

    def created_by(self, user: User) -> bool:
        return self.creator_id == user.id
