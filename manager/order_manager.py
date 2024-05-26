from typing import Final

from data import User, Address, Order
from manager import CartManager
from payments import PaymentProcessor


class OrderManager:
    __cart_manager: Final[CartManager]

    def __init__(self, cart_manager: CartManager):
        self.__cart_manager = cart_manager

    def place_order(self, user: User, payment_processor: PaymentProcessor,
                    shipping_address: Address, billing_address: Address) -> Order:
        cart = self.__cart_manager.get_cart(user)
        if cart.cart_amount != payment_processor.get_payable_amount():
            raise RuntimeError("Invalid amount!")
        if not payment_processor.process_payment():
            raise RuntimeError("Payment failed!")
        order = Order(OrderManager.get_order_id(), cart, shipping_address, billing_address)
        self.__cart_manager.check_out_cart(user, order)
        return order

    @staticmethod
    def get_order_id() -> int:
        return 0
