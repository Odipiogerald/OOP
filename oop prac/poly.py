# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# It provides a way to perform a single action in different ways.
# Method Overriding occurs when a child class provides a specific implementation of a method already defined in its parent class.

# Example 1: Animal Sounds
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

# Example usage of polymorphism
def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
make_sound(dog)  # Output: Bark!
make_sound(cat)  # Output: Meow!

# Example 2: Shape Areas
class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def area(self):
        print("Area = π * r^2")

class Rectangle(Shape):
    def area(self):
        print("Area = length * breadth")

# Example usage
shapes = [Circle(), Rectangle()]
for shape in shapes:
    shape.area()

# Example 3: Vehicle Start
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key...")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a button...")

# Example usage
vehicles = [Car(), Bike()]
for vehicle in vehicles:
    vehicle.start()

# Example 4: Devices and Operation
class Device:
    def operate(self):
        print("Device is operating...")

class Phone(Device):
    def operate(self):
        print("Phone is making a call...")

class Tablet(Device):
    def operate(self):
        print("Tablet is playing a video...")

# Example usage
devices = [Phone(), Tablet()]
for device in devices:
    device.operate()

# Example 5: Payment Methods
class Payment:
    def pay(self):
        print("Processing payment...")

class CreditCard(Payment):
    def pay(self):
        print("Paying with a credit card...")

class PayPal(Payment):
    def pay(self):
        print("Paying with PayPal...")

# Example usage
payments = [CreditCard(), PayPal()]
for payment in payments:
    payment.pay()

# Example 6: Employees Working
class Employee:
    def work(self):
        print("Employee is working...")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team...")

class Developer(Employee):
    def work(self):
        print("Developer is writing code...")

# Example usage
employees = [Manager(), Developer()]
for employee in employees:
    employee.work()

# Example 7: Musical Instruments
class Instrument:
    def play(self):
        print("Playing an instrument...")

class Guitar(Instrument):
    def play(self):
        print("Playing the guitar...")

class Piano(Instrument):
    def play(self):
        print("Playing the piano...")

# Example usage
instruments = [Guitar(), Piano()]
for instrument in instruments:
    instrument.play()

# Example 8: Transportation Modes
class Transportation:
    def move(self):
        print("Transportation is moving...")

class Car(Transportation):
    def move(self):
        print("Car is driving on the road...")

class Airplane(Transportation):
    def move(self):
        print("Airplane is flying in the sky...")

# Example usage
transportations = [Car(), Airplane()]
for transportation in transportations:
    transportation.move()

# Example 9: Animal Communication
class Animal:
    def communicate(self):
        print("Animal is communicating...")

class Bird(Animal):
    def communicate(self):
        print("Bird is chirping...")

class Fish(Animal):
    def communicate(self):
        print("Fish is making bubbles...")

# Example usage
animals = [Bird(), Fish()]
for animal in animals:
    animal.communicate()

# Example 10: Appliances Usage
class Appliance:
    def use(self):
        print("Using an appliance...")

class Blender(Appliance):
    def use(self):
        print("Blending ingredients...")

class Microwave(Appliance):
    def use(self):
        print("Heating food...")

# Example usage
appliances = [Blender(), Microwave()]
for appliance in appliances:
    appliance.use()
