from typing import Final

from notification.subscriber import Subscriber


class SMSSubscriber(Subscriber):
    __phone_number: Final[str]

    def __init__(self, phone_number: str):
        self.__phone_number = phone_number

    def notify(self, message: str):
        pass
