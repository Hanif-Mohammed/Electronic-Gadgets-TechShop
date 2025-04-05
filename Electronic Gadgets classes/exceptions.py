class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided."):
        super().__init__(message)


class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock available for the requested quantity."):
        super().__init__(message)


class IncompleteOrderException(Exception):
    def __init__(self, message="Order detail is incomplete or missing required fields."):
        super().__init__(message)


class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed. Please try again."):
        super().__init__(message)


class FileIOException(Exception):
    def __init__(self, message="Error occurred while reading/writing to a file."):
        super().__init__(message)


class SqlException(Exception):
    def __init__(self, message="Database operation failed. Please check the connection."):
        super().__init__(message)


class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency conflict detected. Please retry your operation."):
        super().__init__(message)


class AuthenticationException(Exception):
    def __init__(self, message="User authentication failed. Invalid credentials provided."):
        super().__init__(message)


class AuthorizationException(Exception):
    def __init__(self, message="Access denied. You do not have permission to perform this action."):
        super().__init__(message)
