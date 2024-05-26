from typing import Final

from data import User
from manager import CartManager
from permission import Permission


class AddToCartPermission(Permission):
    MAX_CART_AMOUNT = 1000000
    DISTINCT_CART_ITEMS_LIMIT = 50
    TOTAL_ITEMS_LIMIT = 1000

    __user: Final[User]

    def __init__(self, user: User):
        self.__user = user

    def is_permitted(self) -> bool:
        cart = CartManager.get_cart(self.__user)
        if cart.cart_amount > AddToCartPermission.MAX_CART_AMOUNT or \
                cart.distinct_item_count > AddToCartPermission.DISTINCT_CART_ITEMS_LIMIT or \
                cart.total_item_count > AddToCartPermission.TOTAL_ITEMS_LIMIT:
            return False
        return False
