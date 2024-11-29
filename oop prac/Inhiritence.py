class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, accessNumber):
        super().__init__(name, age)
        self.accessNumber = accessNumber
        self.name = name
        self.age = age
    
    def display_info(self):
        super().display_info()
        print(f"Access Number: {self.accessNumber}")