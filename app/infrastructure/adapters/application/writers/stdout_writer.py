from app.application.common.ports.writer import ABCWriter


class StdoutWriter(ABCWriter[str]):
    def write(self, content: str) -> None:
        print(content)  # noqa
