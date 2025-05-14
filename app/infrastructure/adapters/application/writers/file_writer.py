from pathlib import Path

from app.application.common.ports.writer import ABCWriter


class FileWriter(ABCWriter[bytes]):

    def __init__(self, file_path: Path, encoding: str = "utf-8") -> None:
        self._file_path = file_path
        self._encoding = encoding

    def write(self, content: bytes) -> None:
        """:raises OSError: Всё что рейзит Path(...).write_bytes(...)"""
        self._file_path.write_bytes(content)
