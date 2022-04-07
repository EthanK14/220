from random import randint


class Die:
    # constructor all constructors have the same name in python and init means initialize
    # every constructor will always have the parameter is self
    def __init__(self, num_sides):
        # to create instance variables you use self.<variable>
        self.sides = num_sides
        self.value = 1  # every die created value = 1

    # methods
    def get_value(self):
        return self.value  # returns the value variable from the die object

    def roll(self):
        new_value = randint(1, self.sides)  # gets the number of sides and then gets a random # between it and 1
        self.value = new_value  # sets the new value equal to the value in the constructor
