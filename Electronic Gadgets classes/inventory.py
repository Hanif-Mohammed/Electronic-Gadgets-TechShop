from datetime import datetime
from product import Product

class Inventory:
    def __init__(self, inventory_id: int, product: Product, quantity_in_stock: int):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = datetime.now()

    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def product(self):
        return self.__product

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @property
    def last_stock_update(self):
        return self.__last_stock_update

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        if value >= 0:
            self.__quantity_in_stock = value
            self.__last_stock_update = datetime.now()
        else:
            raise ValueError("Stock quantity cannot be negative.")

    def add_to_inventory(self, quantity):
        if quantity > 0:
            self.__quantity_in_stock += quantity
            self.__last_stock_update = datetime.now()
            return f"Added {quantity} units to inventory."
        raise ValueError("Invalid quantity.")

    def remove_from_inventory(self, quantity):
        if 0 < quantity <= self.__quantity_in_stock:
            self.__quantity_in_stock -= quantity
            self.__last_stock_update = datetime.now()
            return f"Removed {quantity} units from inventory."
        raise ValueError("Insufficient stock or invalid quantity.")
