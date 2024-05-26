from typing import Final, List

from data import FilterDetails, Product, User
from permission import PermissionFactory
from searcher import ProductSearcher


class SearchProductAPI:
    __product_searcher: Final[ProductSearcher]

    def __init__(self, product_searcher):
        self.__product_searcher = product_searcher

    def search(self, product_name: str, filter_details: FilterDetails,
               user: User) -> List[Product]:
        permission = PermissionFactory.get_search_permission(user)
        if not permission.is_permitted():
            raise RuntimeError("Search request not permitted!")
        return ProductSearcher.search_products(product_name, filter_details)
