from enum import Enum


class DialectQuotingEnum(int, Enum):
    """
    Режимы кавычек для CSV
    - NONE: Никогда не использовать кавычки
    - MINIMAL: Кавычки только там, где это необходимо
    - NONNUMERIC: Все нечисловые значения в кавычках
    - ALL: Все значения в кавычках
    """

    NONE = 0
    MINIMAL = 1
    NONNUMERIC = 2
    ALL = 3
