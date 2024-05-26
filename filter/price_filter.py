from typing import List, Final

from data import Product
from filter import ProductFilter


class PriceFilter(ProductFilter):
    __price_upper_cap: Final[float]
    __next_filter: Final[ProductFilter]

    def __init__(self, price_upper_cap: float, next_filter: ProductFilter):
        self.__price_upper_cap = price_upper_cap
        self.__next_filter = next_filter

    def filter(self, products: List[Product]) -> List[Product]:
        filtered_products = self.__next_filter.filter(products)
        final_products = []
        for product in filtered_products:
            if product.price_in_inr <= self.__price_upper_cap:
                final_products.append(product)
        return final_products
