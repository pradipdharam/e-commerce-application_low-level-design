from data import Cart, User, Order


class DBAccessor:
    def get_products_by_name(self, product_name):
        pass

    @staticmethod
    def get_product_copy_by_id(product_id):
        pass

    @staticmethod
    def persist_cart(cart: Cart, user: User):
        pass

    @staticmethod
    def check_out_cart(cart, oder):
        pass

    @staticmethod
    def get_order_by_id(order_id: int) -> Order:
        pass
