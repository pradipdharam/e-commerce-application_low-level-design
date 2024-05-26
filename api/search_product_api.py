from typing import Final, List

from data import FilterDetails, Product
from searcher import ProductSearcher


class SearchProductAPI:
    __product_searcher: Final[ProductSearcher]

    def __init__(self, product_searcher):
        self.__product_searcher = product_searcher

    def search(self, product_name: str, filter_details: FilterDetails) -> List[Product]:
        return ProductSearcher.search_products(product_name, filter_details)
