from typing import Dict, Any
import datetime

import jwt

key = (
    b"\x83\x9f\x99\xd9\xc1\xa0\x9c\xea\xf2\x2b\x49\x51\xba\x22\x1e\x26"
    b"\x23\x18\x39\xa2\xfc\x01\x84\x88\x1d\x70\x84\x7a\x8d\x2a\xca\x7b"
)

algorithm = "HS384"


class ParseError(Exception):
    pass


async def create(data: Dict[str, Any]) -> str:
    payload = {"data": data, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=180)}
    return jwt.encode(payload, key, algorithm=algorithm).decode("utf-8")


async def parse(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, key, algorithms=algorithm)
        data = payload["data"]
    except (jwt.exceptions.InvalidTokenError, KeyError):
        raise ParseError
    return data
