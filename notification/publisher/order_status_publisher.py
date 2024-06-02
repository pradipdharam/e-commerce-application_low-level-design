from typing import List

from notification.publisher import Publisher
from notification.subscriber import Subscriber


class OrderStatusPublisher(Publisher):
    __subscribers: List[Subscriber]

    def __init__(self):
        self.__subscribers = []

    def add_subscriber(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self.__subscribers.remove(subscriber)

    def notify_all(self, message: str):
        for subscriber in self.__subscribers:
            subscriber.notify(message)
