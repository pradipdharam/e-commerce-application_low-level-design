from permission import Permission


class SearchProductPermission(Permission):
    def is_permitted(self) -> bool:
        return True
