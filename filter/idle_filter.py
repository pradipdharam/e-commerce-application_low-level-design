from typing import List

from data import Product
from filter import ProductFilter


class IdleFilter(ProductFilter):
    def filter(self, products: List[Product]) -> List[Product]:
        return products
