from dataclasses import dataclass

from app.domain.common.entities.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class PayoutEmployeeReport(ValueObject):
    name: str
    department: str
    hours: int
    rate: int
    payout: int
