from __future__ import annotations

import app
import models

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User


class Reply:
    def __init__(self,
                 id_: int = 0,
                 creator_id: int = 0,
                 post_id: int = 0,
                 text: str = "",
                 photo: str = "",
                 deleted: bool = False):
        self.id: int = id_
        self.creator_id: int = creator_id
        self.post_id: int = post_id
        self.text: str = text
        self.photo: str = photo
        self.deleted: bool = deleted

    def exists(self) -> bool:
        return self.id != 0

    def created_by(self, user: User) -> bool:
        return self.creator_id == user.id
