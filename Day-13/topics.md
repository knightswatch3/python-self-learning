Exception Handling: `try`/`except`/`else`/`finally`, `raise`, Custom Exceptions
Add robust exception handling to the file operations from Day 12.

================================================================================
EXCEPTION HANDLING - Comprehensive Guide
================================================================================

1. WHAT ARE EXCEPTIONS?
   - Errors that occur during program execution
   - Python raises exceptions when something goes wrong
   - Without handling, exceptions crash your program
   - Exception handling lets you deal with errors gracefully

2. COMMON EXCEPTIONS:
   - FileNotFoundError: File doesn't exist
   - ZeroDivisionError: Dividing by zero
   - ValueError: Wrong type of value
   - TypeError: Wrong data type used
   - IndexError: List index out of range
   - KeyError: Dictionary key doesn't exist
   - NameError: Variable doesn't exist

3. BASIC TRY/EXCEPT SYNTAX:
   try:
       # Code that might cause an error
       risky_code()
   except ExceptionType:
       # What to do if error occurs
       handle_error()

================================================================================
TRY/EXCEPT - Comprehensive Guide
================================================================================

1. BASIC TRY/EXCEPT:
   - Try to run code, catch errors if they occur
   - Program continues instead of crashing
   
   Syntax:
   try:
       # Code that might fail
   except:
       # Handle the error
   
   Example:
   try:
       result = 10 / 0
   except:
       print("Error occurred!")

2. CATCHING SPECIFIC EXCEPTIONS:
   - Catch specific error types
   - More precise error handling
   
   Example:
   try:
       number = int(input("Enter a number: "))
   except ValueError:
       print("That's not a valid number!")
   except ZeroDivisionError:
       print("Cannot divide by zero!")

3. MULTIPLE EXCEPT CLAUSES:
   - Handle different errors differently
   - Order matters (most specific first)
   
   Example:
   try:
       file = open("data.txt", "r")
       content = file.read()
       result = 10 / int(content)
   except FileNotFoundError:
       print("File not found!")
   except ValueError:
       print("Invalid number in file!")
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   finally:
       file.close()

4. CATCHING MULTIPLE EXCEPTIONS:
   - Catch multiple exception types in one clause
   
   Example:
   try:
       risky_operation()
   except (ValueError, TypeError):
       print("Value or type error occurred!")

5. CATCHING ALL EXCEPTIONS:
   - Use bare except (not recommended)
   - Better: use Exception (catches all built-in exceptions)
   
   Example:
   try:
       risky_code()
   except Exception as e:
       print(f"An error occurred: {e}")

6. GETTING ERROR MESSAGE:
   - Use 'as' to get the exception object
   - Access error message with exception object
   
   Example:
   try:
       result = 10 / 0
   except ZeroDivisionError as e:
       print(f"Error: {e}")  # Error: division by zero

================================================================================
ELSE CLAUSE - Comprehensive Guide
================================================================================

1. WHAT IS ELSE IN TRY/EXCEPT?
   - Code in 'else' runs only if NO exception occurred
   - Runs after try block completes successfully
   - Useful for code that should only run on success
   
   Syntax:
   try:
       # Code that might fail
   except:
       # Handle error
   else:
       # Runs if no error occurred

2. ELSE EXAMPLE:
   try:
       number = int(input("Enter a number: "))
   except ValueError:
       print("Invalid input!")
   else:
       print(f"You entered: {number}")
       print("This only runs if conversion succeeded!")

3. ELSE VS CODE AFTER TRY:
   - Code after try/except always runs
   - else only runs if no exception occurred
   
   Example:
   try:
       result = 10 / 2
   except ZeroDivisionError:
       print("Error!")
   else:
       print("Success!")  # Only runs if no error
   print("Always runs")   # Always runs

4. WHEN TO USE ELSE:
   - When you have code that should only run on success
   - When you want to separate success logic from error handling
   - Common with file operations

================================================================================
FINALLY CLAUSE - Comprehensive Guide
================================================================================

1. WHAT IS FINALLY?
   - Code that ALWAYS runs, regardless of exceptions
   - Runs even if exception occurs
   - Perfect for cleanup code (closing files, etc.)
   
   Syntax:
   try:
       # Code that might fail
   except:
       # Handle error
   finally:
       # Always runs

2. FINALLY EXAMPLE:
   file = None
   try:
       file = open("data.txt", "r")
       content = file.read()
   except FileNotFoundError:
       print("File not found!")
   finally:
       if file:
           file.close()  # Always closes, even if error
       print("Cleanup complete!")

3. FINALLY ALWAYS RUNS:
   - Runs even if exception occurs
   - Runs even if return statement in try/except
   - Perfect for resource cleanup
   
   Example:
   def example():
       try:
           return "Success"
       finally:
           print("This always runs!")

4. FINALLY WITH WITH STATEMENT:
   - 'with' statement handles cleanup automatically
   - But finally still useful for other cleanup
   
   Example:
   try:
       with open("data.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found!")
   finally:
       print("Operation complete!")

================================================================================
RAISE - Comprehensive Guide
================================================================================

1. WHAT IS RAISE?
   - Manually trigger an exception
   - Raise exceptions when conditions aren't met
   - Useful for validation and error signaling
   
   Syntax:
   raise ExceptionType("Error message")

2. BASIC RAISE:
   Example:
   def divide(x, y):
       if y == 0:
           raise ZeroDivisionError("Cannot divide by zero!")
       return x / y
   
   try:
       result = divide(10, 0)
   except ZeroDivisionError as e:
       print(e)  # Cannot divide by zero!

3. RAISE WITH MESSAGE:
   - Include helpful error messages
   - Makes debugging easier
   
   Example:
   def get_age():
       age = int(input("Enter age: "))
       if age < 0:
           raise ValueError("Age cannot be negative!")
       if age > 150:
           raise ValueError("Age seems unrealistic!")
       return age

4. RE-RAISING EXCEPTIONS:
   - Catch exception, do something, then raise it again
   - Useful for logging before re-raising
   
   Example:
   try:
       risky_operation()
   except ValueError:
       print("Logging the error...")
       raise  # Re-raise the same exception

5. RAISING DIFFERENT EXCEPTIONS:
   - Can raise different exception than caught
   - Transform one error into another
   
   Example:
   try:
       file = open("data.txt", "r")
   except FileNotFoundError:
       raise IOError("Could not access file!")

================================================================================
CUSTOM EXCEPTIONS - Comprehensive Guide
================================================================================

1. WHAT ARE CUSTOM EXCEPTIONS?
   - Create your own exception types
   - More specific error handling
   - Better code organization
   - Inherit from Exception class

2. CREATING CUSTOM EXCEPTION:
   - Create a class that inherits from Exception
   - Can add custom behavior
   
   Example:
   class CustomError(Exception):
       pass
   
   # Use it
   raise CustomError("Something went wrong!")

3. CUSTOM EXCEPTION WITH MESSAGE:
   Example:
   class InvalidAgeError(Exception):
       def __init__(self, age, message="Invalid age provided"):
           self.age = age
           self.message = message
           super().__init__(self.message)
   
   # Use it
   if age < 0:
       raise InvalidAgeError(age, "Age cannot be negative!")

4. CUSTOM EXCEPTION WITH ATTRIBUTES:
   Example:
   class FileReadError(Exception):
       def __init__(self, filename, reason):
           self.filename = filename
           self.reason = reason
           super().__init__(f"Could not read {filename}: {reason}")

5. USING CUSTOM EXCEPTIONS:
   Example:
   class NegativeNumberError(Exception):
       pass
   
   def process_number(n):
       if n < 0:
           raise NegativeNumberError(f"{n} is negative!")
       return n * 2
   
   try:
       result = process_number(-5)
   except NegativeNumberError as e:
       print(f"Error: {e}")

6. INHERITANCE IN EXCEPTIONS:
   - Custom exceptions can inherit from other exceptions
   - Create exception hierarchies
   
   Example:
   class MathError(Exception):
       pass
   
   class DivisionError(MathError):
       pass
   
   class ZeroDivisionError(DivisionError):
       pass

================================================================================
BEST PRACTICES - Comprehensive Guide
================================================================================

1. BE SPECIFIC:
   - Catch specific exceptions, not all
   - Better error handling
   
   Bad:
   try:
       code()
   except:
       pass  # Too broad!
   
   Good:
   try:
       code()
   except FileNotFoundError:
       handle_file_error()
   except ValueError:
       handle_value_error()

2. DON'T SWALLOW EXCEPTIONS:
   - Don't catch and ignore without reason
   - At least log the error
   
   Bad:
   try:
       risky_operation()
   except:
       pass  # Silent failure!
   
   Good:
   try:
       risky_operation()
   except Exception as e:
       print(f"Error: {e}")  # At least log it

3. USE FINALLY FOR CLEANUP:
   - Always clean up resources
   - Use finally or with statement
   
   Good:
   try:
       file = open("data.txt", "r")
       # use file
   finally:
       file.close()

4. PROVIDE HELPFUL ERROR MESSAGES:
   - Make errors easy to understand
   - Include context in messages
   
   Good:
   raise ValueError(f"Invalid age: {age}. Must be between 0 and 120.")

5. USE CUSTOM EXCEPTIONS FOR YOUR DOMAIN:
   - Create exceptions specific to your application
   - Makes code more readable
   
   Example:
   class InsufficientFundsError(Exception):
       pass
   
   if balance < amount:
       raise InsufficientFundsError("Not enough money!")

6. EXCEPTION HANDLING PATTERNS:
   
   Pattern 1: Try to do, handle if fails
   try:
       result = operation()
   except SpecificError:
       handle_error()
   
   Pattern 2: Validate first, then operate
   if not valid:
       raise ValueError("Invalid input!")
   result = operation()
   
   Pattern 3: Try with cleanup
   try:
       use_resource()
   except:
       handle_error()
   finally:
       cleanup_resource()

7. COMMON MISTAKES:
   - Catching too broad (bare except)
   - Not handling specific exceptions
   - Forgetting to close resources
   - Not providing error messages
   - Swallowing exceptions silently

8. WHEN TO USE EXCEPTIONS:
   - Use for exceptional circumstances
   - Not for normal control flow
   - Use for errors that can't be prevented
   - Use for validation failures

================================================================================
EXCEPTION HIERARCHY - Quick Reference
================================================================================

BaseException
    Exception
        ArithmeticError
            ZeroDivisionError
            OverflowError
        LookupError
            IndexError
            KeyError
        OSError
            FileNotFoundError
            PermissionError
        ValueError
        TypeError
        NameError
        AttributeError
    KeyboardInterrupt
    SystemExit

- All exceptions inherit from Exception (except system exceptions)
- Can catch base class to catch all subclasses
- Example: except OSError catches FileNotFoundError, PermissionError, etc.

================================================================================
REAL-WORLD EXAMPLES
================================================================================

1. FILE OPERATIONS:
   try:
       with open("data.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found. Creating new file...")
       with open("data.txt", "w") as file:
           file.write("Default content")
   except PermissionError:
       print("Permission denied!")
   except Exception as e:
       print(f"Unexpected error: {e}")

2. USER INPUT VALIDATION:
   while True:
       try:
           age = int(input("Enter your age: "))
           if age < 0 or age > 120:
               raise ValueError("Age must be between 0 and 120")
           break
       except ValueError as e:
           print(f"Invalid input: {e}. Please try again.")

3. DIVISION WITH VALIDATION:
   def safe_divide(x, y):
       try:
           if y == 0:
               raise ZeroDivisionError("Cannot divide by zero!")
           return x / y
       except ZeroDivisionError as e:
           print(f"Error: {e}")
           return None

4. DICTIONARY ACCESS:
   data = {"name": "Alice", "age": 25}
   try:
       city = data["city"]
   except KeyError:
       city = "Unknown"
       print("City not found, using default.")

5. LIST OPERATIONS:
   numbers = [1, 2, 3]
   try:
       value = numbers[10]
   except IndexError:
       print("Index out of range!")
       value = None

