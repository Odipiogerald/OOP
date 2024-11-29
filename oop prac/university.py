class University:
    def __init__ (self, name, location, motto, branches = 1):
        self.name = name
        self.location = location
        self.motto = motto   
        self.branches = branches  

    def __str__(self):
        return (f" Name: {self.name} Location: {self.location} Motto: {self.motto} Branches: {self.branches}")   

ucu = University("UCU", "Mukono", "Center of")

print(ucu)