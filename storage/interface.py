from __future__ import annotations
import abc
from typing import Any, List

import models


class Storage(abc.ABC):
    @abc.abstractmethod
    async def commit(self) -> None:
        pass

    @abc.abstractmethod
    async def rollback(self) -> None:
        pass

    @abc.abstractmethod
    async def transaction(self) -> Storage:
        pass

    @abc.abstractmethod
    async def store_user(self, user: models.User) -> int:
        pass

    @abc.abstractmethod
    async def update_user(self, user: models.User) -> None:
        pass

    @abc.abstractmethod
    async def delete_user(self, user: models.User) -> None:
        pass

    @abc.abstractmethod
    async def get_users(self) -> UsersListQuery:
        pass


class QueryBuilder(abc.ABC):
    @abc.abstractmethod
    def equals(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def not_equals(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def greater(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def greater_or_equals(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def less(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def less_or_equals(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def like(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def contains(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def and_(self, *conditions) -> str:
        pass

    @abc.abstractmethod
    def or_(self, *conditions) -> str:
        pass

    @abc.abstractmethod
    def add(self, condition: str) -> None:
        pass

    @abc.abstractmethod
    def paginate(self, offset: int, limit: int) -> None:
        pass

    @abc.abstractmethod
    def order(self, field: str, value: str) -> None:
        pass

    @abc.abstractmethod
    async def count(self) -> int:
        pass

    @abc.abstractmethod
    async def fetch(self) -> List[Any]:
        pass

    @abc.abstractclassmethod
    async def fetch_one(self) -> Any:
        pass


class UsersListQuery(abc.ABC):
    @abc.abstractmethod
    def equals(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def not_equals(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def like(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def contains(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def in_(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def not_in_(self, field: str, value: Any) -> str:
        pass

    @abc.abstractmethod
    def and_(self, *conditions) -> str:
        pass

    @abc.abstractmethod
    def or_(self, *conditions) -> str:
        pass

    @abc.abstractmethod
    def add(self, condition: str) -> None:
        pass

    @abc.abstractmethod
    def paginate(self, offset: int, limit: int) -> None:
        pass

    @abc.abstractmethod
    def order(self, field: str, value: str) -> None:
        pass

    @abc.abstractmethod
    async def count(self) -> int:
        pass

    @abc.abstractmethod
    async def fetch(self) -> List[models.User]:
        pass

    @abc.abstractmethod
    async def fetch_one(self) -> models.User:
        pass
