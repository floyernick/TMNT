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


async def users_signup(self: Controller, params: Dict[str,
                                                      Any]) -> Dict[str, Any]:

    try:
        await validator.validate("users_signup", params)
    except validator.ValidationError:
        raise errors.RequestValidationFailed

    u_query = await self.storage.get_users()
    u_query.add(u_query.equals("username", params["username"]))

    try:
        user = await u_query.fetch_one()
    except errors.StorageException:
        raise errors.InternalError

    if user.exists():
        raise errors.UsernameUsed

    user = models.User(
        name=params["name"],
        username=params["username"],
        password=await passwords.encode(params["password"]),
    )

    try:
        user.id = await self.storage.store_user(user)
    except errors.StorageException:
        raise errors.InternalError

    token = await tokens.create({"id": user.id})

    result = {"token": token, "id": user.id}

    return result


async def users_signin(self: Controller, params: Dict[str,
                                                      Any]) -> Dict[str, Any]:

    try:
        await validator.validate("users_signin", params)
    except validator.ValidationError:
        raise errors.RequestValidationFailed

    u_query = await self.storage.get_users()
    u_query.add(u_query.equals("username", params["username"]))

    try:
        user = await u_query.fetch_one()
    except errors.StorageException:
        raise errors.InternalError

    if not user.exists():
        raise errors.InvalidCredentials

    if user.password != await passwords.encode(params["password"]):
        raise errors.InvalidCredentials

    token = await tokens.create({"id": user.id})

    result = {"token": token, "id": user.id}

    return result


async def users_get(self: Controller, params: Dict[str,
                                                   Any]) -> Dict[str, Any]:

    try:
        await validator.validate("users_get", params)
    except validator.ValidationError:
        raise errors.RequestValidationFailed

    try:
        token = await tokens.parse(params["token"])
    except tokens.ParseError:
        raise errors.InvalidToken

    u_query = await self.storage.get_users()
    u_query.add(u_query.equals("id", token["id"]))

    try:
        current_user = await u_query.fetch_one()
    except errors.StorageException:
        raise errors.InternalError

    result = {
        "id": current_user.id,
        "name": current_user.name,
        "username": current_user.username,
        "photo": current_user.photo
    }

    return result