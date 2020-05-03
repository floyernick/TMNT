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


async def channels_update(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.channels_update(request_body)
    return response_body


async def channels_delete(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.channels_delete(request_body)
    return response_body


async def channels_get(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.channels_get(request_body)
    return response_body