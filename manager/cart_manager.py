from data import User, ProductCopy
from db import DBAccessor


class CartManager:
    def get_cart(self, user: User):
        return DBAccessor.get_cart(user)

    def add_to_cart(self, user: User, product_copy: ProductCopy):
        if product_copy.is_sold:
            raise RuntimeError("Product sold! Cannot add to the cart.")
        cart = self.get_cart(user)
        cart.add(product_copy)
        DBAccessor.persist_cart(cart, user)

    def remove_from_cart(self, user: User, product_copy: ProductCopy):
        cart = self.get_cart(user)
        cart.remove(product_copy)
        DBAccessor.persist_cart(cart, user)
