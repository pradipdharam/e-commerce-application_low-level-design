from typing import Final

from data import Rating


class Product:
    __product_id: Final[int]
    __name: Final[str]
    __description: Final[str]
    __price_in_inr: Final[float]
    __rating: Final[Rating]
    __pay_on_delivery: Final[bool]

    def __init__(self, product_id: int, name: str, description: str, price_in_inr: float,
                 rating: Rating, pay_on_delivery: bool):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price_in_inr = price_in_inr
        self.__rating = rating
        self.__pay_on_delivery = pay_on_delivery

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price_in_inr(self):
        return self.__price_in_inr

    @property
    def rating(self):
        return self.__rating

    @property
    def pay_on_delivery(self):
        return self.__pay_on_delivery
