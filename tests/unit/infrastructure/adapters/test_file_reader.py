import tempfile
from pathlib import Path

import pytest

from app.infrastructure.adapters.domain.readers.file_reader import FileReader


@pytest.mark.parametrize(
    "content",
    [
        "",
        "simple text",
        "тест",
        "𝔘𝔫𝔦𝔠𝔬𝔡𝔢",
        "line\nbreak",
        "emoji 😊",
    ],
)
def test_read_known_text_cases(content: str) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = Path(tmp_dir) / "test.txt"
        file_path.write_text(content, encoding="utf-8")

        reader = FileReader(file_path)
        result = reader.read()

        assert result == content


def test_file_not_found_error() -> None:
    fake_path = Path("/non/existing/path.txt")

    with pytest.raises(FileNotFoundError):
        FileReader(fake_path).read()
