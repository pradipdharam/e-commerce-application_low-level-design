from data import FilterDetails
from filter import ProductFilter, IdleFilter, RatingFilter, PayOnDeliverFilter, PriceFilter


class FilterFactory:
    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def product_filter(filter_details: FilterDetails) -> ProductFilter:
        filter_ = IdleFilter()
        if filter_details.rating_filter is not None:
            filter_ = RatingFilter(filter_details.rating_filter, filter_)
        if filter_details.pay_on_delivery_filter is not None:
            filter_ = PayOnDeliverFilter(filter_details.pay_on_delivery_filter, filter_)
        if filter_details.price_filter is not None:
            filter_ = PriceFilter(filter_details.price_filter, filter_)
        return filter_
