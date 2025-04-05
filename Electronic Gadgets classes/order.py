from datetime import datetime
from customer import Customer

class Order:
    def __init__(self, order_id: int, customer: Customer, total_amount: float):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = datetime.now()
        self.__total_amount = total_amount
        self.__status = "Processing"
        self.__order_details = []


        customer.add_order(self)

    @property
    def order_id(self):
        return self.__order_id

    @property
    def customer(self):
        return self.__customer

    @property
    def order_date(self):
        return self.__order_date

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def status(self):
        return self.__status

    @property
    def order_details(self):
        return self.__order_details

    @total_amount.setter
    def total_amount(self, value):
        if value >= 0:
            self.__total_amount = value
        else:
            raise ValueError("Total amount cannot be negative.")

    @status.setter
    def status(self, value):
        if value in ["Processing", "Shipped", "Delivered", "Cancelled"]:
            self.__status = value
        else:
            raise ValueError("Invalid order status.")

    def add_order_detail(self, order_detail):
        self.__order_details.append(order_detail)

    def get_order_details(self):
        return f"Order ID: {self.__order_id}, Customer: {self.__customer.get_customer_details()}, Date: {self.__order_date}, Amount: {self.__total_amount}, Status: {self.__status}"
