import abc
from abc import ABC


class PaymentProcessor(ABC):
    @abc.abstractmethod
    def process_payment(self) -> bool:
        pass

    @abc.abstractmethod
    def get_payable_amount(self) -> float:
        pass
