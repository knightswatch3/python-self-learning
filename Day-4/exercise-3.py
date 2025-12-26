"""
Exercise 3: Input/Output (print(), input())

Problem:
You need to learn how to get input from users and display output.
"""

# ============================================================================
# Task 1: Basic print() function
# - Print a simple message: "Hello, World!"
# - Print multiple values: print("Name:", "Alice", "Age:", 25)
# - Print with separator: print("Python", "Programming", sep="-")
# - Print with end parameter: print("Hello", end=" ")
#                              print("World") (should print on same line)
# ============================================================================

print("\n--- Task 1: Basic print() function ---")
# Your code here:
print("Hello, World!")
print("Name: ", "Alice", "Age: 25")
print("Python","Programming", sep="-")
print("Hello", end=" ")
print("World!")

# ============================================================================
# Task 2: Getting user input with input()
# - Ask for user's name: name = input("Enter your name: ")
# - Ask for user's age: age = input("Enter your age: ")
# - Print a greeting using the input: "Hello, {name}! You are {age} years old"
# Note: input() always returns a string, so age will be a string
# ============================================================================

print("\n--- Task 2: Getting user input ---")
# Your code here:
name= input("Enter your name:")
age= input("Enter your age:")
print("Hello, {}! You are {} years old".format(name, age))

# ============================================================================
# Task 3: Type conversion with input()
# - Ask for a number: num_str = input("Enter a number: ")
# - Convert it to integer: num = int(num_str)
# - Ask for a decimal: decimal_str = input("Enter a decimal: ")
# - Convert it to float: decimal = float(decimal_str)
# - Print both with labels
# ============================================================================

print("\n--- Task 3: Type conversion with input() ---")
# Your code here:
num_str = input("Enter a number:")
num = int(num_str)
decimal_str=float(input("Enter a decimal:"))
decimal='{:.2f}'.format(decimal_str)
print('Decimal', decimal)

# ============================================================================
# Task 4: Input validation (basic)
# - Ask for age: age_input = input("Enter your age: ")
# - Try to convert to int: age = int(age_input)
# - If user enters non-number, what happens? (Try it!)
# - Print the age
# Note: We'll learn proper error handling later, but observe what happens
# ============================================================================

print("\n--- Task 4: Input validation ---")
# Your code here:
age_input=input("Enter your age:")
age=int(age_input)
print(age)

# ============================================================================
# Task 5: Multiple inputs and calculations
# - Ask for two numbers: num1 = int(input("Enter first number: "))
# - Ask for second number: num2 = int(input("Enter second number: "))
# - Calculate and print: sum, difference, product, quotient
# - Format the output nicely using f-strings
# ============================================================================

print("\n--- Task 5: Multiple inputs and calculations ---")
# Your code here:
num1 = int(input("Enter a number"))
num2 = int(input("Enter second number"))
print(f"Sum: {num1+num2}")
print(f"Difference: {num1-num2}")
print(f"Product: {num1*num2}")
print(f"Quotient: {num1/num2}")

# ============================================================================
# Task 6: Combining print() features
# - Use print() with sep and end parameters together
# - Example: print("Python", "is", "fun", sep="-", end="!")
# - Create your own combination
# ============================================================================

print("\n--- Task 6: Combining print() features ---")
# Your code here:

print("Python", "is", "fun", sep="-", end="!")
