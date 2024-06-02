import abc

from notification.subscriber import Subscriber


class Publisher(abc.ABC):
    @abc.abstractmethod
    def add_subscriber(self, subscriber: Subscriber):
        pass

    @abc.abstractmethod
    def remove_subscriber(self, subscriber: Subscriber):
        pass

    @abc.abstractmethod
    def notify_all(self, message: str):
        pass
