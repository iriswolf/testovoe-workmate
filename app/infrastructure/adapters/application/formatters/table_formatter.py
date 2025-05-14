from collections import defaultdict
from typing import Any

from app.application.common.ports.formatter import ABCFormatter

TableContentType = list[dict[str, Any]]
PayoutContentType = TableContentType


class TableFormatter(ABCFormatter[TableContentType, str]):
    def format(self, content: TableContentType) -> str:
        if not content:
            return ""

        fields = list(content[0].keys())
        col_widths = {field: len(str(field)) for field in fields}
        for row in content:
            for field in fields:
                value = str(row.get(field, ""))
                col_widths[field] = max(col_widths[field], len(value))

        row_fmt = " | ".join(f"{{:{col_widths[field]}}}" for field in fields)
        header = row_fmt.format(*fields)
        separator = "-+-".join("-" * col_widths[field] for field in fields)
        rows = [row_fmt.format(*(str(row.get(field, "")) for field in fields)) for row in content]
        return "\n".join([header, separator] + rows)


class PayoutTableFormatter(ABCFormatter[PayoutContentType, str]):
    def format(self, content: PayoutContentType) -> str:
        if not content:
            return ""

        grouped = defaultdict(list)
        for item in content:
            grouped[item["department"]].append(item)

        output_lines = []

        for department, employees in grouped.items():
            output_lines.append(department)

            header = f"{'':14} {'name':<28} {'hours':<9} {'rate':<9} {'payout'}"
            output_lines.append(header)

            total_hours = 0
            total_payout = 0

            for emp in employees:
                name = emp["name"]
                hours = emp["hours"]
                rate = emp["rate"]
                payout = emp["payout"]

                total_hours += hours
                total_payout += payout

                line = f"{'-' * 14} {name:<28} {hours:<9} {rate:<9} ${payout}"
                output_lines.append(line)

            summary = f"{'':<43} {total_hours:<9} {'':<9} ${total_payout}"
            output_lines.append(summary)
            output_lines.append("")
        return "\n".join(output_lines)
