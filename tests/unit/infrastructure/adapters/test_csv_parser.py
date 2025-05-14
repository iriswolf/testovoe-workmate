import pytest

from app.infrastructure.adapters.domain.parsers.csv_parser import CSVParser

CSV_SIMPLE = "id,name\n1,Alice\n2,Bob"
EXPECTED_SIMPLE = [{"id": "1", "name": "Alice"}, {"id": "2", "name": "Bob"}]

CSV_QUOTED = 'a,b\n"x,y",z'
EXPECTED_QUOTED = [{"a": "x,y", "b": "z"}]

CSV_ESCAPED_QUOTES = 'id,name\n1,"Bob ""The Boss"""'
EXPECTED_ESCAPED_QUOTES = [{"id": "1", "name": 'Bob "The Boss"'}]

CSV_MALFORMED_ROWS = "id,name\n1\n2,Bob\n3,Alice,Extra\n4,Ana"
EXPECTED_MALFORMED_ROWS = [{"id": "2", "name": "Bob"}, {"id": "4", "name": "Ana"}]

CSV_EMPTY = ""
CSV_ONLY_NEWLINES = "\n\n\n"
CSV_MIXED = "id,name\n\n1,Bob\n\n\n2,Alice\n"
EXPECTED_MIXED = [{"id": "1", "name": "Bob"}, {"id": "2", "name": "Alice"}]


@pytest.mark.parametrize(
    (
        "content",
        "expected",
    ),
    [
        pytest.param(CSV_SIMPLE, EXPECTED_SIMPLE, id="simple rows"),
        pytest.param(CSV_QUOTED, EXPECTED_QUOTED, id="quoted value with comma"),
        pytest.param(CSV_ESCAPED_QUOTES, EXPECTED_ESCAPED_QUOTES, id="escaped quotes"),
    ],
)
def test_csv_parser_common_cases(excel_dialect, content, expected):
    parser = CSVParser(excel_dialect)
    result = parser.parse(content)

    assert isinstance(result, list)
    assert result == expected


@pytest.mark.parametrize(
    (
        "content",
        "expected",
    ),
    [
        pytest.param(CSV_MALFORMED_ROWS, EXPECTED_MALFORMED_ROWS, id="skip malformed rows"),
        pytest.param(CSV_EMPTY, [], id="empty content"),
        pytest.param(CSV_ONLY_NEWLINES, [], id="only newlines"),
        pytest.param(CSV_MIXED, EXPECTED_MIXED, id="mixed empty + valid rows"),
    ],
)
def test_csv_parser_edge_cases(content, expected, excel_dialect):
    parser = CSVParser(excel_dialect)
    result = parser.parse(content)

    assert isinstance(result, list)
    assert result == expected
