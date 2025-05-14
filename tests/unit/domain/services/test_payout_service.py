from app.domain.common.entities.value_objects.email import Email
from app.domain.reports.entities.employee.entity import Employee
from app.domain.reports.entities.employee.value_objects import (
    EmployeeDepartment,
    EmployeeHourlyRate,
    EmployeeHoursWorked,
    EmployeeId,
    EmployeeName,
)
from app.domain.reports.entities.report.value_objects import PayoutEmployeeReport
from app.domain.reports.services.payout_service import PayoutService

REPORT_INPUT = [
    Employee(
        id_=EmployeeId(1),
        email=Email("test@test.tld"),
        name=EmployeeName("test"),
        department=EmployeeDepartment("test"),
        hours_worked=EmployeeHoursWorked(10),
        hourly_rate=EmployeeHourlyRate(10),
    )
]

REPORT_RESULT = [
    PayoutEmployeeReport(name="test", department="test", hours=10, rate=10, payout=100)
]


def test_payout_report():
    service = PayoutService()
    result = service.make_payout_report(REPORT_INPUT)
    assert result == REPORT_RESULT
