from typing import List

from data import FilterDetails, Product
from filter import FilterFactory


class ProductSearcher:
    @staticmethod
    def search_products(product_name: str,
                        filter_details: FilterDetails) -> List[Product]:
        products = DBAccessor.get_products_by_name(product_name)
        return FilterFactory.product_filter(filter_details).filter(products)
