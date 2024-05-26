from typing import List, Final

from data import Product, Rating
from filter import ProductFilter


class RatingFilter(ProductFilter):
    __min_rating: Final[Rating]
    __next_filter: Final[ProductFilter]

    def __init__(self, min_rating: Rating, next_filter: ProductFilter):
        self.__min_rating = min_rating
        self.__next_filter = next_filter

    def filter(self, products: List[Product]) -> List[Product]:
        filtered_products = self.__next_filter.filter(products)
        final_products = []
        for product in filtered_products:
            if product.rating >= self.__min_rating:
                final_products.append(product)
        return final_products
