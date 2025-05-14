from abc import ABC
from dataclasses import asdict, dataclass, fields
from typing import Any, get_type_hints

from app.domain.common.exceptions.base import DomainFieldError


@dataclass(frozen=True, repr=False)
class ValueObject(ABC):
    """
    Базовый класс для value objects

    .. note::
        - Автоматически делает тайп каст str, int, float друг в друга, в зависимости от тайп хинта
        - Равенство и хеш вычисляются на основе всех полей.
        - Подклассы должны указывать ``repr=False``, чтобы использовать кастомный ``__repr__``.
        - Для простых случаев можно использовать ``NewType`` из ``typing`` вместо наследования.
    """

    def __post_init__(self) -> None:
        if not fields(self):
            raise DomainFieldError(f"{type(self).__name__} must contain at least one field")

        type_hints = get_type_hints(self)

        for field_name, field_type in type_hints.items():
            current_value = getattr(self, field_name)

            if isinstance(current_value, field_type):
                return

            if field_type not in [str, int, float]:
                raise TypeError(
                    f"ValueObject - {self.__class__.__name__!r} initialization error: "
                    f"field {field_name!r} must be of type {field_type.__name__}, "
                    f"but got {type(current_value).__name__} instead."
                )
            object.__setattr__(self, field_name, field_type(current_value))

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._repr_value()})"

    def _repr_value(self) -> str:
        all_fields = fields(self)
        if len(all_fields) == 1:
            return f"{getattr(self, all_fields[0].name)!r}"
        return ", ".join(f"{f.name}={getattr(self, f.name)!r}" for f in all_fields)

    def get_fields(self) -> dict[str, Any]:
        return asdict(self)
