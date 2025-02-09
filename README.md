# Programming with Python Professional Certificate

This is my notes and process for completing the LinkedIn Learning learning path [OpenEDG Python Institute: Programming with Python Professional Certificate](https://www.linkedin.com/learning/paths/openedg-python-institute-programming-with-python-professional-certificate). There will be sections for each course in the learning path and an overall review once I have completed everything.

## Table of Contents
* [Python Essential Training](#python-essential-training)
    * [CHAPTER 1 - Gearing Up for Python](#chapter-1---gearing-up-for-python)
    * [CHAPTER 2 - Quickstart](#chapter-2---quickstart)
    * [CHAPTER 3 - Basic Data Types](#chapter-3---basic-data-types)
    * [CHAPTER 4 - Basic Data Structures](#chapter-4---basic-data-structures)
    * [CHAPTER 5 - Control Flow](#chapter-5---control-flow)
    * [CHAPTER 6 - Functions](#chapter-6---functions)
    * [CHAPTER 7 - Classes and Object](#chapter-7---classes-and-objects)
    * [CHAPTER 8 - Errors](#chapter-8---errors)
    * [CHAPTER 9 - Threads and Processes](#chapter-9---threads-and-processes)
    * [CHAPTER 10 - Working with Files](#chapter-10---working-with-files)
    * [CHAPTER 11 - Packaging Python](#chapter-11---packaging-python)
* [Python Object-Oriented Progamming](#python-object-oriented-programming)
    * [INTRODUCTION](#introduction)
    * [CHAPTER 1 - Object-Oriented Programming](#chapter-1---object-oriented-python)
    * [CHAPTER 2 - Inheritance and Composition](#chapter-2---inheritance-and-compositions)
    * [CHAPTER 3 - "Magic" Object Methods](#chapter-3---magic-object-method)
    * [CHAPTER 4 - Data Classes](#chapter-4---data-classes)
* [Level Up: Python](#level-up-python)
    * [CHALLENGE 1 - Prime Facotorization](#challenge-1---prime-factorization)
    * [CHALLENGE 2 - Find Palindromes](#challenge-2---find-palindromes)
    * [CHALLENGE 3 - Sort a String of Words](#challenge-3---sort-a-string-of-words)
    * [CHALLENGE 4 - Find All Items in List](#challenge-4---find-all-items-in-list)
    * [CHALLENGE 5 - Waiting Game](#challenge-5---waiting-game)
    * [CHALLENGE 6 - Save a Dictionary](#challenge-6---save-a-dictionary)

## Python Essential Training <a name="essentials"></a>
This is my repository for the LinkedIn Learning course `Python Essential Training`. The full course is available from [LinkedIn Learning][lil-course-url]. I will be committing my projects and code samples from the course to this repository.

![Python Essential Training][lil-thumbnail-url] 

Python is one of the most commonly used dynamic languages for many large organizations, including Google, Yahoo, and IBM. Supported on all major operating systems, it comes pre-installed on Macs, as well as most Linux and Unix-based systems. In this course, senior software engineer Ryan Mitchell guides you through all the essentials of learning and using Python. Learn how computers think, as well as how to install Python, pip, and Jupyter Notebook and the basics of writing a program. Explore variables and types, operators, functions, classes, objects, and more. Go over basic data types like ints and floats, Booleans, and strings. Deep dive into basic data structures, control flow, functions, classes, and objects. Find out how to handle errors and exceptions, as well as threads and processes. Plus, discover how to work with different types of files in Python, pass command-line arguments to your Python script, and create modules and packages.

### Instructor

Ryan Mitchell 
                            
Senior Software Engineer

[lil-course-url]: https://www.linkedin.com/learning/](https://www.linkedin.com/learning/python-essential-training-18764650/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/C4E0DAQHBQo3TSa3IUg/learning-public-crop_675_1200/0/1674513192001?e=2147483647&v=beta&t=YWS_o8SlM4I6YEzJwQnAIP8Q0kfvzX3QbqA7Avrg7K8

### CHAPTER 1 - Gearing Up for Python <a name="es_chapter1"></a>
This was just an introductory and setup chapter. Walked through what Python is and how to install Python, Pip, and Jupyter.

Was then given a breif over view of Jupyter and Python and given stepwise instructions on how to create a `hello world` program

### CHAPTER 2 - Quickstart
This chapter covered the fundamentals of coding in Python. It covered topics of variables, data structures, and operators. It then when over the basic of control flow using if/else statements and loops. The section ended with a very quick over view of fuinctions and classes that will be build on in later chapters.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_02) was to write a robust function to calculate factorials without using the build in `math.factorial()` function. 

### CHAPTER 3 - Basic Data Types
This chapter covered the basic data structures of Python. This included `int`, `float`, `bool`, `string`, and `byte`.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_03) for this chapter was to create a function that convereted hex numbers to decimal. The goal was to only support at most a 3 digit hex number, but I wrote my code in a way to be robust enough to handle any length. It includes checks to make sure the input is a valid hex number before attemtping to conver to decimal.

### CHAPTER 4 - Basic Data Structures
This chatper is an intro to the basic data structures in Python

* **List** - A `list` is a mutable and ordered sequence of elements in Python. Items can be added and removed from the list as needed.
* **Tuple** - A `tuple` is ordered but immutable. Once the tuple has been created it cannot be changed. If you want to add elements you can convert it to a `list` and manipulate the `list`, but would need to create a new `tuple` to convert it back to a `tuple`
* **Set** - A `set` is an unordered and mutable collection of items. The order in a `set` is not guarunteed and there cannot be repeated elements in the `set`
* **Dictionary** - A `dictionary` stores data in key-value pairs. Dictionaries are mutable and can store other data types or structures.

The chapter concluded with going over the basics of list and dictionary comprehensions.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_04) for this chapter was to encode and decode ASCII art. Given a string, the `encode(string)` function returned a list of tuples using run-length encoding. Given a list of tuples, the `decode(list)` function returned a string that could then be printed out.

### CHAPTER 5 - Control Flow
This chapter focused on the basics of control flow types. Control flows you to execute certain parts of the code and skip others or repeate the same secion of code multiple times.

* **if/elif/else** - Allows you to execute certain sections of code if specific criteria are met using boolean logic to determine if that section should be executed. Only one `if` is allowed, followed by any number of `elif` statements, and finally an optional `else`. Only one of the if/elif/else statements will be executed, the first one that meets the criteria. Order does matter
* **for loop** - Repeat a piece of code a prescribed number of times. This is used when you need to do the same thing multiple times and more cleanly allows this to happen without writing the same code over and over. A `for` loop is used to iterate over a sequence of objects
* **while loop** - A while loop, like a for loop, will repeat the same code multiple times. It will iterate until a condition is met. It is used when you don't know how many iterations you need in advance.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_05) for this chapter was to create a function to find prime numbers. The goal was to make the process more efficient but storing a list of known primes so the program could compare only against prime numbers up to the square root of the potential primee instead of dividing by every number up to the square root.

### CHAPTER 6 - Functions
This chapter was all about functions. Topics discussed were the purpose and intent of functions, how to define and write them, variables and defining the scope of variables, and finally using functions as variables.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_06) was to calculate the square of a number using the triangle sum of the number. The square of a number is equal to `triangle(num) + triangle(num -1)`. This was a quick and straigh forward project focused on declaring functions and calling them recursively as needed.

### CHAPTER 7 - Classes and Objects
This chapter was all about classes and an introduction to object oriented programming. Topics discussed were what are classes, static and instance methods, and inheritance.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_07) was to complete a `Triangle` class that was a child of a predefined `Shape` class. The goal was to have it print a triangle shape with the character #.

### CHAPTER 8 - Errors
This chapter covered `Errors` and `Exceptions`. In Python `Errors` and `Excpetions` are essentially the same thing. The course went over what `Errors` and `Exceptions` are. Then we covered different ways to handle the exceptions. It was noted to put the most generic `Exception` last so that if a specific `Exception` is raised it will be caught by the code to send the correct message to users. Finally, we learned about creating custom `Exceptions`.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_08) was to create a custom `Exception` to handle arguments that aren't integers. It uses a decorator to check that all parameters are integers. If any parameter isn't an integer then it raises a `NotIntArgumentException`.

### CHAPTER 9 - Threads and Processes
This chapter went over the basics of threads and processes. The instructor went over the usage of threads and process, as well as how to import the correct packages. Threads within the same process have access to the same memory while two processes don't share memory. Both can be used to speed up run time, but in some cases threads may not be able to run in parallel.

There was no coding challenge for this chapter.

### CHAPTER 10 - Working with Files
This chapter was about reading and writing files. I learned how to open a file and different modes it can be opened in. She then went over the process of writing to a file and how to append to the end of a file vs. overwritng a file. She then coverd reading from a file and how you can use that data.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Essential_Training/my_work/Chapter_10) was to compress some ASCII art and store it in a file. Then write a second function to decompress and print out the original art. I compressed using using a `bytearray` to make it as small as possible. The ASCII art was compressed to about 25% of its original size.

### CHAPTER 11 - Packaging Python
The final chapter covered modules and packages in Python. A package is a group of modules within a common directory. To indicate that a directory is a package you must inlude a `__init__.py` file. You can use `from <module_name> import ...` in a file to import the module you want. You can import the whole module or just the pieces you need.

***

## Python Object-Oriented Programming <a name="py_oop"></a>
This is the repository for the LinkedIn Learning course Python Object-Oriented Programming. The full course is available from [LinkedIn Learning][lil-course-url].

The object-oriented programming (OOP) features in Python make it easier to build programs of increasing complexity and modularity. In this course with instructor Joe Marini, learn how to apply core OOP principles to build programs that are extensible and efficient. Joe starts with the basics of defining and using classes and objects. Then he moves into more advanced features like abstract base classes and how to implement interfaces. He also details some of the more unique features of Python, like magic class methods to make your classes integrate tightly with the Python language and data classes to dramatically reduce the amount of boilerplate code needed to build data-centric objects.

### Instructions
This repository contains two folders for the contents of the course:
- *Finished*: The fully finished versions of the code examples. Intended to be used as a reference and for help with troubleshooting your own code
- *Start*: The starting point for each exercise. This is the code that you will use in the course to build towards the finished examples.

### Installing
1. To use these exercise files locally on your computer, you must have the following installed:
    - [Python][python-download]
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.

### Codespace
This course has been set up to use Codespaces, an online development environment that requires no installation. Fork a copy of the repository in your own Github account and use a Codespace to work entirely online.


### Instructor

Joe Marini 
                            
Senior Director of Product and Engineering

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/joe-marini).

[lil-course-url]: https://www.linkedin.com/learning/python-object-oriented-programming-22888296?dApp=59033956&leis=LAA

### INTRODUCTION
Just a quick introduction section. It gave recommended course to take to become familiar with Python and OOP. It then had a quick tutorial on how to set up CodeSpaces on GitHub

### CHAPTER 1 - Object-Oriented Python
This chapter goes over the basics of OOP. Python does not requier the use of objects and classes, but complexity of code leads to using OOP to make things easier to read. OOP allows for modular program and isolates different parts of the program from each other.

Some of the key terms that were reviewed are
* *Class* - This is essentially a blue print used for creating objects of a certain type
* *Methods* - These are functions within a class
* *Attributes* - These are variables within a class
* *Object* - A particular instance of a class
* *Inheritance* - This is how a class draws some functionality from a parent class
* *Composition* - Building complex objects out of other objects

After this high-level overview the instructor walked us through some practice creating classes and instances of those classes. We also learned how to check the type of an object of if that object is an instance of a particular class. Finally, it was wrapped up by going over the differences between instance, class, and static methods and attributes.

The final task was a [coding challenge](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Object-Oriented_Programming/My_Work/Chapter_01) implementing a `Stock` class that stores some basic information on stocks and contains a singular method, `get_description()` and prints out all the stored attributes in a formatted string.

### CHAPTER 2 - Inheritance and Composition
This chapter was all about inheritance and composition in Python. The first thing that was dicussed was basic inheritance and nested inheritance. We create a `Book` class that inherited from a `Publication` class, as well as `Magazine` and `Newpaper` classes which inherited from `Periodical` which in turn inherited from `Publication`. From there we learned about abstraction and using the `abc` package to mark classes as abstract classes anduse `@abstractmethod` to declare abstrac methods in the class. This also tied into a following section on interfaces and how they can be used among many different types of class whether they are related or not. The chapter also went over the concept of multiple inheritance and why order of classes matter when listing which classes a new class inherits from. The final topic was on composition. This is the concept of passing in instances of one class into another class. An example is having a `Book` class that is passed an `Author` class because a book **has** an author. The major distiction between the two is that a for inheritance it is an *is* relationship (a `Book` *is* a `Publication`) and composition is an *has* relationship (a `Book` *has* an `Author`).

The [coding challenge](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Object-Oriented_Programming/My_Work/Chapter_02) for this chapter was to expand on the stock example from chatper 1. We wrote an abstract `Asset` class that both `Stock` and `Bond` inherited from. Since both have a `price` the `Asset` class set that for both. Then both implemented the abstract method `get_description()` to print out a description of each.

### CHAPTER 3 - "Magic" Object Method
The instructor defines "magic" object methods as built in functions for Python that a class can override to make the class easier to work with. the first functions we looked at were the `__str__` and `__repr__` functions. These allow for two different ways to represent the class. The `str()` function is more commonly used for friendlier and user readable strings where the `repr()` function is used to provide information to developers. The latter is commonly used in debugging code. The next section was learnig the use of the `__eq__`(==), `__ge__`(>=), and `__lt__`(<) functions. These are used to compare two objects of the same type together and can be used to sort the objects as well. Then we moved on to `__getattribute__`, `__setattr__`, and `__getattr__`. These control how developer can get or set attributes for the class. The `__getattr__` is used if the attribute doesn't exist or the `__getattribute__` function raises an exception. The developer needs to becareful when implementing these functions to avoid an infinite recursive loop. Finally, we looked at, and implemented the `__call__` function. This allows developer to directly call the object as a function instead of having to use the dot notation.

The [coding challenge](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Object-Oriented_Programming/My_Work/Chapter_03) was further extending the previous `Asset`, `Stock`, and `Bond` classes. The task was to implement the `__str__` function, which as added as an `abstractmethod` to the `Asset` class, to allow the user to cleanly print the object. And then implement the `__lt__` method to allow for sorting a list of objects.

### CHAPTER 4 - Data Classes
The last chatpter was on data classes, as the header says. I learned how to import the dataclasses packaage and the benefits that it can bring by implementing certain instance methods be default like, `__init__`, `__eq__`, and `__repr__`. I then learned how to set defaults for instance attributes and make the class immutable.

The [coding challenge](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Python_Object-Oriented_Programming/My_Work/Chapter_04) continued to add on to the `Asset`, `Stock`, and `Bond` classes from before by making them `dataclasses`. 

***

## Level Up: Python 
This is the repository for the LinkedIn Learning course Level Up: Python. The full course is available from [LinkedIn Learning][lil-course-url].

Want to test your Python skills? These concise challenges let you stretch your brain and test your talents. Instructor Barron Stone shares over a dozen Python challenges, as well as his own solutions to each problem—the majority of which are less than two dozen lines of code. The challenges include finding prime factors, sorting strings, scheduling a function, solving a sudoku, and more. You can tackle each problem using the tools in the Python standard library, or opt for the library of your choice. And since each challenge is self-contained, you can complete the course in any order—and at your own pace. Tune in to get the hands-on practice you need to level up your skills.<br><br>This course is integrated with GitHub Codespaces, an instant cloud developer environment that offers all the functionality of your favorite IDE without the need for any local machine setup. With GitHub Codespaces, you can get hands-on practice from any machine, at any time—all while using a tool that you’ll likely encounter in the workplace. <br><br>Each installment of the <em>Level Up</em> series offers at least 15 bite-sized opportunities to practice programming at various levels of difficulty, so you can challenge yourself and reinforce what you’ve learned.

### Instructor

Barron Stone

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/barron-stone).

[lil-course-url]: https://www.linkedin.com/learning/level-up-python

### CHALLENGE 1 - Prime Factorization
The first coding challenge was to create a function to find the (prime factors)[https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Level_Up_Python/my_work/01_Find_Prime_Factors] of a given number. My solution for this started by trying to divide by 2 as that is the lowest prime number. Once I divided by 2 as many times as I could, then I tried divding by 3, as that is the next prime number. From there, I incrimented the divisor by 2 as I only needed to test odd numbers, up to the square root of the most current value of the reduced number. I also included a couple of safety checks before trying to find prime factors. If the input parameter was not a integer I return a warning message letting the user know that an integer is required. Also, if the number is less than 2, then I am returning an empty list as the number can't have any prime factors. The final check was to see is `num > 1` after the loop finishes executing. If so, that number is prime and must be added to the list. This captures the cases where the input number was prime as well as making sure the final prime factor is added to the list

### CHALLENGE 2 - Find Palindromes
The second coding challenge was to determine if a string is a [palindrome]((prime factors)[https://github.com/saxton-chris/LinkedInPythonCert/tree/main/Level_Up_Python/my_work/02_palindrome] ) or not. For this challenge, I repleaced all non-alpha characters with an empty string and then converted them all to lowercase for comparison. The next step was to assign the string to a new variable in reverse order. The return whether the two strings were equal or not.

After building and testing my function, I tried running it through ChatGPT to see if it could be optimized. The result it gave used the `join()` function instead of regex and did the comparison in one step instead of using two separate variables. The new version ran slightly slower in my benchmark testing but the code is more concise and easier to read.

### CHALLENGE 3 - Sort A String of Words

### CHALLENGE 4 - Find All Items in List

### CHALLENGE 5 - Waiting Game

### CHALLENGE 6 - Save a Dictionary
