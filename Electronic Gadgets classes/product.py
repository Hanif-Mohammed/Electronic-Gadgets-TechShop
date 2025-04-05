class Product:
    def __init__(self, product_id: int, product_name: str, description: str, price: float):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative.")

    def get_product_details(self):
        return f"ID: {self.__product_id}, Name: {self.__product_name}, Description: {self.__description}, Price: {self.__price}"

    def update_product_info(self, price=None, description=None):
        if price is not None:
            self.price = price
        if description is not None:
            self.__description = description
        return "Product details updated."
