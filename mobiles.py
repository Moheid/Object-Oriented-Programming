class Mobiles:

    def __init__(self, name, version, price):
        self.name = name                    # Instant attributes 
        self.version = version                  # Instant attributes
        self.price = price                    # Instant attributes 
    
    def phone_prices(self):                         # This method 
        return "{} {}".format(self.name, self.version, self.price)
    
phone1 = Mobiles("iPhone", "15Pro Max", 1200)
phone2 = Mobiles("Samsung", "Ultra24", 1600)
 
print(phone1.phone_prices())
print(phone2.phone_prices())