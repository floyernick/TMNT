from __future__ import annotations

import app
import models

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import User


class ChannelRelation:
    def __init__(self,
                 id_: int = 0,
                 user_id: int = 0,
                 channel_id: int = 0,
                 role: int = 0):
        self.id: int = id_
        self.user_id: int = user_id
        self.channel_id: int = channel_id
        self.role: int = role

    def exists(self) -> bool:
        return self.id != 0
