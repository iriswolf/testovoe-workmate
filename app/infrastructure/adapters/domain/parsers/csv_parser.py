from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

from app.domain.reports.ports.parser import ABCParser

if TYPE_CHECKING:
    from app.infrastructure.descriptors.csv_descriptors.dialects.dialect import Dialect


CSVParseOutput = list[dict[str, Any]]


class CSVParser(ABCParser[str, CSVParseOutput]):

    def __init__(self, dialect: "Dialect") -> None:
        self._dialect = dialect

    def parse(self, content: str) -> CSVParseOutput:
        lines = content.splitlines()
        if not lines:
            return []

        reader = self._iter_lines(lines)
        try:
            headers = next(reader)
        except StopIteration:
            return []

        result: list[dict[str, Any]] = []
        for row in reader:
            if len(row) != len(headers):
                continue
            result.append(dict(zip(headers, row, strict=False)))
        return result

    def _iter_lines(self, lines: list[str]) -> Iterator[list[str]]:
        d = self._dialect
        delimiter = d.delimiter
        quotechar = d.quote_char
        skip_space = d.skip_initial_space

        for line in lines:
            if not line.strip():
                continue

            result: list[str] = []
            current = ""
            inside_quotes = False
            i = 0
            while i < len(line):
                char = line[i]

                if char == quotechar:
                    if (
                        inside_quotes
                        and d.doublequote
                        and i + 1 < len(line)
                        and line[i + 1] == quotechar
                    ):
                        current += quotechar
                        i += 1
                    else:
                        inside_quotes = not inside_quotes
                elif char == delimiter and not inside_quotes:
                    result.append(current.strip() if skip_space else current)
                    current = ""
                else:
                    current += char
                i += 1

            result.append(current.strip() if skip_space else current)
            yield result
