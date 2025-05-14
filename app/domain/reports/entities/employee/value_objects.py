from dataclasses import dataclass

from app.domain.common.entities.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class EmployeeId(ValueObject):
    value: int


@dataclass(frozen=True, repr=False)
class EmployeeName(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class EmployeeDepartment(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class EmployeeHoursWorked(ValueObject):
    value: int


@dataclass(frozen=True, repr=False)
class EmployeeHourlyRate(ValueObject):
    value: int
