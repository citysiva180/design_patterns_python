# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# ConcreteStrategy


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card")

# ConcreteStrategy


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal")

# ConcreteStrategy


class GooglePayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Google Pay")

# Context


class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount):
        self.payment_strategy.pay(amount)


# Client code
if __name__ == "__main__":
    # Creating payment strategies
    credit_card_strategy = CreditCardPayment()
    paypal_strategy = PayPalPayment()
    google_pay_strategy = GooglePayPayment()

    # Creating context with the default strategy (Credit Card)
    payment_context = PaymentContext(credit_card_strategy)

    # Making payments with different strategies
    # Output: Paying $1000 using Credit Card
    payment_context.make_payment(1000)

    # Changing the payment strategy to PayPal
    payment_context.set_payment_strategy(paypal_strategy)
    payment_context.make_payment(500)   # Output: Paying $500 using PayPal

    # Changing the payment strategy to Google Pay
    payment_context.set_payment_strategy(google_pay_strategy)
    payment_context.make_payment(750)   # Output: Paying $750 using Google Pay
