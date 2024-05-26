from typing import Union

from data.user import User
from permission import Permission, SearchProductPermission


class PermissionFactory:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def get_search_permission(user: User) -> Union[None, Permission]:
        # Query DB & retrieve permission the user is associated with.
        # construct and return permission.
        return SearchProductPermission(user)

    @staticmethod
    def get_add_to_cart_permission(user: User) -> Union[None, Permission]:
        # Query DB & retrieve permission the user is associated with.
        # construct and return permission.
        return None