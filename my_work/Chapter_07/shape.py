# Challenge for Chapter 7 of the Python Essentials Training Course on LinkedIn Learning
# This chapter was an overview of classes and inheritance. 
# The task was to write the `printRow` function for the Triangle class that is a child
# of the Shape class. I chose to print a basic right triangle

# Base class for shapes
class Shape:
    # Default dimensions and character for printing the shape
    width = 5
    height = 5
    printChar = '#'

    # Method to print a single row of the shape
    # To be implemented by child classes that inherit from Shape
    def printRow(self, i):
        raise NotImplementedError("Will be implemented by children extending this class")

    # Method to print the entire shape row by row
    def print(self):
        # Iterates through each row (from 0 to height - 1)
        for i in range(self.height):
            self.printRow(i)  # Delegates the row printing to the specific shape's implementation


# Derived class representing a square
class Square(Shape):
    # Overrides the printRow method to print a full row of characters
    def printRow(self, i):
        # Prints a row with 'width' number of characters
        print(self.printChar * self.width)


# Derived class representing a triangle
class Triangle(Shape):
    # Overrides the printRow method to print a row of increasing length
    def printRow(self, i):
        # Prints a row with (i + 1) number of characters, where i is the current row index
        print(self.printChar * (i + 1))


# This demonstrates the use of the Triangle class
t = Triangle()
t.print()  # Prints a triangle shape using the default settings
