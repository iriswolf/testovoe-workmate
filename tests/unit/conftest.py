import pytest

from app.infrastructure.descriptors.csv_descriptors.dialects import (
    CSV_EXCEL_DIALECT,
    Dialect,
)


@pytest.fixture
def excel_dialect() -> Dialect:
    return CSV_EXCEL_DIALECT
