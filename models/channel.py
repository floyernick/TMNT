from __future__ import annotations
from typing import Optional

import app
import models

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User


class Channel:
    def __init__(self,
                 id_: int = 0,
                 creator_id: int = 0,
                 name: str = "",
                 photo: str = ""):
        self.id: int = id_
        self.creator_id: int = creator_id
        self.name: str = name
        self.photo: str = photo
        self.creator: Optional[User] = None

    def exists(self) -> bool:
        return self.id != 0

    def created_by(self, user: User) -> bool:
        return self.creator_id == user.id
