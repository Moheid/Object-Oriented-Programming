class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, expiry):
        self.card_number = card_number
        self.expiry = expiry
    
    def process_payment(self, amount):
        return f"Processed ${amount} via Credit Card ending in {self.card_number[-4:]}"

class MobileWalletPayment(PaymentMethod):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id
    
    def process_payment(self, amount):
        return f"Processed ${amount} via Mobile Wallet {self.wallet_id[:4]}..."

class BankTransferPayment(PaymentMethod):
    def __init__(self, account_number, routing_number):
        self.account_number = account_number
        self.routing_number = routing_number
    
    def process_payment(self, amount):
        return f"Processed ${amount} via Bank Transfer to account {self.account_number[-4:]}"

def process_customer_payment(payment_method, amount):
    print(payment_method.process_payment(amount))

# Usage
credit_card = CreditCardPayment("4111111111111111", "12/25")
mobile_wallet = MobileWalletPayment("WALL123456789")
bank_transfer = BankTransferPayment("987654321", "026009593")

process_customer_payment(credit_card, 50.00)  # Processed $50.00 via Credit Card ending in 1111
process_customer_payment(mobile_wallet, 30.00)  # Processed $30.00 via Mobile Wallet WALL...
process_customer_payment(bank_transfer, 75.00)  # Processed $75.00 via Bank Transfer to account 4321