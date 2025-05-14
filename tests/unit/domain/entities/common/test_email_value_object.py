import pytest
from hypothesis import given
from hypothesis.strategies import emails

from app.domain.common.entities.validators.email.consts import (
    MAX_EMAIL_DOMAIN_PART_LENGTH,
    MAX_EMAIL_USER_PART_LENGTH,
)
from app.domain.common.entities.value_objects.email import Email
from app.domain.common.exceptions.value_objects import EmailValidationError


@given(emails())
def test_vaild_emails(email: str):
    Email(email)


def test_email_local_zero_length_err():
    email = "@domain.tld"
    with pytest.raises(EmailValidationError):
        Email(email)


def test_email_local_max_length_overflow_err():
    email = f"{'a' * (MAX_EMAIL_USER_PART_LENGTH + 1)}@domain.tld"
    with pytest.raises(EmailValidationError):
        Email(email)


def test_invalid_email_domain_zero_length_err():
    email = "box@.tld"
    with pytest.raises(EmailValidationError):
        Email(email)


def test_invalid_email_domain_max_length_overflow_err():
    email = f"box@{'a' * (MAX_EMAIL_DOMAIN_PART_LENGTH + 1)}.tld"
    with pytest.raises(EmailValidationError):
        Email(email)


def test_invalid_email_full_parted_length_overflow_err():
    email = (
        f"{'a' * (MAX_EMAIL_USER_PART_LENGTH + 1)}@{'a' * (MAX_EMAIL_DOMAIN_PART_LENGTH + 1)}.tld"
    )
    with pytest.raises(EmailValidationError):
        Email(email)
