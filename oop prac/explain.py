# Explanation of Encapsulation and Abstraction in Python

# Encapsulation:
# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP).
# It is the practice of bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class.
# By using encapsulation, we can control access to data by making attributes private and exposing them only through methods.
# This helps to protect the integrity of the data, preventing unintended modification from outside the class.

# Example of Encapsulation:

class Car:
    def __init__(self, make, model, year):
        self.make = make  # public attribute
        self._model = model  # protected attribute
        self.__year = year  # private attribute

    # Public method to access the private attribute
    def get_year(self):
        return self.__year

    # Public method to modify the private attribute
    def set_year(self, year):
        if year > 1886:  # Basic validation; the first car was made in 1886
            self.__year = year
        else:
            print("Invalid year")

# Creating an instance of the Car class
car = Car("Toyota", "Corolla", 2020)

print(car.make)         # Accessing public attribute: Output -> Toyota
print(car._model)       # Accessing protected attribute (not recommended): Output -> Corolla
print(car.get_year())   # Accessing private attribute through public method: Output -> 2020

car.set_year(2022)      # Modifying private attribute through public method
print(car.get_year())   # Output -> 2022

car.set_year(1800)      # Trying to set an invalid year: Output -> Invalid year
print(car.get_year())   # Output remains -> 2022

# In this example, 'make' is public, '_model' is protected (conventionally for internal use),
# and '__year' is private. Encapsulation allows the 'Car' class to control how 'year' is accessed and modified.

# -------------------------------------------------------------

# Abstraction:
# Abstraction is another core principle of OOP.
# It focuses on exposing only the necessary details and hiding the internal implementation of a class.
# With abstraction, we can create a simplified model of a complex system by only presenting relevant attributes and methods.
# This helps users of a class understand and interact with it without needing to know its complex inner workings.

# Example of Abstraction with an Abstract Base Class

from abc import ABC, abstractmethod  # Importing ABC module to create abstract classes

class Payment(ABC):  # Abstract class
    @abstractmethod
    def make_payment(self, amount):
        pass  # Abstract method - does not have any implementation in the abstract class

# Subclass that implements the abstract method
class CreditCardPayment(Payment): 
    def make_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

# Another subclass that implements the abstract method
class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

# Usage
payment1 = CreditCardPayment()
payment1.make_payment(100)  # Output -> Processing credit card payment of 100

payment2 = PayPalPayment()
payment2.make_payment(150)  # Output -> Processing PayPal payment of 150

# In this example, 'Payment' is an abstract class with an abstract method 'make_payment'.
# The 'CreditCardPayment' and 'PayPalPayment' classes implement the abstract method and provide specific functionality.
# This is an example of abstraction, as the user interacts with the 'Payment' class interface without needing to know
# the details of how the payment is processed for different payment types.
