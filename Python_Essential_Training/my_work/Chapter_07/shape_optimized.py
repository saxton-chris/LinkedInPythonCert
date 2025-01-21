# Base class for shapes
class Shape:
    def __init__(self, width=5, height=5, print_char='#'):
        """
        Initialize a shape with specified width, height, and character to print.
        :param width: Width of the shape
        :param height: Height of the shape
        :param print_char: Character used to print the shape
        """
        self.width = width
        self.height = height
        self.print_char = print_char

    def printRow(self, i):
        """
        Abstract method to print a row of the shape. Must be implemented by subclasses.
        :param i: Row index
        """
        raise NotImplementedError("Subclasses must implement this method")

    def print(self):
        """
        Print the entire shape row by row.
        """
        for i in range(self.height):
            self.printRow(i)


# Derived class representing a square
class Square(Shape):
    def printRow(self, i):
        """
        Print a single row of the square.
        :param i: Row index (ignored, since all rows are the same for squares)
        """
        print(self.print_char * self.width)


# Derived class representing a triangle
class Triangle(Shape):
    def printRow(self, i):
        """
        Print a single row of the triangle.
        :param i: Row index, determines the number of characters in the row
        """
        print(self.print_char * (i + 1))


# Example usage
if __name__ == "__main__":
    # Create and print a default triangle
    t = Triangle()
    t.print()

    print("\nCustom Square:")
    # Create and print a custom square
    s = Square(width=7, height=7, print_char='*')
    s.print()

    print("\nCustom Triangle:")
    # Create and print a custom triangle
    t_custom = Triangle(width=1, height=4, print_char='@')
    t_custom.print()
