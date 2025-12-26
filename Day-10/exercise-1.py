"""
Exercise 1: Basic Function Definition and Calling

Problem:
You need to learn how to define and call functions in Python.
"""

# ============================================================================
# Task 1: Define and call a simple function
# 1. Define a function called greet() that prints "Hello, World!"
# 2. Call the function to see the output
# ============================================================================

print("\n--- Task 1: Simple function ---")
# Your code here:
def greet():
    print("Hello World!")

greet()

# ============================================================================
# Task 2: Function with one parameter
# 1. Define a function called greet_person() that takes a parameter 'name'
# 2. The function should print "Hello, [name]!" where [name] is the parameter
# 3. Call the function with different names: "Alice", "Bob", "Charlie"
# ============================================================================

print("\n--- Task 2: Function with parameter ---")
# Your code here:
def greet_person(name: str):
    print(f"Hello, {name}!")

greet_person("Satish")

# ============================================================================
# Task 3: Function with multiple parameters
# 1. Define a function called introduce() that takes two parameters: 'name' and 'age'
# 2. The function should print "My name is [name] and I am [age] years old."
# 3. Call the function with different values
# ============================================================================

print("\n--- Task 3: Function with multiple parameters ---")
# Your code here:
def introduce(name: str, age:int):
    print(f"My name is {name} and I am {age} years old.")

introduce("jack",20)


# ============================================================================
# Task 4: Function that returns a value
# 1. Define a function called square() that takes a parameter 'x' and returns x squared
# 2. Call the function with different numbers and print the results
# 3. Store the return value in a variable and print it
# ============================================================================

print("\n--- Task 4: Function with return ---")
# Your code here:
def square(x):
    return x**2

variable=square(4)
print(variable)



# ============================================================================
# Task 5: Function with calculation
# 1. Define a function called add() that takes two parameters 'a' and 'b'
# 2. The function should return the sum of a and b
# 3. Call the function with different pairs of numbers and print the results
# ============================================================================

print("\n--- Task 5: Function with calculation ---")
# Your code here:
def add(a:int, b:int):
    return a+b

print(add(2,4))

# ============================================================================
# Task 6: Function with conditional return
# 1. Define a function called is_even() that takes a parameter 'number'
# 2. The function should return True if the number is even, False otherwise
# 3. Test the function with both even and odd numbers
# ============================================================================

print("\n--- Task 6: Function with conditional return ---")
# Your code here:
def is_even(x: int):
    return x%2==0

print(is_even(4))
print(is_even(5))

# ============================================================================
# Task 7: Function that returns multiple values
# 1. Define a function called get_name() that returns two strings: "John" and "Doe"
# 2. Call the function and unpack the return values into two variables: first_name and last_name
# 3. Print both variables
# ============================================================================

print("\n--- Task 7: Multiple return values ---")
# Your code here:
def get_name():
    return("john", "doe")

first_name,last_name=get_name()
print("First name", first_name)
print("Last name", last_name)

# ============================================================================
# Task 8: Function with no return (implicit None)
# 1. Define a function called display_info() that takes 'name' and 'city' as parameters
# 2. The function should print the information but not return anything
# 3. Call the function and check what it returns (should be None)
# ============================================================================

print("\n--- Task 8: Function returning None ---")
# Your code here:
def display_info(name: str, city: str):
    print(f"Name is {name} and city is {city}")
    return None

print(display_info("s","sf"))

