from dataclasses import dataclass

import pytest

from app.domain.common.entities.base.value_object import ValueObject
from app.domain.common.exceptions.base import DomainFieldError


@dataclass(frozen=True, slots=True, repr=False)
class SingleFieldVO(ValueObject):
    value: int


@dataclass(frozen=True, slots=True, repr=False)
class MultiFieldVO(ValueObject):
    value1: int
    value2: str


@dataclass(frozen=True, slots=True, repr=False)
class TypeCaseCheckVO(ValueObject):
    str_val: str
    int_val: int
    float_val: float
    bool_val: bool


def test_post_init():
    with pytest.raises(DomainFieldError):
        ValueObject()


def test_repr():
    vo_1 = SingleFieldVO(value=123)
    assert repr(vo_1) == "SingleFieldVO(123)"
    vo_2 = MultiFieldVO(value1=123, value2="abc")
    assert repr(vo_2) == "MultiFieldVO(value1=123, value2='abc')"


def test_auto_type_cast():
    TypeCaseCheckVO(str_val=321, int_val="123", float_val="1.1", bool_val=True)  # noqa


def test_auto_type_cast_err():
    with pytest.raises(TypeError):
        TypeCaseCheckVO(str_val=321, int_val="123", float_val="1.1", bool_val="True")  # noqa


def test_get_fields():
    vo = MultiFieldVO(value1=123, value2="abc")
    assert vo.get_fields() == {"value1": 123, "value2": "abc"}
