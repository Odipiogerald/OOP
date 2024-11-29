# Encapsulation in Python
# Encapsulation is the concept of bundling data (attributes) and methods within a single unit (class),
# and restricting access to some attributes to protect the data from unintended modification.

class Payment:
    # Constructor to initialize the final price
    def __init__(self, final_price):
        # Making 'final_price' a private attribute by prefixing it with '__'
        # This prevents direct access to it from outside the class
        self.__final_price = final_price

    # Public method to retrieve the final price
    def get_final_price(self):
        # This method provides controlled access to the private attribute
        return self.__final_price

    # Public method to set the final price with a discount
    def set_final_price(self, discount):
        
        # Modify the final price based on the discount, using a private method
        self.__final_price = self.__final_price - self.__calculate_discount(discount)

    # Private method to calculate the discount
    def __calculate_discount(self, discount):
        # This method is private and can only be accessed within the class
        # It calculates the discount based on a percentage of the final price
        return self.__final_price * (discount / 100)

# Creating an instance of Payment with an initial price of 10
book = Payment(10)

# Attempting to calculate a discount directly (this would cause an error if tried directly outside the class)
# book.__calculate_discount(50)  # Uncommenting this will raise an AttributeError

# Setting a new final price with a 10% discount
book.set_final_price(10)

# Retrieving and printing the final price
# This will show the final price after the discount is applied
print(book.get_final_price())  # Output depends on the initial price and discount
