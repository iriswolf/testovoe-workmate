from typing import Any, TypedDict, Unpack

from app.domain.common.entities.value_objects.email import Email
from app.domain.reports.entities.employee.entity import Employee
from app.domain.reports.entities.employee.value_objects import (
    EmployeeDepartment,
    EmployeeHourlyRate,
    EmployeeHoursWorked,
    EmployeeId,
    EmployeeName,
)

DataDictType = dict[str, Any]


class EmployeeArgs(TypedDict):
    id_: int
    name: str
    email: str
    department: str
    hours_worked: int
    hourly_rate: int


class ReportsService:

    def create_employee(self, **kwargs: Unpack[EmployeeArgs]) -> Employee:
        return Employee(
            id_=EmployeeId(kwargs["id_"]),
            email=Email(kwargs["email"]),
            name=EmployeeName(kwargs["name"]),
            department=EmployeeDepartment(kwargs["department"]),
            hours_worked=EmployeeHoursWorked(kwargs["hours_worked"]),
            hourly_rate=EmployeeHourlyRate(kwargs["hourly_rate"]),
        )

    def create_employees(self, rows: list[DataDictType]) -> list[Employee]:
        return [self.create_employee(**row) for row in rows]

    # O(n+m) знаю, плохо, хотел сделать через модели, но решил код не усложнять
    def change_key_names(
        self, data: DataDictType, replacement: str, replaceable: list[str]
    ) -> DataDictType:
        updated = data.copy()
        for old_key in replaceable:
            if old_key in updated:
                updated[replacement] = updated.pop(old_key)
        return updated

    def change_key_names_list(
        self, data: list[DataDictType], replace: dict[str, list[str]]
    ) -> list[DataDictType]:
        result = []
        for data_row in data:
            copied_row = data_row.copy()
            for replacement, replaceable in replace.items():
                copied_row = self.change_key_names(copied_row, replacement, replaceable)
            result.append(copied_row)
        return result
