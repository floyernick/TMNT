import hashlib

salt = "8A1RpsWB"


async def encode(password: str) -> str:
    m = hashlib.md5()
    m.update(salt.encode("utf-8"))
    m.update(password.encode("utf-8"))
    return m.hexdigest()
