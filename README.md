# Programming with Python Professional Certificate

This is my notes and process for completing the LinkedIn Learning learning path [OpenEDG Python Institute: Programming with Python Professional Certificate](https://www.linkedin.com/learning/paths/openedg-python-institute-programming-with-python-professional-certificate). There will be sections for each course in the learning path and an overall review once I have completed everything.

## Python Essential Training
This is my repository for the LinkedIn Learning course `Python Essential Training`. The full course is available from [LinkedIn Learning][lil-course-url]. I will be committing my projects and code samples from the course to this repository.

![Python Essential Training][lil-thumbnail-url] 

Python is one of the most commonly used dynamic languages for many large organizations, including Google, Yahoo, and IBM. Supported on all major operating systems, it comes pre-installed on Macs, as well as most Linux and Unix-based systems. In this course, senior software engineer Ryan Mitchell guides you through all the essentials of learning and using Python. Learn how computers think, as well as how to install Python, pip, and Jupyter Notebook and the basics of writing a program. Explore variables and types, operators, functions, classes, objects, and more. Go over basic data types like ints and floats, Booleans, and strings. Deep dive into basic data structures, control flow, functions, classes, and objects. Find out how to handle errors and exceptions, as well as threads and processes. Plus, discover how to work with different types of files in Python, pass command-line arguments to your Python script, and create modules and packages.

### Instructor

Ryan Mitchell 
                            
Senior Software Engineer

[lil-course-url]: https://www.linkedin.com/learning/](https://www.linkedin.com/learning/python-essential-training-18764650/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/C4E0DAQHBQo3TSa3IUg/learning-public-crop_675_1200/0/1674513192001?e=2147483647&v=beta&t=YWS_o8SlM4I6YEzJwQnAIP8Q0kfvzX3QbqA7Avrg7K8

### CHAPTER 1 - Gearing Up for Python
This was just an introductory and setup chapter. Walked through what Python is and how to install Python, Pip, and Jupyter.

Was then given a breif over view of Jupyter and Python and given stepwise instructions on how to create a `hello world` program

### CHAPTER 2 - Quickstart
This chapter covered the fundamentals of coding in Python. It covered topics of variables, data structures, and operators. It then when over the basic of control flow using if/else statements and loops. The section ended with a very quick over view of fuinctions and classes that will be build on in later chapters.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_02) was to write a robust function to calculate factorials without using the build in `math.factorial()` function. 

### CHAPTER 3 - Basic Data Types
This chapter covered the basic data structures of Python. This included `int`, `float`, `bool`, `string`, and `byte`.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_03) for this chapter was to create a function that convereted hex numbers to decimal. The goal was to only support at most a 3 digit hex number, but I wrote my code in a way to be robust enough to handle any length. It includes checks to make sure the input is a valid hex number before attemtping to conver to decimal.

### CHAPTER 4 - Basic Data Structures
This chatper is an intro to the basic data structures in Python

* **List** - A `list` is a mutable and ordered sequence of elements in Python. Items can be added and removed from the list as needed.
* **Tuple** - A `tuple` is ordered but immutable. Once the tuple has been created it cannot be changed. If you want to add elements you can convert it to a `list` and manipulate the `list`, but would need to create a new `tuple` to convert it back to a `tuple`
* **Set** - A `set` is an unordered and mutable collection of items. The order in a `set` is not guarunteed and there cannot be repeated elements in the `set`
* **Dictionary** - A `dictionary` stores data in key-value pairs. Dictionaries are mutable and can store other data types or structures.

The chapter concluded with going over the basics of list and dictionary comprehensions.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_04) for this chapter was to encode and decode ASCII art. Given a string, the `encode(string)` function returned a list of tuples using run-length encoding. Given a list of tuples, the `decode(list)` function returned a string that could then be printed out.

### CHAPTER 5 - Control Flow
This chapter focused on the basics of control flow types. Control flows you to execute certain parts of the code and skip others or repeate the same secion of code multiple times.

* **if/elif/else** - Allows you to execute certain sections of code if specific criteria are met using boolean logic to determine if that section should be executed. Only one `if` is allowed, followed by any number of `elif` statements, and finally an optional `else`. Only one of the if/elif/else statements will be executed, the first one that meets the criteria. Order does matter
* **for loop** - Repeat a piece of code a prescribed number of times. This is used when you need to do the same thing multiple times and more cleanly allows this to happen without writing the same code over and over. A `for` loop is used to iterate over a sequence of objects
* **while loop** - A while loop, like a for loop, will repeat the same code multiple times. It will iterate until a condition is met. It is used when you don't know how many iterations you need in advance.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_05) for this chapter was to create a function to find prime numbers. The goal was to make the process more efficient but storing a list of known primes so the program could compare only against prime numbers up to the square root of the potential primee instead of dividing by every number up to the square root.

### CHATPER 6 - Functions
This chapter was all about functions. Topics discussed were the purpose and intent of functions, how to define and write them, variables and defining the scope of variables, and finally using functions as variables.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_06) was to calculate the square of a number using the triangle sum of the number. The square of a number is equal to `triangle(num) + triangle(num -1)`. This was a quick and straigh forward project focused on declaring functions and calling them recursively as needed.

### CHAPTER 7 - Classes and Objects
This chapter was all about classes and an introduction to object oriented programming. Topics discussed were what are classes, static and instance methods, and inheritance.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_07) was to complete a `Triangle` class that was a child of a predefined `Shape` class. The goal was to have it print a triangle shape with the character #.

### CHAPTER 8 - Errors
This chapter covered `Errors` and `Exceptions`. In Python `Errors` and `Excpetions` are essentially the same thing. The course went over what `Errors` and `Exceptions` are. Then we covered different ways to handle the exceptions. It was noted to put the most generic `Exception` last so that if a specific `Exception` is raised it will be caught by the code to send the correct message to users. Finally, we learned about creating custom `Exceptions`.

The [coding project](https://github.com/saxton-chris/LinkedInPythonCert/tree/main/my_work/Chapter_08) was to create a custom `Exception` to handle arguments that aren't integers. It uses a decorator to check that all parameters are integers. If any parameter isn't an integer then it raises a `NotIntArgumentException`.

### CHAPTER 9

### CHAPTER 10

### CHAPTER 11
