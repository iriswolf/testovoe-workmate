import pytest

from app.domain.reports.services.reports_service import ReportsService

RAW_EMPLOYEES = [
    {
        "id_": 1,
        "name": "foo",
        "email": "foo@bar.tld",
        "department": "test",
        "hours_worked": 10,
        "hourly_rate": 10,
    },
    {
        "id_": 2,
        "name": "bar",
        "email": "foo@bar.tld",
        "department": "test",
        "hours_worked": 10,
        "hourly_rate": 10,
    },
]

ALIASES_MAP = {"id": ["id_"], "hours": ["hours_worked"]}


@pytest.fixture
def service():
    return ReportsService()


def test_create_employees(service: ReportsService):
    service.create_employees(RAW_EMPLOYEES)


def test_change_key_names_list(service: ReportsService):
    result = service.change_key_names_list(RAW_EMPLOYEES, ALIASES_MAP)

    for row in RAW_EMPLOYEES:
        assert "id" not in row
        assert "hours" not in row

    for row in result:
        assert "id" in row
        assert "hours" in row
