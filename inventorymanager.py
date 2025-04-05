from exceptions import InsufficientStockException
from sortedcontainers import SortedDict

class Inventory:
    def __init__(self):
        self.inventory = SortedDict()

    def add_inventory(self, product_id: int, quantity: int):
        self.inventory[product_id] = self.inventory.get(product_id, 0) + quantity

    def update_inventory(self, product_id: int, quantity: int):
        if product_id not in self.inventory:
            raise InsufficientStockException(f"Product ID {product_id} not found in inventory.")
        self.inventory[product_id] = quantity

    def remove_inventory(self, product_id: int):
        if product_id in self.inventory:
            del self.inventory[product_id]

    def check_stock(self, product_id: int, quantity: int):
        if product_id not in self.inventory or self.inventory[product_id] < quantity:
            raise InsufficientStockException(f"Not enough stock for product ID {product_id}. Available: {self.inventory.get(product_id, 0)}")
        return True
