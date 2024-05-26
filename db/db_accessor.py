from data import Cart, User


class DBAccessor:
    def get_products_by_name(self, product_name):
        pass

    @staticmethod
    def get_product_copy_by_id(product_id):
        pass

    @staticmethod
    def persist_cart( cart: Cart, user: User):
        pass

    @classmethod
    def check_out_cart(cls, cart, oder):
        pass
