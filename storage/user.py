from __future__ import annotations
from typing import List, Any, Optional

import models
import app.errors as errors
import tools.logger as logger
from . import interface

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Storage


class UsersListQuery(interface.UsersListQuery):
    def __init__(self, storage: Storage):
        self.storage = storage
        self.conditions: List[str] = []
        self.params: List[Any] = []
        self.offset: Optional[int] = None
        self.limit: Optional[int] = None
        self.order_conditions: List[str] = []

    def equals(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} = ${len(self.params)}"

    def not_equals(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} != ${len(self.params)}"

    def contains(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"${len(self.params)} = ANY({field})"

    def like(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} ILIKE '%' || ${len(self.params)} || '%'"

    def in_(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} = ANY(${len(self.params)})"

    def not_in_(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} != ANY(${len(self.params)})"

    def and_(self, *conditions) -> str:
        result = "("
        for i in range(len(conditions)):
            if i != 0:
                result += " AND "
            result += conditions[i]
        result += ")"
        return result

    def or_(self, *conditions) -> str:
        result = "("
        for i in range(len(conditions)):
            if i != 0:
                result += " OR "
            result += conditions[i]
        result += ")"
        return result

    def add(self, condition: str) -> None:
        self.conditions.append(condition)

    def paginate(self, offset: int, limit: int) -> None:
        self.offset = offset
        self.limit = limit

    def order(self, field: str, value: str) -> None:
        self.order_conditions.append(f"{field} {value}")

    def __format_query(self, query: str, count_only: bool = False) -> str:
        if len(self.conditions) > 0:
            query += " WHERE "
            for i in range(len(self.conditions)):
                if i != 0:
                    query += " AND "
                query += self.conditions[i]
        if not count_only:
            if len(self.order_conditions) > 0:
                query += f" ORDER BY "
                for i in range(len(self.order_conditions)):
                    if i != 0:
                        query += ", "
                    query += self.order_conditions[i]
            if self.offset is not None:
                query += f" OFFSET {self.offset}"
            if self.limit is not None:
                query += f" LIMIT {self.limit}"
        return query

    async def count(self) -> int:

        query = "SELECT COUNT(id) FROM users"

        query = self.__format_query(query, True)

        number = 0

        try:
            result = await self.storage.performer().fetchrow(
                query, *self.params)
        except Exception as e:
            await logger.warning(e)
            raise errors.StorageException

        if result is None:
            return number

        number = result["count"]

        return number

    async def fetch(self) -> List[models.User]:

        query = ("SELECT id, name, username, photo, password FROM users")

        query = self.__format_query(query)

        users = []

        try:
            results = await self.storage.performer().fetch(query, *self.params)
        except Exception as e:
            await logger.warning(e)
            raise errors.StorageException

        if results is None:
            return users

        for result in results:
            user = models.User()
            user.id = result["id"]
            user.name = result["name"]
            user.username = result["username"]
            user.photo = result["photo"]
            user.password = result["password"]
            users.append(user)

        return users

    async def fetch_one(self) -> models.User:

        query = ("SELECT id, name, username, photo, password FROM users")

        query = self.__format_query(query)

        user = models.User()

        try:
            result = await self.storage.performer().fetchrow(
                query, *self.params)
        except Exception as e:
            await logger.warning(e)
            raise errors.StorageException

        if result is None:
            return user

        user.id = result["id"]
        user.name = result["name"]
        user.username = result["username"]
        user.photo = result["photo"]
        user.password = result["password"]

        return user


async def store_user(self: Storage, user: models.User) -> int:

    query = ("INSERT INTO users(name, username, photo, password) "
             "VALUES ($1, $2, $3, $4) RETURNING id")

    try:
        result = await self.performer().fetchrow(query, user.name,
                                                 user.username, user.photo,
                                                 user.password)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException

    id_ = result["id"]

    return id_


async def update_user(self: Storage, user: models.User) -> None:

    query = (
        "UPDATE users SET name = $2, username = $3, photo = $4, password = $5 WHERE id = $1"
    )

    try:
        await self.performer().fetchrow(query, user.id, user.name,
                                        user.username, user.photo,
                                        user.password)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def delete_user(self: Storage, user: models.User) -> None:

    query = "DELETE FROM users WHERE id = $1"

    try:
        await self.performer().execute(query, user.id)
    except Exception as e:
        await logger.warning(e)
        raise errors.StorageException


async def get_users(self: Storage) -> UsersListQuery:
    return UsersListQuery(self)
