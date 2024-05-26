from typing import Final

from data import User
from db import DBAccessor
from manager import CartManager
from permission import PermissionFactory


class AddToCartAPI:
    __cart_manager: Final[CartManager]

    def __init__(self, cart_manager: CartManager):
        self.__cart_manager = cart_manager

    def add_to_cart(self, product_id: int, user: User) -> None:
        product_copy = DBAccessor.get_product_copy_by_id(product_id)
        if product_copy is None:
            raise RuntimeError("Invalid product ID")

        permission = PermissionFactory.get_add_to_cart_permission(user, product_copy)
        if not permission.is_permitted():
            raise RuntimeError("Add to cart operation not permitted!")

        self.__cart_manager.add_to_cart(user, product_copy)
