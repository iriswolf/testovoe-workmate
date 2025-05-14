from unittest.mock import MagicMock

import pytest

from app.application.reports.interactors.get_payout_report import (
    GetPayoutReportInteractor,
)
from app.domain.reports.services.payout_service import PayoutService
from app.domain.reports.services.reports_service import ReportsService


class DummyValueObject:
    def __init__(self, data: dict):
        self._data = data

    def get_fields(self):
        return self._data


@pytest.fixture
def reader():
    m = MagicMock()
    m.read.return_value = "raw csv text"
    return m


@pytest.fixture
def parser():
    m = MagicMock()
    m.parse.return_value = [
        {"orig_key": "value1"},
        {"orig_key": "value2"},
    ]
    return m


@pytest.fixture
def reports_service():
    m = MagicMock(spec=ReportsService)
    m.change_key_names_list.return_value = [
        {"name": "Alice"},
        {"name": "Bob"},
    ]

    m.create_employees.return_value = [
        DummyValueObject({"name": "Alice", "payout": 100}),
        DummyValueObject({"name": "Bob", "payout": 200}),
    ]
    return m


@pytest.fixture
def payout_service():
    m = MagicMock(spec=PayoutService)
    m.make_payout_report.return_value = [
        DummyValueObject({"name": "Alice", "payout": 100}),
        DummyValueObject({"name": "Bob", "payout": 200}),
    ]
    return m


@pytest.fixture
def formatter():
    m = MagicMock()
    m.format.return_value = "FORMATTED REPORT"
    return m


@pytest.fixture
def writer():
    return MagicMock()


@pytest.fixture
def aliases():
    return {"name": ["orig_key"]}


def test_get_payout_report_flow(
    reader,
    parser,
    reports_service,
    payout_service,
    formatter,
    writer,
    aliases,
):
    interactor = GetPayoutReportInteractor(
        reader=reader,
        parser=parser,
        formatter=formatter,
        writer=writer,
        aliases=aliases,
        payout_service=payout_service,
        reports_service=reports_service,
    )

    interactor()

    reader.read.assert_called_once()
    parser.parse.assert_called_once_with("raw csv text")
    reports_service.change_key_names_list.assert_called_once_with(
        parser.parse.return_value, aliases
    )

    reports_service.create_employees.assert_called_once_with(
        reports_service.change_key_names_list.return_value
    )

    payout_service.make_payout_report.assert_called_once_with(
        reports_service.create_employees.return_value
    )

    formatter.format.assert_called_once_with(
        [r.get_fields() for r in payout_service.make_payout_report.return_value]
    )

    writer.write.assert_called_once_with("FORMATTED REPORT")
