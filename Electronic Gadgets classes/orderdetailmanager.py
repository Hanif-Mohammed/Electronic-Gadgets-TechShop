from exceptions import IncompleteOrderException, InsufficientStockException


class OrderDetail:
    def __init__(self, order_detail_id: int, order_id: int, product_id: int, quantity: int):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity


class OrderDetailManager:
    def __init__(self, inventory_manager):
        self.order_details = []
        self.inventory_manager = inventory_manager

    def add_order_detail(self, order_detail: OrderDetail):
        """Validate product availability before adding order details."""
        if not self.inventory_manager.check_stock(order_detail.product_id, order_detail.quantity):
            raise InsufficientStockException(f"Not enough stock for product ID {order_detail.product_id}.")

        self.order_details.append(order_detail)
        self.inventory_manager.update_inventory(order_detail.product_id, self.inventory_manager.inventory[
            order_detail.product_id] - order_detail.quantity)

    def remove_order_detail(self, order_detail_id: int):
        """Remove order details."""
        self.order_details = [od for od in self.order_details if od.order_detail_id != order_detail_id]
