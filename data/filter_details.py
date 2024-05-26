from typing import Final, Union

from data import Rating


class FilterDetails:
    __price_filter: Final[Union[None, float]]
    __rating_filter: Final[Union[None, Rating]]
    __pay_on_delivery_filter: Final[Union[None, bool]]

    def __init__(self,
                 price_filter: Union[None, float],
                 rating_filter: Union[None, Rating],
                 pay_on_delivery_filter: Union[None, bool]):
        self.__price_filter = price_filter
        self.__rating_filter = rating_filter
        self.__pay_on_delivery_filter = pay_on_delivery_filter

    @property
    def price_filter(self):
        return self.__price_filter

    @property
    def rating_filter(self):
        return self.__rating_filter

    @property
    def pay_on_delivery_filter(self):
        return self.__pay_on_delivery_filter
