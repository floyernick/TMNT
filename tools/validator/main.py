from typing import Dict, Any

import cerberus


class ValidationError(Exception):
    pass


schemas = {
    "users_signup": {
        "name": {
            "required": True,
            "type": "string",
            "minlength": 1,
            "maxlength": 100
        },
        "username": {
            "required": True,
            "type": "string",
            "minlength": 1,
            "maxlength": 100
        },
        "password": {
            "required": True,
            "type": "string",
            "regex": "[^\s]{8,32}$"
        },
    }
}


async def validate(kind: str, document: Dict[str, Any]) -> None:
    v = cerberus.Validator()
    if not v.validate(document, schemas[kind]):
        raise ValidationError