# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(f"The type of b1 is {type(b1)}")
print(f"The type of b2 is {type(n1)}")

# TODO: compare two types together
print(f"b1 and b2 are the same type (checked by using the type() function): {type(b1) == type(b2)}")
print(f"b1 and n2 are the same type (checked by using the type() function): {type(b1) == type(n2)}")

# TODO: use isinstance to compare a specific instance to a known type
print(f"b1 is a book(checked using the isinstance() function): {isinstance(b1, Book)}")
print(f"n1 is a newspaper(checked using the isinstance() function): {isinstance(n1, Newspaper)}")
print(f"n2 is a book(checked using the isinstance() function): {isinstance(n2, Book)}")
print(f"n2 is an object(checked using the isinstance() function): {isinstance(n2, object)}")