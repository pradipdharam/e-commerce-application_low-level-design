from typing import Final


class Address:
    __address_line1: Final[str]
    __address_line2: Final[str]
    __address_line3: Final[str]
    __city: Final[str]
    __state: Final[str]
    __country: Final[str]
    __zip: Final[str]

    def __init__(self, address_line1, address_line2, address_line3,
                 city, state, country, zip):
        self.__address_line1 = address_line1
        self.__address_line2 = address_line2
        self.__address_line3 = address_line3
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zip = zip

    @property
    def address_line1(self):
        return self.__address_line1

    @property
    def address_line2(self):
        return self.__address_line2

    @property
    def address_line3(self):
        return self.__address_line3

    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def country(self):
        return self.__country

    @property
    def zip(self):
        return self.__zip
