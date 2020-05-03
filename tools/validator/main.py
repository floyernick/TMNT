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
    },
    "users_signin": {
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
    },
    "users_get": {
        "token": {
            "required": True,
            "type": "string"
        }
    },
    "users_update": {
        "token": {
            "required": True,
            "type": "string"
        },
        "name": {
            "required": False,
            "type": "string",
            "minlength": 1,
            "maxlength": 100
        },
        "username": {
            "required": False,
            "type": "string",
            "minlength": 1,
            "maxlength": 100
        },
        "password": {
            "required": False,
            "type": "string",
            "regex": "[^\s]{8,32}$"
        },
        "photo": {
            "required": False,
            "type": "string",
            "minlength": 1,
            "maxlength": 100
        },
    },
}


async def validate(kind: str, document: Dict[str, Any]) -> None:
    v = cerberus.Validator()
    if not v.validate(document, schemas[kind]):
        raise ValidationError