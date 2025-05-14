from abc import ABC, abstractmethod


class ABCReader[RT](ABC):

    @abstractmethod
    def read(self) -> RT: ...
