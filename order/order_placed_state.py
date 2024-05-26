from data import OrderStatusDetails, DeliveryDetails, TransitDetails, PickUpDetails
from order.order_state import OrderState


class OrderPlacedState(OrderState):

    def schedule_pickup(self, pickup_details: PickUpDetails):
        pass

    def pickup(self):
        pass

    def end_transit(self, transit_details: TransitDetails):
        pass

    def schedule_delivery(self, delivery_details: DeliveryDetails):
        pass

    def deliver(self):
        pass

    def cancel(self):
        pass

    def get_status(self) -> OrderStatusDetails:
        pass