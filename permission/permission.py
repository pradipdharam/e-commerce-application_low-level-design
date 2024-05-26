import abc
from abc import ABC


class Permission(ABC):
    @abc.abstractmethod
    def is_permitted(self) -> bool:
        pass
