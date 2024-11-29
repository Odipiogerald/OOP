class Shape:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides

    def area(self):
        print(f"{type}'s Area is ")

class Square(Shape):
    def __init__(self, type, sides, length):
        super().__init__(type, sides)
        self.length = length

    def area(self):
        print(f"Area = {self.length ** 2}")

square = Square("Square", 4, 5)
square.area()

