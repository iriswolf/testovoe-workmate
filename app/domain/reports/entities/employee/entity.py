from dataclasses import dataclass

from app.domain.common.entities.base.entity import Entity
from app.domain.common.entities.value_objects.email import Email
from app.domain.reports.entities.employee.value_objects import (
    EmployeeDepartment,
    EmployeeHourlyRate,
    EmployeeHoursWorked,
    EmployeeId,
    EmployeeName,
)


@dataclass(eq=False, kw_only=True)
class Employee(Entity[EmployeeId]):
    # rich
    email: Email
    name: EmployeeName
    department: EmployeeDepartment
    hours_worked: EmployeeHoursWorked
    hourly_rate: EmployeeHourlyRate

    def calculate_payout(self) -> int:
        return self.hours_worked.value * self.hourly_rate.value
