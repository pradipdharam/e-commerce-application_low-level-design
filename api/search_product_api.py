from typing import Final


class SearchProductAPI:
    __product_searcher: Final[ProductSearcher]

    def __init__(self, product_searcher):
        self.__product_searcher = product_searcher

    def search(self, product_name: str, filter_details: FilterDetails):
        pass

