"""Domain-specific exceptions."""


class DomainException(Exception):
    """Base exception for domain errors."""

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundException(DomainException):
    """Raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class UnauthorizedException(DomainException):
    """Raised when user is not authorized."""

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, status_code=401)


class ForbiddenException(DomainException):
    """Raised when user lacks permission."""

    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, status_code=403)


class ConflictException(DomainException):
    """Raised when there's a resource conflict."""

    def __init__(self, message: str = "Resource conflict"):
        super().__init__(message, status_code=409)


class ValidationException(DomainException):
    """Raised when validation fails."""

    def __init__(self, message: str = "Validation error"):
        super().__init__(message, status_code=422)
