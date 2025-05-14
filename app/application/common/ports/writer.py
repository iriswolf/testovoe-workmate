from abc import ABC, abstractmethod


class ABCWriter[T](ABC):
    @abstractmethod
    def write(self, content: T) -> None: ...
