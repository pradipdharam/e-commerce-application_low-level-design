from permission import Permission


class AddToCartPermission(Permission):
    def is_permitted(self) -> bool:
        return False
