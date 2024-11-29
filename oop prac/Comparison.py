# Procedural approach: Using individual variables and a function
# In this approach, data and behavior are separate, without the structure provided by a class.

# Defining variables for employee attributes
base_salary = 30000
overtime = 10
rate = 20

# Defining a function to calculate the wage
def get_wage(base_salary, overtime, rate):
    # Function calculates the total wage based on the provided arguments
    return base_salary + (overtime * rate)

# Calling the function and printing the result
# Here, we pass the individual data points to the function to perform the calculation.
print(get_wage(base_salary, overtime, rate))  # Output: 30200


# Defining a basic employee class to represent the concept of an employee.
# This approach encapsulates the data (attributes) and behavior (methods) related to an employee in a single unit (class).

class Employee:
    def __init__(self, base_salary, overtime, rate):
        # These are instance variables, specific to each Employee object.
        # Encapsulation ensures that these variables are associated only with instances of this class.
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate

    # Method to calculate the total wage
    # This method uses the object's own attributes (base_salary, overtime, rate) to perform a calculation.
    def get_wage(self):
        # Calculating the total wage based on base salary and overtime pay rate.
        # The method acts on the object's own data, showing encapsulation in action.
        return self.base_salary + (self.overtime * self.rate)

# Creating an instance (object) of the Employee class.
employee = Employee(base_salary=30000, overtime=10, rate=20)

# Calling the get_wage method to calculate the employee's wage.
# This demonstrates how methods work with the instance data to provide specific behavior.
print(employee.get_wage())  # Output: 30200
