from app.infrastructure.adapters.application.formatters.table_formatter import (
    PayoutTableFormatter,
    TableFormatter,
)


def test_table_formatter_with_data():
    content = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]
    formatter = TableFormatter()
    result = formatter.format(content)

    expected = "name  | age\n" "------+----\n" "Alice | 30 \n" "Bob   | 25 "
    assert result.strip() == expected.strip()


def test_table_formatter_empty():
    formatter = TableFormatter()
    result = formatter.format([])
    assert result == ""


def test_payout_table_formatter_grouped_output():
    content = [
        {"department": "HR", "name": "Alice", "hours": 10, "rate": 20, "payout": 200},
        {"department": "HR", "name": "Bob", "hours": 5, "rate": 20, "payout": 100},
        {"department": "IT", "name": "Charlie", "hours": 8, "rate": 25, "payout": 200},
    ]

    formatter = PayoutTableFormatter()
    result = formatter.format(content)

    assert "HR" in result
    assert "IT" in result
    assert "Alice" in result
    assert "Charlie" in result
    assert "$200" in result
    assert "$100" in result
    assert "$300" in result  # HR total
    assert "$200" in result  # IT total


def test_payout_table_formatter_empty():
    formatter = PayoutTableFormatter()
    result = formatter.format([])
    assert result == ""
