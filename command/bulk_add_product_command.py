from typing import Final, List

from command import Command
from data import ProductCopy, User


class BulkAddProductCommand(Command):
    __user: Final[User]
    __product_copies: Final[List[ProductCopy]]

    def __init__(self, user: User, product_copies: List[ProductCopy]):
        self.__user = user
        self.__product_copies = product_copies

    def execute(self):
        pass
