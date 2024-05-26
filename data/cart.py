from typing import List, Final

from data import ProductCopy


class Cart:
    __id: Final[int]
    __products: Final[List[ProductCopy]]

    def __init__(self, id):
        self.__id = id
        self.__products = []

    def add(self, product_copy: ProductCopy) -> None:
        self.__products.append(product_copy)

    def remove(self, product_copy: ProductCopy) -> None:
        if product_copy not in self.__products:
            raise RuntimeError("Product not in cart!")
        self.__products.remove(product_copy)

    @property
    def cart_amount(self) -> float:
        amount = 0
        for copy in self.__products:
            amount += copy.product.price_in_inr
        return amount

    @property
    def distinct_item_count(self) -> int:
        distinct_ids = set()
        for copy in self.__products:
            distinct_ids.add(copy.id)
        return len(distinct_ids)

    @property
    def total_item_count(self) -> int:
        return len(self.__products)
