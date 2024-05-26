from typing import Final


class OrderStatusDetails:
    __order_status: Final[OrderStatus]
    __description: Final[str]

    def __init__(self, order_status: OrderStatus, description: str):
        self.__order_status = order_status
        self.__description = description

    @property
    def order_status(self):
        return self.__order_status

    @property
    def description(self):
        return self.__description
