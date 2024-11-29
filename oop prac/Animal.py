#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

#Child Class
class Dog(Animal):
    def speak(self):
        return "Bark"

#Child Class
class Cat(Animal):
    def speak(self):
        print(f" {self.name} Meows")

# Child Class
class Cow(Animal):
    pass
    
tummy = Cat("Tummy")
max = Dog("Max")
cow = Cow("Bihogo")

tummy.speak()
print(max.speak())
print(cow.speak())