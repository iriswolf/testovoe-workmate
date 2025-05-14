from typing import Any

from app.application.common.ports.formatter import ABCFormatter
from app.application.common.ports.writer import ABCWriter
from app.domain.reports.ports.parser import ABCParser
from app.domain.reports.ports.reader import ABCReader
from app.domain.reports.services.payout_service import PayoutService
from app.domain.reports.services.reports_service import ReportsService

RowsListType = list[dict[str, Any]]


class GetPayoutReportInteractor[T, F]:

    def __init__(
        self,
        reader: ABCReader[T],
        parser: ABCParser[T, RowsListType],
        formatter: ABCFormatter[RowsListType, F],
        writer: ABCWriter[F],
        aliases: dict[str, list[str]],
        payout_service: PayoutService,
        reports_service: ReportsService,
    ) -> None:
        self._reader = reader
        self._writer = writer
        self._parser = parser
        self._aliases = aliases
        self._formatter = formatter
        self._payout_service = payout_service
        self._reports_service = reports_service

    def __call__(self) -> None:
        raw_content = self._reader.read()
        content = self._parser.parse(raw_content)

        with_normal_keys = self._reports_service.change_key_names_list(content, self._aliases)
        employees = self._reports_service.create_employees(with_normal_keys)
        report = self._payout_service.make_payout_report(employees)

        # Да, я сначала перегоняю сущность в сущность,
        # а потом это перегоняю в дикт, хотя мог сразу в дикт пихать в `make_payout_report()`,
        # соответственно трачу попусту процессорное время.
        # Но в данном случае, я сделал это для того,
        # что бы была конкретная типизированная и явно описанная сущность на каждом из этапов
        raw_report = [r.get_fields() for r in report]

        formatted_content = self._formatter.format(raw_report)
        self._writer.write(formatted_content)
