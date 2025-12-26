Functions: Defining and Calling (def), Positional/Keyword/Default Parameters, Return Statements, Multiple Returns
Write functions for the previous calculator and list operations.

================================================================================
FUNCTIONS - Comprehensive Guide
================================================================================

1. WHAT ARE FUNCTIONS?
   - Reusable blocks of code that perform specific tasks
   - Help avoid code repetition (DRY principle: Don't Repeat Yourself)
   - Make code more organized and readable
   - Can take inputs (parameters) and return outputs
   - Example: Instead of writing the same calculation 10 times, write it once in a function

2. DEFINING A FUNCTION:
   Syntax:
   def function_name():
       # code block
       pass
   
   - def: Keyword to define a function
   - function_name: Name of the function (follows variable naming rules)
   - (): Parentheses for parameters (can be empty)
   - :: Colon indicates start of function body
   - Indented code: Function body (must be indented)

3. BASIC FUNCTION EXAMPLE:
   def greet():
       print("Hello, World!")
   
   - Function is defined but not executed yet
   - Code inside function only runs when function is called

4. CALLING A FUNCTION:
   Syntax: function_name()
   
   Example:
   def greet():
       print("Hello, World!")
   
   greet()  # Calling the function
   # Output: Hello, World!
   
   - Function must be defined before it's called
   - Use parentheses () to call the function
   - Can call a function multiple times

5. FUNCTION WITH PARAMETERS:
   Parameters are variables that receive values when function is called
   
   Syntax:
   def function_name(parameter1, parameter2):
       # code using parameter1 and parameter2
   
   Example:
   def greet(name):
       print(f"Hello, {name}!")
   
   greet("Alice")  # name = "Alice"
   # Output: Hello, Alice!
   
   - Parameters are placeholders for values
   - Values passed when calling are called "arguments"

6. POSITIONAL PARAMETERS:
   - Parameters are matched by position (order matters)
   - First argument goes to first parameter, second to second, etc.
   
   Example:
   def add(x, y):
       return x + y
   
   result = add(5, 3)  # x=5, y=3
   # result = 8
   
   - Position matters: add(5, 3) is different from add(3, 5)

7. KEYWORD ARGUMENTS:
   - Specify parameter names when calling function
   - Order doesn't matter when using keyword arguments
   
   Example:
   def greet(first_name, last_name):
       print(f"Hello, {first_name} {last_name}!")
   
   # Positional arguments
   greet("John", "Doe")  # first_name="John", last_name="Doe"
   
   # Keyword arguments
   greet(last_name="Doe", first_name="John")  # Order doesn't matter!
   greet(first_name="John", last_name="Doe")  # Same result
   
   - Can mix positional and keyword arguments
   - Keyword arguments must come after positional arguments

8. DEFAULT PARAMETERS:
   - Parameters can have default values
   - If argument not provided, default value is used
   
   Syntax:
   def function_name(parameter=default_value):
       # code
   
   Example:
   def greet(name, greeting="Hello"):
       print(f"{greeting}, {name}!")
   
   greet("Alice")  # Uses default: greeting="Hello"
   # Output: Hello, Alice!
   
   greet("Bob", "Hi")  # Overrides default: greeting="Hi"
   # Output: Hi, Bob!
   
   - Parameters with defaults must come after parameters without defaults
   - Can have multiple default parameters

9. RETURN STATEMENTS:
   - Functions can return values using return statement
   - return exits the function and sends value back to caller
   - If no return, function returns None
   
   Syntax:
   def function_name():
       return value
   
   Example:
   def add(x, y):
       return x + y
   
   result = add(5, 3)  # result = 8
   print(result)  # 8
   
   - return immediately exits the function
   - Code after return in same block won't execute

10. MULTIPLE RETURN VALUES:
    - Functions can return multiple values (as a tuple)
    - Can unpack multiple return values
    
    Example:
    def get_name():
        return "John", "Doe"  # Returns tuple
    
    first, last = get_name()  # Unpacking
    # first = "John", last = "Doe"
    
    # Or use as tuple
    name = get_name()  # name = ("John", "Doe")
    
    - Multiple values are automatically packed into a tuple
    - Can return any number of values

11. FUNCTION SCOPE:
    - Variables defined inside function are local (only accessible inside function)
    - Variables defined outside function are global (accessible everywhere)
    - Local variables don't affect global variables with same name
    
    Example:
    x = 10  # Global variable
    
    def my_function():
        x = 5  # Local variable (different from global x)
        print(x)  # 5
    
    my_function()
    print(x)  # 10 (global x unchanged)
    
    - Use global keyword to modify global variables inside function

12. DOCSTRINGS:
    - Documentation strings for functions
    - Written in triple quotes """ """
    - Describes what function does
    
    Example:
    def add(x, y):
        """Adds two numbers and returns the result."""
        return x + y
    
    - Access with: function_name.__doc__
    - Helps others understand your code

13. FUNCTION TYPES:
    
    Type 1 - No parameters, no return:
    def greet():
        print("Hello!")
    
    Type 2 - With parameters, no return:
    def greet(name):
        print(f"Hello, {name}!")
    
    Type 3 - No parameters, with return:
    def get_pi():
        return 3.14159
    
    Type 4 - With parameters, with return:
    def add(x, y):
        return x + y
    
    Type 5 - Multiple returns:
    def divide(x, y):
        quotient = x // y
        remainder = x % y
        return quotient, remainder

14. COMMON PATTERNS:
    
    Pattern 1 - Calculator functions:
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    Pattern 2 - List operations:
    def get_max(numbers):
        return max(numbers)
    
    def get_sum(numbers):
        return sum(numbers)
    
    Pattern 3 - String operations:
    def capitalize_words(text):
        return text.title()
    
    Pattern 4 - Conditional returns:
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False
    
    # Or simpler:
    def is_even(number):
        return number % 2 == 0

15. CALLING FUNCTIONS:
    - Functions must be called to execute
    - Can store return value in variable
    - Can use return value directly
    
    Example:
    def square(x):
        return x ** 2
    
    # Store in variable
    result = square(5)  # result = 25
    
    # Use directly
    print(square(5))  # 25
    
    # Use in expression
    total = square(3) + square(4)  # 9 + 16 = 25

16. PARAMETER ORDER RULES:
    - Positional parameters first
    - Then default parameters
    - Keyword arguments can be in any order (but after positional)
    
    Correct:
    def func(a, b, c=10, d=20):
        pass
    
    func(1, 2)  # a=1, b=2, c=10, d=20
    func(1, 2, 3)  # a=1, b=2, c=3, d=20
    func(1, 2, d=30)  # a=1, b=2, c=10, d=30
    
    Wrong:
    def func(a=10, b):  # Error! Default before non-default
        pass

17. RETURN VS PRINT:
    - return: Sends value back to caller (can be stored/used)
    - print: Displays value to screen (can't be stored/used)
    
    Example:
    def add_print(x, y):
        print(x + y)  # Displays but returns None
    
    def add_return(x, y):
        return x + y  # Returns value
    
    result1 = add_print(5, 3)  # Prints 8, but result1 = None
    result2 = add_return(5, 3)  # result2 = 8

18. WHEN TO USE FUNCTIONS:
    - Code that's repeated multiple times
    - Complex logic that should be separated
    - Tasks that can be reused
    - To make code more readable and organized
    - To test code in isolation

19. BEST PRACTICES:
    - Use descriptive function names (verb + noun)
    - Keep functions focused on one task
    - Use docstrings to document functions
    - Don't make functions too long
    - Use meaningful parameter names
    - Return values instead of printing (when possible)

20. IMPORTANT NOTES:
    - Function definition doesn't execute code (only when called)
    - Parameters are local variables
    - return exits function immediately
    - Functions can call other functions
    - Functions can be defined in any order (but must be defined before calling)
    - Can have functions with same name in different scopes

