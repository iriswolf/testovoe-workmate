from abc import ABC, abstractmethod


class ABCFormatter[T, RT](ABC):
    @abstractmethod
    def format(self, content: T) -> RT: ...
