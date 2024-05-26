from typing import List, Final

from data import Product
from filter import ProductFilter


class PayOnDeliverFilter(ProductFilter):
    __is_pay_on_delivery: Final[bool]
    __next_filter: Final[ProductFilter]

    def __init__(self, is_pay_on_delivery: bool, next_filter: ProductFilter):
        self.__is_pay_on_delivery = is_pay_on_delivery
        self.__next_filter = next_filter

    def filter(self, products: List[Product]) -> List[Product]:
        pass
