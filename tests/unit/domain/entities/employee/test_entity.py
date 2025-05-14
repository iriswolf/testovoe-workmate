from hypothesis import given
from hypothesis.strategies import integers

from app.domain.common.entities.value_objects.email import Email
from app.domain.reports.entities.employee.entity import Employee
from app.domain.reports.entities.employee.value_objects import (
    EmployeeDepartment,
    EmployeeHourlyRate,
    EmployeeHoursWorked,
    EmployeeId,
    EmployeeName,
)


def test_valid_employee():
    Employee(
        id_=EmployeeId(1),
        email=Email("test@doman.tld"),
        name=EmployeeName("Ivan Ivanov"),
        department=EmployeeDepartment("dep"),
        hours_worked=EmployeeHoursWorked(40),
        hourly_rate=EmployeeHourlyRate(50),
    )


@given(
    hours=integers(min_value=0, max_value=100), hourly_rate=integers(min_value=0, max_value=100)
)
def test_calculate_salary_func(hours: int, hourly_rate: int):
    e = Employee(
        id_=EmployeeId(1),
        email=Email("test@domain.tld"),
        name=EmployeeName("Ivan Ivanov"),
        department=EmployeeDepartment("dep"),
        hours_worked=EmployeeHoursWorked(hours),
        hourly_rate=EmployeeHourlyRate(hourly_rate),
    )

    salary_result = e.calculate_payout()
    assert salary_result == hours * hourly_rate
