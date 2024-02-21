# python
learn python basics

# design pattern in python
 python used [mtv](https://www.geeksforgeeks.org/django-project-mvt-structure/) but node uses mvc folder structure pattern.

 # Django

 [w3school](https://www.w3schools.com/django/django_admin_create_user.php)

 # object create in django

 [one method needs to be save using save() function other method directly save it to db](https://stackoverflow.com/questions/26672077/django-model-vs-model-objects-create)

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



# important points

* by deafult python and ruby support negating indexing.
* [python does not have switch-case condition like other programming language](https://www.geeksforgeeks.org/switch-case-in-python-replacement/)

