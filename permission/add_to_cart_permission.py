from typing import Final

from data import User, ProductCopy
from manager import CartManager
from permission import Permission


class AddToCartPermission(Permission):
    MAX_CART_AMOUNT = 1000000
    DISTINCT_CART_ITEMS_LIMIT = 50
    TOTAL_ITEMS_LIMIT = 1000

    __user: Final[User]
    __product_copy: Final[ProductCopy]

    def __init__(self, user: User, product_copy: ProductCopy):
        self.__user = user
        self.__product_copy = product_copy

    def is_permitted(self) -> bool:
        cart = CartManager.get_cart(self.__user)
        if cart.cart_amount > AddToCartPermission.MAX_CART_AMOUNT or \
                cart.distinct_item_count > AddToCartPermission.DISTINCT_CART_ITEMS_LIMIT or \
                cart.total_item_count > AddToCartPermission.TOTAL_ITEMS_LIMIT:
            return False
        return False
