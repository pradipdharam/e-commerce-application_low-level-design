import abc
from abc import ABC

from data import PickUpDetails, TransitDetails, DeliveryDetails, OrderStatusDetails


class OrderState(ABC):
    @abc.abstractmethod
    def schedule_pickup(self, pickup_details: PickUpDetails):
        pass

    @abc.abstractmethod
    def pickup(self):
        pass

    @abc.abstractmethod
    def end_transit(self, transit_details: TransitDetails):
        pass

    @abc.abstractmethod
    def schedule_delivery(self, delivery_details: DeliveryDetails):
        pass

    @abc.abstractmethod
    def deliver(self):
        pass

    @abc.abstractmethod
    def cancel(self):
        pass

    @abc.abstractmethod
    def get_status(self) -> OrderStatusDetails:
        pass
