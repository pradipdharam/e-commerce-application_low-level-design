from typing import Final

from data import Cart, Address, TransitDetails, OrderStatusDetails
from order import OrderState


class Order:
    __order_id: Final[int]
    __cart: Final[Cart]
    __shipping_address: Final[Address]
    __billing_address: Final[Address]
    __order_state: OrderState

    def __init__(self, order_id: int, cart: Cart, shipping_address: Address,
                 billing_address: Address, order_state: OrderState) -> None:
        self.__order_id = order_id
        self.__cart = cart
        self.__shipping_address = shipping_address
        self.__billing_address = billing_address
        # order state value instantiation.
        # 1. Go and check in DB whether order exists & retrieve the status for assignment.
        # 2. If order is not present in db, consider order is placed, i.e. initialize it to its first status.
        self.__order_state = order_state

    @property
    def order_id(self):
        return self.__order_id

    @property
    def cart(self):
        return self.__cart

    @property
    def shipping_address(self):
        return self.__shipping_address

    @property
    def billing_address(self):
        return self.__billing_address

    def schedule_pick_up(self, pickup_details):
        self.__order_state.schedule_pickup(pickup_details)

    def cancel(self):
        self.__order_state.cancel()

    def pick_up(self):
        self.__order_state.pickup()

    def end_transit(self, transit_details: TransitDetails):
        self.__order_state.end_transit(transit_details)

    def get_order_details(self) -> OrderStatusDetails:
        return self.__order_state.get_status()
