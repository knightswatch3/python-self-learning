Scope (LEGB rule), Lambda Functions, *args and **kwargs, Recursion
Practice using *args and **kwargs to create flexible functions (e.g., a custom print function).

================================================================================
SCOPE (LEGB RULE) - Comprehensive Guide
================================================================================

1. WHAT IS SCOPE?
   - Scope determines where variables can be accessed in your code
   - Different scopes have different variable visibility
   - Python follows LEGB rule to find variables

2. LEGB RULE (Order of Variable Lookup):
   L - Local: Variables defined inside a function
   E - Enclosing: Variables in enclosing (outer) functions (nested functions)
   G - Global: Variables defined at module level (top level of file)
   B - Built-in: Python's built-in functions and variables (like print, len, etc.)
   
   Python searches in this order when looking for a variable name.

3. LOCAL SCOPE:
   - Variables defined inside a function
   - Only accessible within that function
   - Created when function is called, destroyed when function ends
   
   Example:
   def my_function():
       x = 10  # Local variable
       print(x)  # Works: 10
   
   my_function()
   print(x)  # Error: NameError (x doesn't exist outside function)

4. GLOBAL SCOPE:
   - Variables defined at module level (top of file, outside functions)
   - Accessible from anywhere in the file
   - Can be read from inside functions
   
   Example:
   x = 10  # Global variable
   
   def my_function():
       print(x)  # Works: reads global x
   
   my_function()  # Output: 10

5. MODIFYING GLOBAL VARIABLES:
   - To modify a global variable inside a function, use 'global' keyword
   - Without 'global', assignment creates a local variable
   
   Example:
   x = 10  # Global
   
   def modify():
       global x  # Declare we want to modify global x
       x = 20    # Now modifies global x
   
   modify()
   print(x)  # 20 (global x changed)
   
   Without global keyword:
   def modify_wrong():
       x = 20  # Creates LOCAL variable, doesn't modify global
   
   modify_wrong()
   print(x)  # Still 10 (global unchanged)

6. ENCLOSING SCOPE (Nested Functions):
   - Variables in outer (enclosing) function
   - Accessible in inner function
   - Use 'nonlocal' to modify enclosing scope variables
   
   Example:
   def outer():
       x = 10  # Enclosing scope
       
       def inner():
           print(x)  # Can read enclosing x
       
       inner()  # Output: 10
   
   outer()

7. NONLOCAL KEYWORD:
   - Used to modify variables in enclosing (non-global) scope
   - Similar to 'global' but for nested functions
   
   Example:
   def outer():
       x = 10  # Enclosing scope
       
       def inner():
           nonlocal x  # Modify enclosing x
           x = 20
       
       inner()
       print(x)  # 20 (enclosing x modified)

8. BUILT-IN SCOPE:
   - Python's built-in names (print, len, range, etc.)
   - Always available
   - Lowest priority in LEGB lookup
   
   Example:
   def my_function():
       print("Hello")  # Uses built-in print function

9. SCOPE RESOLUTION ORDER:
   When Python encounters a variable name:
   1. Check Local scope first
   2. If not found, check Enclosing scope
   3. If not found, check Global scope
   4. If not found, check Built-in scope
   5. If still not found, raise NameError

================================================================================
LAMBDA FUNCTIONS - Comprehensive Guide
================================================================================

1. WHAT ARE LAMBDA FUNCTIONS?
   - Anonymous functions (functions without a name)
   - Created with 'lambda' keyword
   - Can have any number of arguments but only one expression
   - Often used for short, simple operations

2. BASIC SYNTAX:
   lambda arguments: expression
   
   Example:
   square = lambda x: x ** 2
   print(square(5))  # 25
   
   Equivalent regular function:
   def square(x):
       return x ** 2

3. LAMBDA VS REGULAR FUNCTION:
   Regular Function:
   def add(x, y):
       return x + y
   
   Lambda Function:
   add = lambda x, y: x + y
   
   - Lambda is more concise
   - Lambda is anonymous (no name needed)
   - Lambda can only have one expression

4. LAMBDA WITH MULTIPLE ARGUMENTS:
   Example:
   multiply = lambda x, y, z: x * y * z
   print(multiply(2, 3, 4))  # 24

5. LAMBDA WITH NO ARGUMENTS:
   Example:
   get_pi = lambda: 3.14159
   print(get_pi())  # 3.14159

6. LAMBDA WITH CONDITIONAL EXPRESSIONS:
   Example:
   max_value = lambda x, y: x if x > y else y
   print(max_value(5, 3))  # 5
   
   is_even = lambda x: True if x % 2 == 0 else False
   print(is_even(4))  # True

7. COMMON USE CASES:
   
   With map():
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x ** 2, numbers))
   # [1, 4, 9, 16, 25]
   
   With filter():
   numbers = [1, 2, 3, 4, 5]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   # [2, 4]
   
   With sorted():
   people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
   sorted_by_age = sorted(people, key=lambda x: x[1])
   # [("Bob", 20), ("Alice", 25), ("Charlie", 30)]

8. WHEN TO USE LAMBDA:
   - Short, simple operations
   - Functions used only once
   - As arguments to other functions (map, filter, sorted)
   - When you need a quick function without defining it

9. WHEN NOT TO USE LAMBDA:
   - Complex logic (use regular function)
   - Multiple statements (lambda only allows one expression)
   - When you need to reuse the function multiple times
   - When readability is more important than brevity

================================================================================
*ARGS AND **KWARGS - Comprehensive Guide
================================================================================

1. WHAT IS *ARGS?
   - Allows function to accept any number of positional arguments
   - *args collects extra positional arguments into a tuple
   - 'args' is just a convention (you can use any name after *)
   
   Syntax:
   def function(*args):
       # args is a tuple of all positional arguments

2. BASIC *ARGS EXAMPLE:
   def add_all(*args):
       return sum(args)
   
   print(add_all(1, 2, 3))        # 6
   print(add_all(1, 2, 3, 4, 5))  # 15
   print(add_all())               # 0 (empty tuple)
   
   - *args collects all arguments into a tuple
   - Can access like: args[0], args[1], etc.

3. *ARGS WITH REGULAR PARAMETERS:
   - Regular parameters must come before *args
   
   Example:
   def greet(greeting, *names):
       for name in names:
           print(f"{greeting}, {name}!")
   
   greet("Hello", "Alice", "Bob", "Charlie")
   # greeting = "Hello"
   # names = ("Alice", "Bob", "Charlie")

4. WHAT IS **KWARGS?
   - Allows function to accept any number of keyword arguments
   - **kwargs collects extra keyword arguments into a dictionary
   - 'kwargs' is just a convention (you can use any name after **)
   
   Syntax:
   def function(**kwargs):
       # kwargs is a dictionary of all keyword arguments

5. BASIC **KWARGS EXAMPLE:
   def print_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")
   
   print_info(name="Alice", age=25, city="NYC")
   # name: Alice
   # age: 25
   # city: NYC
   
   - **kwargs collects all keyword arguments into a dictionary
   - Can access like: kwargs['name'], kwargs.get('age'), etc.

6. COMBINING *ARGS AND **KWARGS:
   - Order must be: regular params, *args, **kwargs
   
   Example:
   def function(a, b, *args, **kwargs):
       print(f"a={a}, b={b}")
       print(f"args={args}")
       print(f"kwargs={kwargs}")
   
   function(1, 2, 3, 4, 5, x=10, y=20)
   # a=1, b=2
   # args=(3, 4, 5)
   # kwargs={'x': 10, 'y': 20}

7. UNPACKING WITH * AND **:
   - Can unpack lists/tuples with *
   - Can unpack dictionaries with **
   
   Example:
   def add(a, b, c):
       return a + b + c
   
   numbers = [1, 2, 3]
   result = add(*numbers)  # Unpacks: add(1, 2, 3)
   
   def greet(name, age):
       print(f"{name} is {age}")
   
   info = {"name": "Alice", "age": 25}
   greet(**info)  # Unpacks: greet(name="Alice", age=25)

8. PRACTICAL USE CASES:
   
   Flexible print function:
   def custom_print(*args, sep=" ", end="\n"):
       print(*args, sep=sep, end=end)
   
   Custom logger:
   def log(message, **metadata):
       print(f"LOG: {message}")
       for key, value in metadata.items():
           print(f"  {key}: {value}")

9. COMMON PATTERNS:
   - *args for variable number of arguments
   - **kwargs for configuration options
   - Combining both for maximum flexibility
   - Unpacking when calling functions

================================================================================
RECURSION - Comprehensive Guide
================================================================================

1. WHAT IS RECURSION?
   - Function that calls itself
   - Breaks problem into smaller subproblems
   - Must have a base case (stopping condition)
   - Without base case, recursion continues infinitely

2. BASIC RECURSION EXAMPLE (Factorial):
   def factorial(n):
       # Base case
       if n == 0 or n == 1:
           return 1
       # Recursive case
       return n * factorial(n - 1)
   
   print(factorial(5))  # 5 * 4 * 3 * 2 * 1 = 120
   
   How it works:
   factorial(5) = 5 * factorial(4)
   factorial(4) = 4 * factorial(3)
   factorial(3) = 3 * factorial(2)
   factorial(2) = 2 * factorial(1)
   factorial(1) = 1  (base case)

3. RECURSION STRUCTURE:
   def recursive_function(parameter):
       # Base case (stopping condition)
       if base_condition:
           return base_value
       
       # Recursive case (calls itself)
       return recursive_function(modified_parameter)

4. COMMON RECURSION EXAMPLES:
   
   Fibonacci:
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   
   Sum of list:
   def sum_list(numbers):
       if not numbers:
           return 0
       return numbers[0] + sum_list(numbers[1:])
   
   Count items:
   def count_items(items):
       if not items:
           return 0
       return 1 + count_items(items[1:])

5. RECURSION VS ITERATION:
   Recursion:
   - More elegant for some problems
   - Can be harder to understand
   - May use more memory (call stack)
   
   Iteration:
   - Usually more efficient
   - Easier to understand for simple cases
   - Uses less memory

6. WHEN TO USE RECURSION:
   - Problems naturally recursive (trees, graphs)
   - Code is cleaner and more readable
   - Problem can be broken into similar subproblems
   - Depth is limited (not too deep)

7. WHEN NOT TO USE RECURSION:
   - Very deep recursion (may cause stack overflow)
   - Performance is critical
   - Simple iteration is clearer
   - Memory is limited

8. RECURSION BEST PRACTICES:
   - Always have a base case
   - Make sure base case is reachable
   - Ensure recursive call moves toward base case
   - Consider stack overflow for deep recursion

9. TAIL RECURSION:
   - Recursive call is the last operation
   - Some languages optimize this, Python doesn't
   - Still useful for clarity

10. COMMON RECURSION PATTERNS:
    - Divide and conquer
    - Tree/graph traversal
    - Backtracking algorithms
    - Dynamic programming

