from dataclasses import dataclass

from app.infrastructure.enums.csv_enums import DialectQuotingEnum
from app.infrastructure.exceptions.descriptors import CSVDialectValidationError


@dataclass(frozen=True, slots=True)
class Dialect:
    r"""
    Value Object, описывающий правила разбора CSV-данных.

    Используется для задания параметров парсинга: символов-разделителей, кавычек, экранирования
    и других особенностей форматирования.

    :param delimiter: Символ-разделитель между полями (по умолчанию: ',')
    :type delimiter: str

    :param quote_char: Символ, используемый для оборачивания значений (по умолчанию: '"')
    :type quote_char: str

    :param escape_char: Символ экранирования или None (по умолчанию: None)
    :type escape_char: Optional[str]

    :param doublequote: Экранировать кавычки через удвоение (по умолчанию: True)
    :type doublequote: bool

    :param skip_initial_space: Пропускать пробел после разделителя (по умолчанию: False)
    :type skip_initial_space: bool

    :param quoting: Режим кавычек
    :type quoting: int

    :raises ValueError
    """

    delimiter: str
    quote_char: str
    escape_char: str | None
    doublequote: bool
    skip_initial_space: bool
    quoting: DialectQuotingEnum

    def __post_init__(self) -> None:
        if len(self.delimiter) != 1:
            raise CSVDialectValidationError("Delimiter must be a single character")

        if len(self.quote_char) != 1:
            raise CSVDialectValidationError("Quotechar must be a single character")

        if self.escape_char is not None and len(self.escape_char) != 1:
            raise CSVDialectValidationError("Escapechar must be a single character or None")

        if not isinstance(self.quoting, DialectQuotingEnum):
            raise CSVDialectValidationError("Quoting must be an instance of Quoting enum")
