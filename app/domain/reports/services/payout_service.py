from app.domain.reports.entities.employee.entity import Employee
from app.domain.reports.entities.report.value_objects import PayoutEmployeeReport

ReportReturnType = list[PayoutEmployeeReport]


class PayoutService:
    def make_payout_report(self, employees: list[Employee]) -> ReportReturnType:
        return [
            PayoutEmployeeReport(
                name=e.name.value,
                department=e.department.value,
                hours=e.hours_worked.value,
                rate=e.hours_worked.value,
                payout=e.calculate_payout(),
            )
            for e in employees
        ]
