class CustomerAccount:
    def __init__(self, customer_id, balance=0):
        self.customer_id = customer_id  # public
        self.__balance = balance  # private
        self.__call_history = []  # private
    
    def add_call(self, duration, cost):
        self.__balance += cost
        self.__call_history.append((duration, cost))
    
    def make_payment(self, amount):
        if amount > 0:
            self.__balance -= amount
            return f"Payment of ${amount} received. New balance: ${self.__balance}"
        return "Invalid payment amount"
    
    def get_balance(self):
        return self.__balance
    
    def get_call_history(self):
        return self.__call_history.copy()  # Return copy to prevent modification

# Usage
customer = CustomerAccount("TEL12345")
customer.add_call(10, 2.50)  # 10 minute call, $2.50
customer.add_call(5, 1.25)   # 5 minute call, $1.25
print(customer.make_payment(3.00))  # Payment of $3.00 received. New balance: $0.75
print(customer.get_balance())  # 0.75