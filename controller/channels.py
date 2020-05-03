from __future__ import annotations
from typing import Dict, Any

import models
import app
import app.errors as errors
import tools.tokens as tokens
import tools.uuid as uuid
import tools.passwords as passwords
import tools.validator as validator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Controller


async def channels_create(self: Controller,
                          params: Dict[str, Any]) -> Dict[str, Any]:

    try:
        await validator.validate("channels_create", params)
    except validator.ValidationError:
        raise errors.RequestValidationFailed

    try:
        token = await tokens.parse(params["token"])
    except tokens.ParseError:
        raise errors.InvalidToken

    cu_query = await self.storage.get_users()
    cu_query.add(cu_query.equals("id", token["id"]))

    try:
        current_user = await cu_query.fetch_one()
    except errors.StorageException:
        raise errors.InternalError

    channel = models.Channel(creator_id=current_user.id, name=params["name"])

    if "photo" in params:
        channel.photo = params["photo"]

    try:
        channel.id = await self.storage.store_channel(channel)
    except errors.StorageException:
        raise errors.InternalError

    result = {"id": channel.id}

    return result
