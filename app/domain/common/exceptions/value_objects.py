from app.domain.common.exceptions.base import DomainFieldError


class EmailValidationError(DomainFieldError):
    """По сути более локализованый вариант ``DomainFieldError``"""
