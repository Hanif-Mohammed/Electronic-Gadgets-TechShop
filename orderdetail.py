from product import Product
from order import Order

class OrderDetail:
    def __init__(self, order_detail_id: int, order: Order, product: Product, quantity: int):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

        order.add_order_detail(self)

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value > 0:
            self.__quantity = value
        else:
            raise ValueError("Quantity must be positive.")

    def calculate_subtotal(self):
        return self.__quantity * self.__product.price

    def get_order_detail_info(self):
        return f"OrderDetail ID: {self.__order_detail_id}, Order ID: {self.__order.order_id}, Product: {self.__product.product_name}, Quantity: {self.__quantity}, Subtotal: {self.calculate_subtotal()}"
