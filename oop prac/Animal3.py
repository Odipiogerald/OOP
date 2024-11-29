class Animal:
    def __init__(self, name):
        self.name = name

    def display_Info(self):
        print(f"{self.name}")
    
    def make_sound(self):
        print(f"{self.name} cries")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound
    
    def make_sound(self):
        super().display_Info()
        print(f"{self.sound}")

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def make_sound(self):
        super().display_Info()
        print(f"{self.sound}")

elephant = Animal("elephant")
elephant.make_sound()

popi = Dog("popi", "Woof")
popi.make_sound()

    