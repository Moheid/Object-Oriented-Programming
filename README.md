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
OOP is a programming paradigm that structures code around *objects* - self-contained units that combine:  
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
#### *Class & Object*  
```
python
class Car:  
    # Constructor (initializer)
    def __init__(self, brand, model):  
        # Instance attributes (encapsulation)
        self.brand = brand  
        self.model = model  
        self.__mileage = 0  # Private attribute
    
    # Method (behavior)
    def drive(self, km):  
        self.__mileage += km  
        print(f"Driven {km}km. Total: {self.__mileage}km")
    
    # Getter (abstraction)
    def get_mileage(self):  
        return self.__mileage

# Create object (instantiation)
my_car = Car("Tesla", "Model S")  
my_car.drive(50)  # Output: Driven 50km. Total: 50km
```

#### *Inheritance & Polymorphism*  
```
python
class ElectricCar(Car):  # Inheritance
    def __init__(self, brand, model, battery_size):  
        super().__init__(brand, model)  
        self.battery_size = battery_size
    
    # Polymorphism (method overriding)
    def drive(self, km):  
        super().drive(km)  
        print(f"Battery used: {km / 5}kWh")

# Polymorphic usage
electric_car = ElectricCar("Tesla", "Model 3", 75)  
electric_car.drive(100)  
# Output: 
# Driven 100km. Total: 100km
# Battery used: 20kWh
```

#### *Abstraction*  
```
python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def speak(self):  # Abstract method
        pass

class Dog(Animal):
    def speak(self):  # Concrete implementation
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Polymorphism
        return "Meow!"

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!
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
