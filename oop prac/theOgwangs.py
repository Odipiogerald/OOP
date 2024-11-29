class Father:
    behavior = "Confident"
    def __init__(self, name):
        self.name = name

class Daughter(Father):
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

MrOgwang = Father("Ogwang")
Joanna = Daughter(19, "Female")


print(Joanna.behavior)
    