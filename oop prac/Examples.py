# Example 1: Basic Single Inheritance
# In this example, we create a parent class `Person` and a child class `Student` that inherits from it.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class constructor using super()
        self.student_id = student_id

    def display_info(self):
        super().display_info()  # Call parent class method
        print(f"Student ID: {self.student_id}")

# Example usage
student = Student("Alice", 20, "S12345")
student.display_info()

# Example 2: Overriding a Parent Method in Child Class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark!")  # Overriding the parent method

# Example usage
dog = Dog()
dog.make_sound()  # Will output "Bark!" instead of the parent method

# Example 3: Using the super() Function to Call Parent Methods
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the parent constructor
        self.doors = doors

    def display_info(self):
        super().display_info()  # Call the parent method
        print(f"Number of doors: {self.doors}")

# Example usage
car = Car("Toyota", "Corolla", 4)
car.display_info()

# Example 4: Multiple Inheritance
# A class can inherit from more than one parent class
class A:
    def feature_one(self):
        print("Feature 1")

class B:
    def feature_two(self):
        print("Feature 2")

# Child class inheriting from both A and B
class C(A, B):
    def feature_three(self):
        print("Feature 3")

# Example usage
obj = C()
obj.feature_one()  # Inherited from class A
obj.feature_two()  # Inherited from class B
obj.feature_three()  # Defined in class C

# Example 5: Hierarchical Inheritance
# Hierarchical inheritance means multiple child classes inherit from the same parent class.
class Parent:
    def common_feature(self):
        print("This is a common feature")

class ChildOne(Parent):
    def unique_feature_one(self):
        print("This is a unique feature of Child One")

class ChildTwo(Parent):
    def unique_feature_two(self):
        print("This is a unique feature of Child Two")

# Example usage
child_one = ChildOne()
child_two = ChildTwo()
child_one.common_feature()  # Inherited from Parent
child_two.common_feature()  # Inherited from Parent
child_one.unique_feature_one()
child_two.unique_feature_two()

# Example 6: Multilevel Inheritance
# Multilevel inheritance is where a child class inherits from another child class.
class Grandparent:
    def feature_grandparent(self):
        print("Feature of the grandparent")

class Parent(Grandparent):
    def feature_parent(self):
        print("Feature of the parent")

class Child(Parent):
    def feature_child(self):
        print("Feature of the child")

# Example usage
child = Child()
child.feature_grandparent()  # Inherited from Grandparent
child.feature_parent()  # Inherited from Parent
child.feature_child()  # Defined in Child

# Example 7: Diamond Problem in Multiple Inheritance
# Python resolves the diamond problem using the Method Resolution Order (MRO).
class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")

class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C):
    pass

# Example usage
d = D()
d.show()  # MRO will call the show method of class B because B is listed first in inheritance

# Example 8: super() in Multiple Inheritance
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Bird(Animal):
    def sound(self):
        super().sound()  # Call the parent method
        print("Bird chirps")

class Parrot(Bird):
    def sound(self):
        super().sound()  # Call the parent method
        print("Parrot talks")

# Example usage
parrot = Parrot()
parrot.sound()

# Example 9: Constructor Overriding
class Shape:
    def __init__(self, color):
        self.color = color

    def display(self):
        print(f"Shape color is {self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)  # Call parent constructor
        self.radius = radius

    def display(self):
        super().display()  # Call parent display
        print(f"Circle radius is {self.radius}")

# Example usage
circle = Circle("Red", 5)
circle.display()

# Example 10: Combining Inheritance and Polymorphism
class Employee:
    def work(self):
        print("Employee works")

class Manager(Employee):
    def work(self):
        print("Manager oversees")

class Developer(Employee):
    def work(self):
        print("Developer codes")

def assign_work(employee):
    employee.work()  # Polymorphism in action: Calls the appropriate method depending on the object type

# Example usage
manager = Manager()
developer = Developer()
assign_work(manager)  # Output: Manager oversees
assign_work(developer)  # Output: Developer codes
