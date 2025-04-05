from exceptions import IncompleteOrderException
from datetime import datetime
from collections import OrderedDict

class Order:
    def __init__(self, order_id: int, customer_id: int, order_date: datetime, status: str, total_amount: float):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status
        self.total_amount = total_amount

class OrderManager:
    def __init__(self):
        self.orders = OrderedDict()

    def add_order(self, order: Order):
        if order.order_id in self.orders:
            raise IncompleteOrderException(f"Order with ID {order.order_id} already exists.")
        self.orders[order.order_id] = order

    def update_order_status(self, order_id: int, status: str):
        if order_id not in self.orders:
            raise IncompleteOrderException(f"Order with ID {order_id} not found.")
        self.orders[order_id].status = status

    def remove_order(self, order_id: int):
        if order_id in self.orders:
            del self.orders[order_id]

    def sort_orders_by_date(self, descending=False):
        return sorted(self.orders.values(), key=lambda x: x.order_date, reverse=descending)
