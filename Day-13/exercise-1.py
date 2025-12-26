"""
Exercise 1: Exception Handling Basics

Problem:
Learn how to handle exceptions using try/except/else/finally blocks.
"""

# ============================================================================
# Task 1: Basic try/except
# 1. Write code that divides 10 by 0
# 2. Catch the ZeroDivisionError
# 3. Print a friendly error message
# ============================================================================

print("--- Task 1: Basic try/except ---")
# Your code here:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# ============================================================================
# Task 2: Catching specific exceptions
# 1. Try to convert a string to integer: int("abc")
# 2. Catch ValueError specifically
# 3. Print an appropriate error message
# ============================================================================

print("\n--- Task 2: Catching specific exceptions ---")
# Your code here:
try:
    number = int("abc")
except ValueError:
    print("Error: Cannot convert 'abc' to an integer!")

# ============================================================================
# Task 3: Multiple exception types
# 1. Create a function that divides two numbers
# 2. Handle both ValueError (if input not a number) and ZeroDivisionError
# 3. Test with different inputs
# ============================================================================

print("\n--- Task 3: Multiple exception types ---")
# Your code here:
def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        return None

print(divide_numbers(10, 2))  # Should work
print(divide_numbers(10, 0))  # Should catch ZeroDivisionError
print(divide_numbers(10, "2"))  # Should catch TypeError

# ============================================================================
# Task 4: Getting error information
# 1. Catch an exception and store it in a variable using 'as'
# 2. Print the error message
# 3. Try with different exceptions
# ============================================================================

print("\n--- Task 4: Getting error information ---")
# Your code here:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
    print(f"Error type: {type(e).__name__}")

try:
    number = int("not a number")
except ValueError as e:
    print(f"Caught error: {e}")

# ============================================================================
# Task 5: else clause
# 1. Try to convert user input to integer
# 2. If successful, print the number in the else block
# 3. If it fails, catch ValueError
# ============================================================================

print("\n--- Task 5: else clause ---")
# Your code here:
test_inputs = ["123", "abc", "45"]

for test_input in test_inputs:
    try:
        number = int(test_input)
    except ValueError:
        print(f"'{test_input}' is not a valid number!")
    else:
        print(f"Successfully converted '{test_input}' to {number}")

# ============================================================================
# Task 6: finally clause
# 1. Open a file in try block
# 2. Close it in finally block (so it always closes)
# 3. Test with file that exists and one that doesn't
# ============================================================================

print("\n--- Task 6: finally clause ---")
# Your code here:
file = None
try:
    file = open("test_file.txt", "w")
    file.write("Test content")
    print("File written successfully!")
except Exception as e:
    print(f"Error writing file: {e}")
finally:
    if file:
        file.close()
        print("File closed in finally block")

# ============================================================================
# Task 7: Complete try/except/else/finally
# 1. Create a complete example using all four blocks
# 2. Try to read a number from a file
# 3. Handle errors appropriately
# ============================================================================

print("\n--- Task 7: Complete try/except/else/finally ---")
# Your code here:
# First, create a test file
with open("number.txt", "w") as f:
    f.write("42")

try:
    with open("number.txt", "r") as file:
        content = file.read()
        number = int(content)
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File does not contain a valid number!")
else:
    print(f"Successfully read number: {number}")
finally:
    print("Operation completed!")

# ============================================================================
# Task 8: Catching multiple exceptions in one clause
# 1. Catch both ValueError and TypeError in a single except clause
# 2. Handle them the same way
# ============================================================================

print("\n--- Task 8: Catching multiple exceptions ---")
# Your code here:
def process_value(value):
    try:
        result = int(value) * 2
        return result
    except (ValueError, TypeError) as e:
        print(f"Invalid value type: {e}")
        return None

print(process_value("10"))    # Should work
print(process_value("abc"))    # ValueError
print(process_value(None))    # TypeError

# ============================================================================
# Task 9: Exception handling in loops
# 1. Create a list with mixed types: [1, 2, "three", 4, "five"]
# 2. Try to square each number
# 3. Handle errors and continue processing
# ============================================================================

print("\n--- Task 9: Exception handling in loops ---")
# Your code here:
numbers = [1, 2, "three", 4, "five", 6]

for item in numbers:
    try:
        squared = item ** 2
        print(f"{item} squared = {squared}")
    except TypeError:
        print(f"'{item}' is not a number, skipping...")

# ============================================================================
# Task 10: Nested try/except
# 1. Create nested try/except blocks
# 2. Handle different errors at different levels
# ============================================================================

print("\n--- Task 10: Nested try/except ---")
# Your code here:
try:
    # Outer try
    data = {"numbers": [1, 2, 3]}
    try:
        # Inner try
        value = data["numbers"][10]  # IndexError
    except IndexError:
        print("Inner: Index out of range!")
        try:
            # Nested inner try
            value = data["missing_key"]  # KeyError
        except KeyError:
            print("Nested: Key not found!")
except KeyError:
    print("Outer: Key error!")

print("\n=== Exercise 1 Complete ===")

