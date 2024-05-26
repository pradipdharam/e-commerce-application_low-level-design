from typing import Final

from data import User
from permission import Permission


class SearchProductPermission(Permission):
    __user: Final[User]

    def __init__(self, user: User):
        self.__user = user

    def is_permitted(self) -> bool:
        return True
