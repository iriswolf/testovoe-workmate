from typing import Final

from app.infrastructure.descriptors.csv_descriptors.dialects.dialect import Dialect
from app.infrastructure.enums.csv_enums import DialectQuotingEnum

CSV_EXCEL_DIALECT: Final[Dialect] = Dialect(
    delimiter=",",
    quote_char='"',
    escape_char=None,
    doublequote=True,
    skip_initial_space=False,
    quoting=DialectQuotingEnum.MINIMAL,
)
