from typing import Final

from data import User, Order
from permission import Permission


class TrackOrderPermission(Permission):
    __order: Final[Order]
    __user: Final[User]

    def __init__(self, order: Order, user: User):
        self.__order = order
        self.__user = user

    def is_permitted(self) -> bool:
        return False
