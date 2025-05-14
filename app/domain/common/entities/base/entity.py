from abc import ABC
from dataclasses import dataclass
from typing import Any

from app.domain.common.entities.base.value_object import ValueObject
from app.domain.common.exceptions.base import DomainError


@dataclass(eq=False)
class Entity[T: ValueObject](ABC):
    """
    Базовый класс domain entity

    :param id_: Идентификатор сущности (ValueObject), неизменяемый

    .. note::
        - Сущности сравниваются **только** по идентификатору ``id_``
        - Подклассы **обязаны** указывать ``eq=False`` в декораторе ``@dataclass``
          для правильной логики сравнения
        - Рекомендуется указывать использовать ``kw_only=True`` в подклассах
    """

    id_: T

    def __setattr__(self, name: str, value: Any) -> None:
        """Запрещаем изменение id сущности"""
        if name == "id_" and getattr(self, "id_", None) is not None:
            raise DomainError("Changing entity id is not permitted.")
        super().__setattr__(name, value)

    def __eq__(self, other: Any) -> bool:
        """Сущности считаются одиаковыми, если имеют один айди"""
        return isinstance(other, type(self)) and other.id_ == self.id_

    def __hash__(self) -> int:
        """Генерация хэша по уникальному айди для хэшмапов (dict/set)"""
        return hash(self.id_)
