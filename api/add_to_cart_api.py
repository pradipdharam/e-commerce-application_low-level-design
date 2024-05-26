from data import User
from db import DBAccessor
from permission import PermissionFactory
from searcher import ProductSearcher


class AddToCartAPI:
    def add_to_cart(self, product_id: int, user: User) -> None:
        product_copy = DBAccessor.get_product_copy_by_id(product_id)
        if product_copy is None:
            raise RuntimeError("Invalid product ID")

        permission = PermissionFactory.get_add_to_cart_permission(user, product_copy)
        if not permission.is_permitted():
            raise RuntimeError("Add to cart operation not permitted!")

        # Add further product to the cart. Create class Cart
