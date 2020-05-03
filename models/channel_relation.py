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
        self.id = id_
        self.user_id = user_id
        self.channel_id = channel_id
        self.role = role

    def exists(self) -> bool:
        return self.id != 0
