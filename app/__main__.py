import argparse
from collections.abc import Iterable
from pathlib import Path
from typing import TypedDict, Unpack

from app.application.reports.interactors.get_payout_report import (
    GetPayoutReportInteractor,
)
from app.domain.reports.registry import EMPLOYEE_COLUMN_NAME_ALIASES
from app.domain.reports.services.payout_service import PayoutService
from app.domain.reports.services.reports_service import ReportsService
from app.infrastructure.adapters.application.formatters.table_formatter import (
    PayoutTableFormatter,
)
from app.infrastructure.adapters.application.writers.stdout_writer import StdoutWriter
from app.infrastructure.adapters.domain.parsers.csv_parser import CSVParser
from app.infrastructure.adapters.domain.readers.file_reader import FileReader
from app.infrastructure.descriptors.csv_descriptors.dialects.excel_dialect import (
    CSV_EXCEL_DIALECT,
)


class CLIArgs(TypedDict):
    input: str
    report_type: str


def payout_report(**kwargs: Unpack[CLIArgs]) -> None:
    input_arg = kwargs["input"]
    csv_path = Path(input_arg)

    if not csv_path.is_file():
        raise FileNotFoundError(f"Not found file on path: {input_arg!r}")

    reader = FileReader(csv_path)
    parser = CSVParser(CSV_EXCEL_DIALECT)
    formatter = PayoutTableFormatter()
    writer = StdoutWriter()

    GetPayoutReportInteractor(
        reader=reader,
        parser=parser,
        formatter=formatter,
        writer=writer,
        aliases=EMPLOYEE_COLUMN_NAME_ALIASES,
        payout_service=PayoutService(),
        reports_service=ReportsService(),
    )()


def setup_argparse(default_report_type: str, known_report_types: Iterable[str]) -> CLIArgs:
    parser = argparse.ArgumentParser(description="Генерация отчётов по сотрудникам")
    parser.add_argument(
        "-i", "--input", type=Path, required=True, help="Путь к входному CSV-файлу"
    )
    parser.add_argument(
        "-r",
        "--report",
        type=str,
        default=default_report_type,
        choices=known_report_types,
        help="Тип отчёта",
    )
    namespace = parser.parse_args()

    return CLIArgs(input=namespace.input, report_type=namespace.report)


REPORT_MAP = {"payout": payout_report}

if __name__ == "__main__":
    kwargs = setup_argparse(default_report_type="payout", known_report_types=["payout"])
    report_handler = REPORT_MAP.get(kwargs["report_type"])

    if report_handler is None:
        raise ValueError("Report type not exsist")

    report_handler(**kwargs)
