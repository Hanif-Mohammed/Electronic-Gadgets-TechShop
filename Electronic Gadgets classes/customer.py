class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__orders = []

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    @property
    def orders(self):
        return self.__orders

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            raise ValueError("Invalid email format.")

    @phone.setter
    def phone(self, value):
        if value.isdigit() and len(value) in (10, 11):
            self.__phone = value
        else:
            raise ValueError("Invalid phone number.")

    @address.setter
    def address(self, value):
        if value:
            self.__address = value
        else:
            raise ValueError("Address cannot be empty.")

    def calculate_total_orders(self):
        return len(self.__orders)

    def get_customer_details(self):
        return f"ID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        return "Customer information updated."
