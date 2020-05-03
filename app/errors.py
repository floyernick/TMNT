class PresenterException(Exception):
    description = ""


class InvalidRequest(PresenterException):
    description = "invalid request"


class DomainException(Exception):
    description = ""


class InvalidParams(DomainException):
    description = "invalid params"


class InternalError(DomainException):
    description = "internal error"


class RequestValidationFailed(DomainException):
    description = "request validation failed"


class InvalidToken(DomainException):
    description = "invalid token"


class ActionNotAllowed(DomainException):
    description = "action not allowed"


class UsernameUsed(DomainException):
    description = "username used"


class InvalidCredentials(DomainException):
    description = "invalid credentials"


class StorageException(Exception):
    description = ""
