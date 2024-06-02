from typing import Final

from command import Command
from data import ProductCopy, User


class AddProductCommand(Command):
    __user: Final[User]
    __product_copy: Final[ProductCopy]

    def __init__(self, user: User, product_copy: ProductCopy):
        self.__user = user
        self.__product_copy = product_copy

    def execute(self):
        pass
