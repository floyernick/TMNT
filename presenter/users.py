from __future__ import annotations
from typing import Any, Dict

from . import utils

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Presenter


async def users_signup(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.users_signup(request_body)
    return response_body


async def users_signin(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.users_signin(request_body)
    return response_body


async def users_get(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.users_get(request_body)
    return response_body


async def users_update(self: Presenter, request: Any) -> Dict[str, Any]:
    request_body = await utils.parse_request_body(request)
    response_body = await self.controller.users_update(request_body)
    return response_body