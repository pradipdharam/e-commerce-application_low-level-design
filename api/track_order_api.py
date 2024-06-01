from data import User, OrderStatusDetails
from db import DBAccessor
from permission import PermissionFactory


class TrackOrderAPI:
    def track_order(self, order_id: int, user: User) -> OrderStatusDetails:
        order = DBAccessor.get_order_by_id(order_id)
        if order is None:
            raise RuntimeError("Unable to fetch order")
        permission = PermissionFactory.get_track_order_permission(order, user)
        if permission is None or permission.is_permitted():
            raise RuntimeError("Action not permitted")
        return order.get_order_details()
