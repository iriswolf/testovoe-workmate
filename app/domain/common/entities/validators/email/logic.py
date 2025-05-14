from app.domain.common.entities.validators.email.consts import (
    EMAIL_REGEX_RFC5321,
    MAX_EMAIL_DOMAIN_PART_LENGTH,
    MAX_EMAIL_LENGTH,
    MAX_EMAIL_USER_PART_LENGTH,
)
from app.domain.common.exceptions.value_objects import EmailValidationError


def _validate_email_user_part_length(email_local_part: str) -> None:
    """:raises EmailValidationError:"""
    if len(email_local_part) <= MAX_EMAIL_USER_PART_LENGTH:
        return

    raise EmailValidationError(
        f"User part of email must not exceed {MAX_EMAIL_USER_PART_LENGTH} characters"
    )


def _validate_email_domain_part_length(email_domain_part: str) -> None:
    """:raises EmailValidationError:"""
    if len(email_domain_part) <= MAX_EMAIL_DOMAIN_PART_LENGTH:
        return

    raise EmailValidationError(
        f"Domain part of email must not exceed {MAX_EMAIL_DOMAIN_PART_LENGTH} characters"
    )


def _validate_email_full_length(email: str) -> None:
    """:raises EmailValidationError:"""
    if len(email) <= MAX_EMAIL_LENGTH:
        return
    raise EmailValidationError(f"Email address must not exceed {MAX_EMAIL_LENGTH} characters")


def validate_email_length(email: str) -> None:
    """:raises EmailValidationError:"""
    # Мог перенести валидацию длинны и формата в одну регулярку,
    # но тогда мы теряем более подробные ошибки,
    # будем знать только что email неправильный, но без конкретики
    local_part, _, domain_part = email.rpartition("@")

    _validate_email_full_length(email)
    _validate_email_user_part_length(local_part)
    _validate_email_domain_part_length(domain_part)


def validate_email_format(email: str) -> None:
    """:raises EmailValidationError:"""
    if EMAIL_REGEX_RFC5321.match(email):
        return
    raise EmailValidationError("Invalid email format")
