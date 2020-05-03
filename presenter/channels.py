from __future__ import annotations
from typing import Any, Dict

from . import utils

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Presenter


async def channels_create(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.channels_create(request_body)
    return response_body