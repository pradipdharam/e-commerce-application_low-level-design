import abc
from abc import ABC
from typing import List

from data import Product


class ProductFilter(ABC):
    @abc.abstractmethod
    def filter(self, products: List[Product]) -> List[Product]:
        pass
