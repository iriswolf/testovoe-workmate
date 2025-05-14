from pathlib import Path

from app.domain.reports.ports.reader import ABCReader


class FileReader(ABCReader[str]):

    def __init__(self, file_path: Path, encoding: str = "utf-8") -> None:
        self._file_path = file_path
        self._encoding = encoding

    def read(self) -> str:
        """:raises OSError: и подклассы"""
        return self._file_path.read_text(self._encoding)
