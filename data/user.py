from typing import Final


class User:
    __id: Final[int]
    __name: Final[str]
    __email: Final[str]
    __phone: Final[str]

    def __init__(self, id, name, email, phone):
        """Builder design pattern also can be used here.
        """
        self.__id = id
        self.__name = name
        self.__email = email
        self.__phone = phone

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone
