class Dog:
    def __init__(self, name, age, colour): # The self parameter
        # e.g. dog 1 and 2 is automatically passed to the dog class
        # so we know which dog we are talking about
        self.name = name # name attribute for dog
        self.age = age # age attribute
        self.colour = colour # colour attribute

    def print_details(self): # crete a method to display the imformations
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def age_days(self):
        return f"{self.name} is {self.age * 365} days old"

# These are all different dog objects
dog1 = Dog("Spot", 7, "black")
dog2 = Dog("Jazz", 5, "white")

# calling the print details method for each dog obejct
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
print(Dog.age_days((dog1)))
print(Dog.age_days((dog2)))
