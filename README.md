# Object-Oriented Programming in Python Masterclass

This repository contains the code examples and exercises for the Object-Oriented Programming in Python Masterclass. Below is an overview of each file corresponding to the topics covered in the course.

- `basics.py`: Introduces the fundamental concepts of classes, instances, attributes, and methods in Python.
- `magicmethods.py`: Demonstrates the use of magic methods, including operator overloading and protocols.
- `inheritance.py`: Contains examples of single inheritance, showcasing how a class can inherit attributes and methods from another class.
- `slots.py`: A placeholder for the topic of slots, which will be covered later in the course to optimize memory usage.
- `dataclasses_and_enums.py`: Provides examples of dataclasses for automated attribute management and enums for enumerations.
- `multipleinheritance.py`: Explores the concept of multiple inheritance and mixin classes in Python.
- `getters_and_setters.py`: Illustrates the use of properties, getters, and setters for controlled attribute access.
- `deskriptors.py`: Covers both data and non-data descriptors for managing attribute access in a class.
- `abcs.py`: Implements abstract base classes to define a common API for a set of subclasses.
- `metaprogramming.py`: Discusses metaprogramming concepts for creating dynamic and flexible code.
- `pattern.py`: Examines various design patterns and how they can be implemented in Python.

Each file is a standalone module providing clear examples related to the topic it represents. Feel free to explore and experiment with the code to deepen your understanding of object-oriented programming in Python.

### *Object-Oriented Programming (OOP) in Python: Ultimate Guide*  

#### *1. What is OOP?*  
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects rather than functions and logic. Python fully supports OOP concepts, which help in creating modular, reusable, and maintainable code. OOP is a programming paradigm that structures code around *objects* - self-contained units that combine:  
- *Data* (attributes/properties)  
- *Behavior* (methods/functions)  

Instead of writing procedural code (step-by-step instructions), you model real-world entities as interacting objects.  

---

### *2. Four Core Principles (Types of OOP)*  
| Principle       | Description                                                                 | Python Example                                 |
|-----------------|-----------------------------------------------------------------------------|-----------------------------------------------|
| *Encapsulation* | Bundling data + methods into a class. Controlling access via public/private members. | self.__private_data                         |
| *Inheritance*  | Creating new classes (children) from existing classes (parents). Promotes code reuse. | class Child(Parent):                        |
| *Polymorphism* | Objects of different classes responding to the same method call differently. | shape.draw() works for Circle, Square, etc. |
| *Abstraction*  | Hiding complex implementation details behind simplified interfaces.        | Using @abstractmethod                       |

---

### *3. When to Use OOP*  
✅ **Complex Systems**:  
   - GUI applications (buttons, windows as objects)  
   - Game development (players, enemies, items)  
   - Enterprise software (users, orders, inventory)  

✅ **Code Reusability**:  
   - When multiple entities share functionality (e.g., different user roles inherit from User)  

✅ **State Management**:  
   - Objects maintain internal state (e.g., bank account balance)  

✅ **Team Projects**:  
   - Clear structure enables parallel development  

⛔ **Avoid For**:  
   - Simple scripts (e.g., one-time file rename)  
   - Pure math computations  
   - Performance-critical low-level code  

---
### *4. Why Use OOP?*  
| Reason          | Explanation                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| *Modularity*  | Break complex systems into manageable, independent objects                  |
| *Reusability* | Inherit/extend existing classes instead of rewriting code                   |
| *Maintainability* | Fix bugs in one class without breaking others                             |
| *Scalability* | Easily add new features by extending classes                                |
| *Real-World Modeling* | Intuitive mapping of business logic to code (e.g., Customer, Order) |

---

### *5. Practical Python Implementation*  
1. Encapsulation
Definition: Bundling data (attributes) and methods that operate on that data into a single unit (class), while controlling access to internal components.

What: Hiding internal state and requiring all interaction through methods.

**When:**
- When processing sensitive customer data
- When managing billing systems
- When implementing secure authentication

**Why:**
- Protects sensitive customer information
- Ensures valid data in billing systems

```
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

```
#### 2. Inheritance
Creating new classes (child) from existing classes (parent), inheriting attributes and methods while allowing specialization. Establishing hierarchical relationships between classes.

#### When:
- When creating different service plans
- When modeling employee hierarchies
- When implementing network device types
#### Why:
- Reduces code duplication for similar services
- Enables polymorphic treatment of services
```
class TelecomService:
    def __init__(self, service_id, base_cost):
        self.service_id = service_id
        self.base_cost = base_cost
    
    def calculate_monthly_charge(self):
        return self.base_cost
    
    def __str__(self):
        return f"Service {self.service_id} (${self.base_cost}/month)"

class MobileDataPlan(TelecomService):
    def __init__(self, service_id, base_cost, data_limit):
        super().__init__(service_id, base_cost)
        self.data_limit = data_limit  # in GB
    
    def calculate_monthly_charge(self):
        return self.base_cost + (self.data_limit * 0.50)  # $0.50/GB
    
    def __str__(self):
        return f"{super().__str__()} - {self.data_limit}GB data"

class VoIPService(TelecomService):
    def __init__(self, service_id, base_cost, included_minutes):
        super().__init__(service_id, base_cost)
        self.included_minutes = included_minutes
    
    def calculate_monthly_charge(self, minutes_used):
        extra = max(0, minutes_used - self.included_minutes) * 0.10
        return self.base_cost + extra

# Usage
basic_plan = TelecomService("BASIC", 15.00)
print(basic_plan)  # Service BASIC ($15.00/month)

data_plan = MobileDataPlan("DATA5", 20.00, 5)
print(data_plan)  # Service DATA5 ($20.00/month) - 5GB data
print(data_plan.calculate_monthly_charge())  # 22.5

voip = VoIPService("VOIP20", 12.00, 200)
print(voip.calculate_monthly_charge(250))  # 12 + (50 * 0.10) = 17.0
```
#### 3. Polymorphism
Ability of different classes to be used interchangeably through a common interface. Different implementations of the same method across classes.

##### When:
- When processing different payment methods
- When generating various types of reports
- When handling multiple network protocols

##### Why:
- Supports standardized interfaces
- Simplifies maintenance of related classes
- Maintains integrity of telecom operations

```
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
```
#### 4. Abstraction
Defining interfaces without implementation, forcing subclasses to implement specific methods. Creating abstract base classes that define required methods.

#### When:
- When defining standard interfaces for network equipment
- When creating mandatory reporting formats
- When establishing service level agreements

#### Why:
- Ensures consistent interfaces
- Prevents incomplete implementations
- Documents required functionality

```
from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass

class Router(NetworkDevice):
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Router {self.ip_address} connected"
    
    def disconnect(self):
        self.connected = False
        return f"Router {self.ip_address} disconnected"
    
    def get_status(self):
        return "Active" if self.connected else "Inactive"

class Switch(NetworkDevice):
    def __init__(self, switch_id):
        self.switch_id = switch_id
        self.ports = {}
    
    def connect(self):
        return f"Switch {self.switch_id} initialized"
    
    def disconnect(self):
        return f"Switch {self.switch_id} powered down"
    
    def get_status(self):
        return f"Switch {self.switch_id} with {len(self.ports)} active ports"

# Usage
router = Router("192.168.1.1")
print(router.connect())  # Router 192.168.1.1 connected
print(router.get_status())  # Active

switch = Switch("SW-01")
print(switch.connect())  # Switch SW-01 initialized
```

---
### *6. OOP vs. Procedural Programming*  
| Scenario            | OOP Approach               | Procedural Approach         |
|---------------------|----------------------------|-----------------------------|
| *Bank Account*    | account.deposit(100)     | deposit(account, 100)     |
| *User Management* | user.update_email()      | update_user_email(user)   |
| *Game Character*  | character.attack()       | attack(character, enemy)  |

*Key Advantage*: OOP groups related data/behavior together, reducing complexity in large systems.
---

### *7. Real-World Use Cases*  
1. *Django Web Framework*: Models (e.g., class User(models.Model))  
2. *PyGame*: Game entities as objects (class Player(pygame.sprite.Sprite))  
3. *GUI Libraries*: Tkinter/PyQt widgets (class App(tk.Tk):)  
4. *Data Science*: Custom data loaders (class Dataset(torch.utils.data.Dataset))

> 💡 *Pro Tip*: Use OOP when your code needs to represent entities with:  
> - Persistent state (attributes)  
> - Complex behaviors (methods)  
> - Relationships (inheritance/composition)

Master OOP to build scalable, maintainable Python applications! 🐍🚀
