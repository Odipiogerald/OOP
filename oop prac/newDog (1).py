class Dog:
    legs = 4
    def __init__(self, name, theColor):
        self.name = name
        self.color = theColor

rafi = Dog("Rafiki", "Brown")
rafi.age = 5
rafi.behave = "Annoying"
max = Dog("Max", "Black")

print(rafi.legs)
print(max.legs)