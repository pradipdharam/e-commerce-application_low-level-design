from typing import Final

from data import Product


class ProductCopy:
    __product: Final[Product]
    __id: Final[int]
    __is_sold: Final[bool]

    def __init__(self, product, id, is_sold):
        self.__id = id
        self.__product = product
        self.__is_sold = is_sold

    @property
    def id(self):
        return self.__id

    @property
    def product(self):
        return self.__product

    @property
    def is_sold(self):
        return self.__is_sold
