import tempfile
from pathlib import Path

import pytest

from app.infrastructure.adapters.application.writers.file_writer import FileWriter


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
def test_file_writer(content: str) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        fp = Path(tmp_dir) / "test.txt"
        fw = FileWriter(fp)
        fw.write(content.encode("utf-8"))

        result = fp.read_text("utf-8")
        assert result == content
