from exceptions import PaymentFailedException

class Payment:
    def __init__(self, payment_id: int, order_id: int, amount: float, status: str):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.status = status

class PaymentManager:
    def __init__(self):
        self.payments = {}

    def record_payment(self, payment: Payment):
        """Record a new payment."""
        self.payments[payment.payment_id] = payment

    def update_payment_status(self, payment_id: int, status: str):
        """Update payment status."""
        if payment_id not in self.payments:
            raise PaymentFailedException(f"Payment ID {payment_id} not found.")
        self.payments[payment_id].status = status

    def get_payment_status(self, payment_id: int):
        """Retrieve payment status."""
        return self.payments.get(payment_id, None)
