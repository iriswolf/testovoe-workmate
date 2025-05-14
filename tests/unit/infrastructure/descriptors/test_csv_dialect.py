import pytest

from app.infrastructure.descriptors.csv_descriptors.dialects.dialect import Dialect
from app.infrastructure.enums.csv_enums import DialectQuotingEnum
from app.infrastructure.exceptions.descriptors import CSVDialectValidationError


def test_csv_dialect_delimeter_exception():
    with pytest.raises(CSVDialectValidationError):
        Dialect(
            delimiter="12323",
            quote_char="1",
            escape_char=None,
            doublequote=False,
            skip_initial_space=False,
            quoting=DialectQuotingEnum.NONE,
        )


def test_csv_dialect_quote_char_exception():
    with pytest.raises(CSVDialectValidationError):
        Dialect(
            delimiter="1",
            quote_char="1s23123",
            escape_char=None,
            doublequote=False,
            skip_initial_space=False,
            quoting=DialectQuotingEnum.NONE,
        )


def test_csv_dialect_escape_char_exception():
    with pytest.raises(CSVDialectValidationError):
        Dialect(
            delimiter="1",
            quote_char="1",
            escape_char="23123213",
            doublequote=False,
            skip_initial_space=False,
            quoting=DialectQuotingEnum.NONE,
        )


def test_csv_dialect_quote_ivalid_type_exception():
    with pytest.raises(CSVDialectValidationError):
        Dialect(
            **dict(  # noqa
                delimiter="1",
                quote_char="1",
                escape_char=None,
                doublequote=False,
                skip_initial_space=False,
                quoting=12323,
            )
        )
