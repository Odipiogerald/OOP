# Additional fun examples for Week 2: Constructors and Instance Variables

# Example 5: Library System
class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

book = Book("1984", "George Orwell", 1949)
book.display_info()


# Example 6: Fitness Tracker
class FitnessTracker:
    def _init_(self, user, steps, calories_burned):
        self.user = user
        self.steps = steps
        self.calories_burned = calories_burned

    def display_activity(self):
        print(f"{self.user} walked {self.steps} steps and burned {self.calories_burned} calories.")

tracker = FitnessTracker("John", 5000, 300)
tracker.display_activity()


# Example 7: Music Playlist
class Song:
    def _init_(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in minutes

    def display_song(self):
        print(f"{self.title} by {self.artist}, Duration: {self.duration} mins")

song = Song("Shape of You", "Ed Sheeran", 4)
song.display_song()


# Example 8: Taxi Booking System
class Taxi:
    def _init_(self, driver_name, car_model):
        self.driver_name = driver_name
        self.car_model = car_model

    def start_ride(self):
        print(f"{self.driver_name} is driving the {self.car_model}. Your ride has started!")

taxi = Taxi("James", "Toyota Prius")
taxi.start_ride()


# Example 9: Coffee Machine
class CoffeeMachine:
    def _init_(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity  # in cups

    def brew_coffee(self):
        print(f"{self.brand} is brewing {self.capacity} cups of coffee.")

machine = CoffeeMachine("Nespresso", 2)
machine.brew_coffee()


# Example 10: Hotel Room Booking
class HotelRoom:
    def _init_(self, room_number, guest_name, nights_stayed):
        self.room_number = room_number
        self.guest_name = guest_name
        self.nights_stayed = nights_stayed

    def display_booking(self):
        print(f"Room {self.room_number} is booked for {self.guest_name} for {self.nights_stayed} nights.")

room = HotelRoom(101, "Alice", 3)
room.display_booking()


# Example 11: Video Game Character
class GameCharacter:
    def _init_(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def display_stats(self):
        print(f"{self.name} - Level: {self.level}, Health: {self.health}")

character = GameCharacter("Warrior", 5, 100)
character.display_stats()


# Example 12: Movie Theater
class MovieTheater:
    def _init_(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.available_seats = available_seats

    def display_info(self):
        print(f"Movie: {self.movie_title}, Available seats: {self.available_seats}")

theater = MovieTheater("Avengers: Endgame", 50)
theater.display_info()


# Saving all the code examples to a single .py file
week2_fun_examples_v2_path = "/mnt/data/Week2_Fun_Examples_v2.py"
with open(week2_fun_examples_v2_path, "w") as file:
    file.write("""
# Example 1: Student Enrollment System
class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = Student("Alice", 14, "8th Grade")
student1.display_info()


# Example 2: Online Shopping Cart
class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append((item, price))

    def show_cart(self):
        if not self.items:
            print("Your cart is empty!")
        else:
            print("Items in your cart:")
            for item, price in self.items:
                print(f"{item}: ${price}")

cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Headphones", 199.99)
cart.show_cart()


# Example 3: Pet Adoption Center
class Pet:
    def _init_(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type

    def display_info(self):
        print(f"{self.pet_type} Name: {self.name}")

pet1 = Pet("Buddy", "Dog")
pet2 = Pet("Whiskers", "Cat")
pet1.display_info()
pet2.display_info()


# Example 4: Recipe Book
class Recipe:
    def _init_(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def show_recipe(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

recipe1 = Recipe("Pancakes", ["Flour", "Milk", "Eggs", "Sugar"])
recipe1.show_recipe()


# Example 5: Library System
class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"'{self.title}' by {self.author} ({self.year})")

book = Book("1984", "George Orwell", 1949)
book.display_info()


# Example 6: Fitness Tracker
class FitnessTracker:
    def _init_(self, user, steps, calories_burned):
        self.user = user
        self.steps = steps
        self.calories_burned = calories_burned

    def display_activity(self):
        print(f"{self.user} walked {self.steps} steps and burned {self.calories_burned} calories.")

tracker = FitnessTracker("John", 5000, 300)
tracker.display_activity()


# Example 7: Music Playlist
class Song:
    def _init_(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def display_song(self):
        print(f"{self.title} by {self.artist}, Duration: {self.duration} mins")

song = Song("Shape of You", "Ed Sheeran", 4)
song.display_song()


# Example 8: Taxi Booking System
class Taxi:
    def _init_(self, driver_name, car_model):
        self.driver_name = driver_name
        self.car_model = car_model

    def start_ride(self):
        print(f"{self.driver_name} is driving the {self.car_model}. Your ride has started!")

taxi = Taxi("James", "Toyota Prius")
taxi.start_ride()


# Example 9: Coffee Machine
class CoffeeMachine:
    def _init_(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity

    def brew_coffee(self):
        print(f"{self.brand} is brewing {self.capacity} cups of coffee.")

machine = CoffeeMachine("Nespresso", 2)
machine.brew_coffee()


# Example 10: Hotel Room Booking
class HotelRoom:
    def _init_(self, room_number, guest_name, nights_stayed):
        self.room_number = room_number
        self.guest_name = guest_name
        self.nights_stayed = nights_stayed

    def display_booking(self):
        print(f"Room {self.room_number} is booked for {self.guest_name} for {self.nights_stayed} nights.")

room = HotelRoom(101, "Alice", 3)
room.display_booking()


# Example 11: Video Game Character
class GameCharacter:
    def _init_(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def display_stats(self):
        print(f"{self.name} - Level: {self.level}, Health: {self.health}")

character = GameCharacter("Warrior", 5, 100)
character.display_stats()


# Example 12: Movie Theater
class MovieTheater:
    def _init_(self, movie_title, available_seats):
        self.movie_title = movie_title
        self.available_seats = available_seats

    def display_info(self):
        print(f"Movie: {self.movie_title}, Available seats: {self.available_seats}")

theater = MovieTheater("Avengers: Endgame", 50)
theater.display_info()
""")

