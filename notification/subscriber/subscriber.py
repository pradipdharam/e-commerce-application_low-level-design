import abc


class Subscriber(abc.ABC):
    @abc.abstractmethod
    def notify(self, message: str):
        pass
  