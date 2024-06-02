from typing import Final

from notification.subscriber import Subscriber


class EmailSubscriber(Subscriber):
    __email: Final[str]

    def __init__(self, email: str):
        self.__email = email

    def notify(self, message: str):
        pass
