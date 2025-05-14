from dataclasses import dataclass

from app.domain.common.entities.base.value_object import ValueObject
from app.domain.common.entities.validators.email.logic import (
    validate_email_format,
    validate_email_length,
)


@dataclass(frozen=True, repr=False)
class Email(ValueObject):
    """raises EmailValidationError"""

    value: str

    def __post_init__(self) -> None:
        """:raises EmailValidationError:"""
        super().__post_init__()

        validate_email_length(self.value)
        validate_email_format(self.value)
