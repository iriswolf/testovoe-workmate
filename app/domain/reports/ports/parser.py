from abc import ABC, abstractmethod


class ABCParser[T, RT](ABC):
    @abstractmethod
    def parse(self, content: T) -> RT: ...
