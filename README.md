# python
learn python basics

# design pattern in python
 python used [mtv](https://www.geeksforgeeks.org/django-project-mvt-structure/) but node uses mvc folder structure pattern.

 # function annotation

 https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions

 # python basic

 [w3 school python](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)


 ## Python String Method Cheat Sheet:

**General:**

* **len(string):** Returns the length of the string.
* **isdigit():** Returns True if all characters are digits, False otherwise.
* **isalpha():** Returns True if all characters are letters, False otherwise.
* **isalnum():** Returns True if all characters are alphanumeric, False otherwise.
* **islower():** Returns True if all characters are lowercase, False otherwise.
* **isupper():** Returns True if all characters are uppercase, False otherwise.
* **istitle():** Returns True if the string is title-cased, False otherwise.
* **find(substring):** Returns the index of the first occurrence of the substring, -1 if not found.
* **rfind(substring):** Returns the index of the last occurrence of the substring, -1 if not found.
* **count(substring):** Counts the number of occurrences of the substring.
* **startswith(prefix):** Returns True if the string starts with the prefix, False otherwise.
* **endswith(suffix):** Returns True if the string ends with the suffix, False otherwise.

**Case manipulation:**

* **upper():** Converts the string to uppercase.
* **lower():** Converts the string to lowercase.
* **title():** Capitalizes the first letter of each word.
* **swapcase():** Swaps uppercase and lowercase letters.

**String modification:**

* **strip():** Removes leading and trailing whitespace (by default).
* **lstrip():** Removes leading whitespace.
* **rstrip():** Removes trailing whitespace.
* **replace(old, new):** Replaces all occurrences of old with new.
* **split(sep):** Splits the string into a list based on the separator (space by default).
* **join(iterable):** Joins elements of an iterable into a string using the separator.

**Formatting:**

* **f-strings:** Use expressions in curly braces `f"{variable}"` for dynamic formatting.
* **format() method:** Use `.format(variable1, variable2, ...)` for placeholder-based formatting.

**Advanced:**

* **partition(sep):** Splits the string at the first occurrence of the separator and returns a 3-tuple.
* **rpartition(sep):** Splits the string at the last occurrence of the separator and returns a 3-tuple.
* **expandtabs(tabsize):** Expands tabs into spaces based on the given tab size.
* **capitalize():** Capitalizes the first letter of the string.
* **isalnum():** Checks if all characters are alphanumeric (letters, digits, and underscores).
* **isspace():** Checks if all characters are whitespace.

**Remember:** This is just a cheat sheet, not an exhaustive list. Consult the official Python documentation for complete details and more methods: [https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)

# same kind of functionality

While JavaScript allows storing different data types in the same array, its flexibility comes with potential downsides like unexpected behavior in operations and less clarity for complex data. Different languages offer varying approaches to data storage and type handling, each with its advantages and trade-offs. Here are some options with similarities and differences to consider:

**Languages with Similar Flexibility:**

* **Python:** Like JavaScript, Python is dynamically typed and permits mixed data types in arrays. However, Python offers list comprehensions and generator expressions for more concise and type-aware manipulations.
* **Ruby:** Similar to JavaScript and Python, Ruby allows flexible data types in arrays and provides methods like `each` and `map` for iterating and transforming elements effectively.
* **PHP:** While PHP generally enforces data types at runtime, arrays can hold diverse values. Careful type checking is recommended to avoid unintended results.

**Languages with Stricter Typing:**

* **Java:** Java enforces data types at compile time, requiring you to declare array types upfront. This ensures type safety but might seem less flexible than JavaScript initially.
* **C#:** C# also implements strong typing for arrays, promoting clarity and preventing common errors. Similar to Java, it might require more upfront planning.
* **TypeScript:** As a typed superset of JavaScript, TypeScript allows optional type annotations to enhance clarity and static type checking while maintaining JavaScript's core flexibility.

**Other Data Structures:**

* **Dictionaries (or Maps):** These data structures map keys to values, allowing different data types for both keys and values. They offer greater flexibility and organization compared to arrays when dealing with heterogeneous data.
* **Structs (or Records):** In languages like C# and Swift, structs or records define named fields with specific data types, providing type safety and structured data representation.

Choosing the best language depends on your specific needs and priorities. Consider:

* **Type safety:** If data integrity and error prevention are crucial, a strongly typed language like Java or C# might be more suitable.
* **Flexibility:** If you need maximum flexibility and dynamic data handling, JavaScript or Python could be good choices.
* **Data complexity:** For complex data with structured relationships, dictionaries or structs might offer better organization and clarity.

# dictionary 

Python provides various methods for dictionaries, including:

- `dict.items()`: Returns a view of dictionary key-value pairs as tuples.
- `dict.keys()`: Returns a view of dictionary keys.
- `dict.values()`: Returns a view of dictionary values.
- `dict.get(key, default)`: Returns the value for the specified key, or a default value if the key is not found.
- `dict.pop(key)`: Removes the item with the specified key and returns its value.
- `dict.update(other_dict)`: Updates the dictionary with the key-value pairs from another dictionary.

# sep () and end()

1. **`sep` Parameter:**
   - The `sep` parameter is used to specify the separator between the values you want to print.
   - By default, `sep` is set to a space character (' ').

   Example:

   ```python
   print("apple", "orange", "banana", sep=', ')  # Output: apple, orange, banana
   ```

2. **`end` Parameter:**
   - The `end` parameter is used to specify what character or string should be printed at the end of the `print` statement.
   - By default, `end` is set to the newline character ('\n').

   Example:

   ```python
   print("Hello", end='!')  # Output: Hello!
   ```
# double underscores (__)
 It is around an identifier are used for special methods or attributes. These are often called "magic methods" or "dunder" (double underscore) methods. One such commonly used special method is `__init__`, which is the constructor method.

Here are a few examples of commonly used dunder methods:

1. `__init__`: The constructor method, called when an object is created.
2. `__str__`: Used to define the "informal" or printable string representation of an object. It is called by the built-in `str()` function and the `print()` function.
3. `__repr__`: Used to define the "official" string representation of an object. It is called by the built-in `repr()` function and is intended to be unambiguous.
4. `__len__`: Used to define the behavior of the `len()` function for an object.
5. `__getitem__` and `__setitem__`: Used for getting and setting values using square bracket notation (`obj[key]`).
6. `__call__`: Allows an object to be called like a function.

Here's an example demonstrating `__str__` and `__repr__`:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

# Example usage
obj = MyClass(42)

print(str(obj))    # Output: MyClass instance with value: 42
print(repr(obj))   # Output: MyClass(42)
```

more explaination about __str__

Certainly! Let's consider a real-life analogy using a `Person` class. Without a custom `__str__` method, the default behavior provides less informative output, but with a custom `__str__`, we can make the output more meaningful.

**Without Custom `__str__`:**
```python
class PersonWithoutStr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance without a custom __str__
person = PersonWithoutStr(name="John", age=25)

# Without a custom __str__, you get a less informative output
print(person)
# Output: <__main__.PersonWithoutStr object at 0x...>
```

In this case, the default `__str__` inherited from the base `object` class provides an output that includes the object's memory address but lacks human-readable information.

**With Custom `__str__`:**
```python
class PersonWithStr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Creating an instance with a custom __str__
person = PersonWithStr(name="John", age=25)

# With a custom __str__, you get a more meaningful output
print(person)
# Output: John, 25 years old
```

In this example, the `PersonWithStr` class has a custom `__str__` method. When you print or convert an instance of this class to a string, the custom `__str__` method is called, providing a more human-readable representation of the `Person` object.

So, customizing `__str__` allows you to control how your objects are presented in a way that is more meaningful and useful for your specific class and its instances.

# class decorators method

In Python, decorators are a powerful feature that allows you to modify or extend the behavior of functions or methods. There are several built-in decorators in Python, and here are examples of a few of them:

1. **`@staticmethod`:**
   - Used to define a static method within a class.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

result = MathOperations.add(3, 4)
print(result)  # Output: 7
```

2. **`@classmethod`:**
   - Used to define a class method within a class.

```python
class MyClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

result = MyClass.class_method()
print(result)  # Output: 10
```

3. **`@property`:**
   - Used to define a getter method for a class attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

circle = Circle(5)
print(circle.radius)  # Output: 5
```

4. **`@classmethod` and `@property` together:**
   - Combining `@classmethod` and `@property` to create a read-only class property.

```python
class MyClass:
    _class_variable = 42

    @classmethod
    @property
    def class_variable(cls):
        return cls._class_variable

result = MyClass.class_variable
print(result)  # Output: 42
```

These are just a few examples of built-in decorators in Python. Decorators provide a clean and concise way to extend or modify the behavior of functions or methods, and you can also create your own decorators for custom behavior.

# decorator

a decorator is a special type of function that is used to modify the behavior of another function or method. Decorators are a powerful and flexible feature of the language, allowing you to wrap or modify the functionality of functions dynamically.

Here's a basic example of a decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
```

In this example, `my_decorator` is a decorator function. The `@my_decorator` syntax is a shorthand way of applying the decorator to the `say_hello` function. When you call `say_hello()`, it is actually calling the wrapped version of the function defined by the `wrapper` function within the decorator. This allows you to execute code before and after the original function's execution.

Decorators are commonly used for tasks such as logging, timing, access control, and more. Python provides a convenient syntax with the `@decorator` syntax, but decorators themselves are just functions that take a function as an argument and return a new function.

It's important to note that decorators can be used with any callable object (functions, methods, or even class methods) and can be stacked to apply multiple transformations. They contribute to Python's support for metaprogramming, enabling dynamic modifications to the behavior of functions and methods.

# reduce() function

Certainly! The **`reduce()`** function in Python is a powerful tool for cumulative calculations on sequences of values. Let's explore its details and use cases:

1. **Definition and Syntax**:
   - The `reduce()` function is part of the `functools` module.
   - It applies a binary function cumulatively to the elements of an iterable, progressively reducing them to a single result.
   - The syntax is as follows:
     ```
     reduce(function, sequence)
     ```
     - `function`: A binary function that takes two arguments and returns a single value.
     - `sequence`: An iterable (e.g., list, tuple, etc.) containing the elements to be processed.

2. **Working Principle**:
   - The `reduce()` function works as follows:
     1. Initially, it picks the first two elements from the sequence and applies the function to obtain a result.
     2. Next, it applies the same function to the previously obtained result and the next element in the sequence.
     3. This process continues until no more elements are left in the container.
     4. The final result is returned.

3. **Example: Sum and Maximum**:
   ```python
   import functools

   numbers = [1, 3, 5, 6, 2]

   # Calculate the sum of the list elements
   sum_result = functools.reduce(lambda a, b: a + b, numbers)
   print("Sum of the list elements:", sum_result)

   # Find the maximum element in the list
   max_result = functools.reduce(lambda a, b: a if a > b else b, numbers)
   print("Maximum element in the list:", max_result)
   ```
   Output:
   ```
   Sum of the list elements: 17
   Maximum element in the list: 6
   ```

4. **Using Operator Functions**:
   - We can also combine `reduce()` with operator functions for readability:
     ```python
     import functools
     import operator

     # Calculate sum and product using operator functions
     sum_result = functools.reduce(operator.add, numbers)
     product_result = functools.reduce(operator.mul, numbers)

     print("Sum of the list elements:", sum_result)
     print("Product of list elements:", product_result)
     ```

5. **Difference Between `reduce()` and `accumulate()`**:
   - Both `reduce()` and `accumulate()` calculate the summation of sequence elements.
   - Key differences:
     - `reduce()` stores intermediate results and returns the final summation value.
     - `accumulate()` returns an iterator containing intermediate results.
     - The last value in the iterator from `accumulate()` is the summation value of the list.

6. **Three-Parameter Usage**:
   - The `reduce()` function can take three parameters:
     - If the second argument is an empty sequence, the third argument serves as the default value.

In summary, `reduce()` is a versatile function for cumulative calculations, making it useful in various scenarios! 🌟🐍

For more details, you can refer to the [GeeksforGeeks article](https://www.geeksforgeeks.org/reduce-in-python/) ¹.

Source: Conversation with Bing, 20/3/2024
(1) reduce() in Python - GeeksforGeeks. https://www.geeksforgeeks.org/reduce-in-python/.
(2) Reduce in Python : All You Need To Know. https://datatrained.com/post/reduce-in-python/.
(3) Python reduce() Function - Python Geeks. https://pythongeeks.org/python-reduce-function/.
(4) Python reduce() Function: A Comprehensive Guide [2022]. https://www.codingem.com/how-python-reduce-function-works/.
(5) Python's reduce(): From Functional to Pythonic Style. https://realpython.com/python-reduce-function/.



# multithreading

Multithreading allows a program to execute multiple threads concurrently within the same process. Each thread represents a separate flow of execution that can perform tasks independently. In Python, the `threading` module provides support for working with threads.

Here's how multithreading works and how the main thread creates and interacts with subthreads:

1. **Main Thread**: When a Python program starts, it automatically creates a main thread, which is the initial thread of execution. This main thread is responsible for executing the program's main code.

2. **Creating Subthreads**: To create additional threads, the main thread can instantiate `threading.Thread` objects and specify a target function that the new thread will execute. This target function represents the code to be executed in the subthread.

   ```python
   import threading

   # Define a function to be executed by the subthread
   def subthread_task():
       print("Subthread is executing")

   # Create a new subthread
   subthread = threading.Thread(target=subthread_task)

   # Start the subthread
   subthread.start()
   ```

3. **Starting Subthreads**: After creating a subthread, the main thread calls the `start()` method on the subthread object. This initiates the execution of the target function in the subthread. The main thread and the subthread will then execute concurrently.

4. **Joining Threads**: The main thread can use the `join()` method on a subthread object to wait for the subthread to complete its execution. When the `join()` method is called, the main thread will pause its execution and wait until the subthread finishes before continuing.

   ```python
   # Wait for the subthread to finish
   subthread.join()
   ```

   The `join()` method ensures that the main thread waits for the subthread to complete before proceeding with further instructions. This helps in synchronizing the execution of threads and ensures that the main thread does not terminate before the subthreads have finished their tasks.

5. **Impact of Join on the Default Thread**: When the main thread calls `join()` on a subthread, it effectively waits for that subthread to complete. This means that the main thread will be blocked until the subthread finishes its execution. Once the subthread completes and `join()` returns, the main thread can resume its execution.

In summary, the main thread creates and starts subthreads to execute concurrent tasks. The `join()` method allows the main thread to synchronize with subthreads by waiting for them to complete before proceeding further. This coordination ensures proper execution order and synchronization between threads.


# important points

* by deafult python and ruby support negating indexing.
* [python does not have switch-case condition like other programming language](https://www.geeksforgeeks.org/switch-case-in-python-replacement/)
* in python we can only create a single constructor. java support multi constructor with diffrent args. but not python.
* [read this to make not accessible function,variable outside of class](https://www.geeksforgeeks.org/private-variables-python/)

- [eval funtion](https://www.geeksforgeeks.org/eval-in-python/)

- [constructor](https://www.shiksha.com/online-courses/articles/constructors-in-python-definition-types-and-rules/#:~:text=Constructors%20in%20Python%20is%20a,value%20to%20the%20object's%20members.)

- [access modifier](https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/)

- [polymorphisim](https://www.geeksforgeeks.org/dunder-magic-methods-python/)

- [operators precedence](https://www.geeksforgeeks.org/precedence-and-associativity-of-operators-in-python/)

- [2d list](https://snakify.org/en/lessons/two_dimensional_lists_arrays/)

- [asynchronus programming in python](https://www.geeksforgeeks.org/asyncio-in-python/)

- [destructor](https://www.geeksforgeeks.org/destructors-in-python/)

- [pass statement](https://www.w3schools.com/python/ref_keyword_pass.asp#:~:text=Python%20pass%20Statement&text=The%20pass%20statement%20is%20used,definitions%2C%20or%20in%20if%20statements.)

- [abstracte class](https://www.geeksforgeeks.org/data-abstraction-in-python/)

- [__name__](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)

- [getter & setter](https://www.geeksforgeeks.org/getter-and-setter-in-python/)



In Python, whether an object is passed "by value" or "by reference" depends on whether the object is mutable or immutable:

- **Mutable objects (pass by reference-like behavior):**
  - Lists
  - Dictionaries
  - Sets
  - Custom objects/classes (if they are designed to be mutable)

- **Immutable objects (pass by value-like behavior):**
  - Integers
  - Floats
  - Strings
  - Tuples
  - Frozensets
  - Custom objects/classes (if they are designed to be immutable)

Understanding the mutability of objects is crucial in Python to grasp how modifications to objects may or may not affect the original variables.