from unittest.mock import patch

from app.infrastructure.adapters.application.writers.stdout_writer import StdoutWriter


def test_stdout_writer():
    writer = StdoutWriter()
    string = "test 123, hello world"
    with patch("builtins.print") as mock_print:
        writer.write(string)
        mock_print.assert_called_once_with(string)
