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
    input_files: list[Path]
    report_type: str


def payout_report(**kwargs: Unpack[CLIArgs]) -> None:
    input_files = kwargs["input_files"]

    parser = CSVParser(CSV_EXCEL_DIALECT)
    formatter = PayoutTableFormatter()
    writer = StdoutWriter()

    for file_path in input_files:
        if not file_path.is_file():
            raise FileNotFoundError(f"Not found file on path: {file_path!r}")

        GetPayoutReportInteractor(
            reader=FileReader(file_path),
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
        "-i", "--input", nargs="+", type=Path, required=True, help="Путь к входному CSV-файлу"
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

    return CLIArgs(input_files=namespace.input, report_type=namespace.report)


REPORT_MAP = {"payout": payout_report}

if __name__ == "__main__":
    kwargs = setup_argparse(default_report_type="payout", known_report_types=["payout"])
    report_handler = REPORT_MAP.get(kwargs["report_type"])

    if report_handler is None:
        raise ValueError("Report type not exsist")
    report_handler(**kwargs)
