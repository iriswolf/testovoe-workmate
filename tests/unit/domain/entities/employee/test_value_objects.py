from app.domain.reports.entities.employee.value_objects import (
    EmployeeDepartment,
    EmployeeHourlyRate,
    EmployeeHoursWorked,
    EmployeeId,
    EmployeeName,
)


# ===== EmployeeId =====
def test_valid_employee_id():
    EmployeeId(123)


# ===== EmployeeName =====
def test_valid_employee_name():
    EmployeeName("Some Name")


# ===== EmployeeHourlyRate =====
def test_valid_employee_hourly_rate():
    EmployeeHourlyRate(55)


# ===== EmployeeDepartment =====
def test_valid_employee_departament():
    EmployeeDepartment("Departament")


# ===== EmployeeHoursWorked =====
def test_valid_employee_hours_worked():
    EmployeeHoursWorked(40)
