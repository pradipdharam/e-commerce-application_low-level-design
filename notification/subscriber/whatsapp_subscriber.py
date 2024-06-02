from typing import Final

from notification.subscriber import Subscriber


class WhatsappSubscriber(Subscriber):
    __whatsapp_number: Final[str]

    def __init__(self, whatsapp_number: str):
        self.__whatsapp_number = whatsapp_number

    def notify(self, message: str):
        pass
