from exceptions import InvalidDataException
from collections import OrderedDict

class Product:
    def __init__(self, product_id: int, name: str, category: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

class ProductManager:
    def __init__(self):
        self.products = OrderedDict()  # Maintaining insertion order

    def add_product(self, product: Product):
        if product.product_id in self.products:
            raise InvalidDataException(f"Product with ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def update_product(self, product_id: int, name=None, category=None, price=None, stock=None):
        if product_id not in self.products:
            raise InvalidDataException(f"Product with ID {product_id} not found.")
        product = self.products[product_id]
        if name:
            product.name = name
        if category:
            product.category = category
        if price:
            product.price = price
        if stock is not None:
            product.stock = stock

    def remove_product(self, product_id: int):
        if product_id not in self.products:
            raise InvalidDataException(f"Product with ID {product_id} does not exist.")
        del self.products[product_id]

    def search_product(self, keyword: str):
        return [p for p in self.products.values() if keyword.lower() in p.name.lower() or keyword.lower() in p.category.lower()]
