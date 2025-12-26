"""
Exercise 2: raise and Custom Exceptions

Problem:
Learn how to raise exceptions and create custom exception classes.
"""

# ============================================================================
# Task 1: Basic raise
# 1. Create a function that checks if a number is positive
# 2. Raise ValueError if number is negative
# 3. Test the function
# ============================================================================

print("--- Task 1: Basic raise ---")
# Your code here:
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive!")
    return f"{number} is positive"

try:
    print(check_positive(5))
    print(check_positive(-3))
except ValueError as e:
    print(f"Error: {e}")

# ============================================================================
# Task 2: raise with custom message
# 1. Create a function that validates age
# 2. Raise ValueError with specific messages for different invalid cases
# 3. Test with different ages
# ============================================================================

print("\n--- Task 2: raise with custom message ---")
# Your code here:
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    if age < 18:
        raise ValueError("Must be 18 or older!")
    return f"Age {age} is valid"

test_ages = [25, -5, 200, 15]
for age in test_ages:
    try:
        result = validate_age(age)
        print(result)
    except ValueError as e:
        print(f"Age {age}: {e}")

# ============================================================================
# Task 3: Re-raising exceptions
# 1. Catch an exception, log it, then re-raise it
# 2. Show that the exception propagates up
# ============================================================================

print("\n--- Task 3: Re-raising exceptions ---")
# Your code here:
def inner_function():
    raise ValueError("Original error from inner function")

def outer_function():
    try:
        inner_function()
    except ValueError as e:
        print(f"Caught in outer: {e}")
        raise  # Re-raise the exception

try:
    outer_function()
except ValueError as e:
    print(f"Caught at top level: {e}")

# ============================================================================
# Task 4: Create a custom exception class
# 1. Create a class called NegativeNumberError that inherits from Exception
# 2. Raise it when a negative number is encountered
# 3. Catch it specifically
# ============================================================================

print("\n--- Task 4: Create custom exception class ---")
# Your code here:
class NegativeNumberError(Exception):
    pass

def process_number(n):
    if n < 0:
        raise NegativeNumberError(f"{n} is negative!")
    return n * 2

try:
    print(process_number(5))
    print(process_number(-3))
except NegativeNumberError as e:
    print(f"Custom error: {e}")

# ============================================================================
# Task 5: Custom exception with attributes
# 1. Create InvalidAgeError exception class
# 2. Store the invalid age as an attribute
# 3. Include it in the error message
# ============================================================================

print("\n--- Task 5: Custom exception with attributes ---")
# Your code here:
class InvalidAgeError(Exception):
    def __init__(self, age, message="Invalid age provided"):
        self.age = age
        self.message = message
        super().__init__(f"{message}: {age}")

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age, "Age cannot be negative")
    if age > 120:
        raise InvalidAgeError(age, "Age seems unrealistic")
    return f"Age {age} is valid"

try:
    print(check_age(25))
    print(check_age(-5))
except InvalidAgeError as e:
    print(f"Error: {e}")
    print(f"Invalid age was: {e.age}")

# ============================================================================
# Task 6: Custom exception with custom methods
# 1. Create FileReadError exception
# 2. Store filename and reason
# 3. Add a method to get formatted error message
# ============================================================================

print("\n--- Task 6: Custom exception with methods ---")
# Your code here:
class FileReadError(Exception):
    def __init__(self, filename, reason):
        self.filename = filename
        self.reason = reason
        super().__init__(f"Cannot read {filename}: {reason}")
    
    def get_details(self):
        return f"File: {self.filename}, Reason: {self.reason}"

def read_file_safe(filename):
    if not filename.endswith('.txt'):
        raise FileReadError(filename, "File must be .txt format")
    if len(filename) > 20:
        raise FileReadError(filename, "Filename too long")
    return f"Reading {filename}..."

try:
    print(read_file_safe("data.txt"))
    print(read_file_safe("data.pdf"))
except FileReadError as e:
    print(f"Error: {e}")
    print(f"Details: {e.get_details()}")

# ============================================================================
# Task 7: Exception hierarchy
# 1. Create a base exception class: MathError
# 2. Create subclasses: DivisionError, NegativeNumberError
# 3. Show inheritance in exception handling
# ============================================================================

print("\n--- Task 7: Exception hierarchy ---")
# Your code here:
class MathError(Exception):
    """Base exception for math operations"""
    pass

class DivisionError(MathError):
    """Error in division operations"""
    pass

class NegativeNumberError(MathError):
    """Error for negative numbers"""
    pass

def divide(x, y):
    if y == 0:
        raise DivisionError("Cannot divide by zero!")
    if x < 0 or y < 0:
        raise NegativeNumberError("Numbers must be positive!")
    return x / y

try:
    result = divide(10, -2)
except DivisionError as e:
    print(f"Division error: {e}")
except NegativeNumberError as e:
    print(f"Negative number error: {e}")
except MathError as e:
    print(f"Math error: {e}")

# ============================================================================
# Task 8: Raise different exception types
# 1. Create a function that can raise different exceptions
# 2. Transform one error into another
# 3. Show exception chaining
# ============================================================================

print("\n--- Task 8: Raise different exceptions ---")
# Your code here:
def process_data(data):
    try:
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        if "value" not in data:
            raise KeyError("'value' key not found")
        number = int(data["value"])
        if number < 0:
            raise ValueError("Value must be positive")
        return number * 2
    except (TypeError, KeyError) as e:
        # Transform to a more specific error
        raise ValueError(f"Invalid data format: {e}") from e

test_cases = [
    {"value": "10"},
    {"value": "-5"},
    {"other": "data"},
    "not a dict"
]

for test in test_cases:
    try:
        result = process_data(test)
        print(f"Success: {result}")
    except ValueError as e:
        print(f"Error: {e}")

# ============================================================================
# Task 9: Practical example - Bank account
# 1. Create InsufficientFundsError exception
# 2. Create a BankAccount class with withdraw method
# 3. Raise exception when balance is insufficient
# ============================================================================

print("\n--- Task 9: Practical example - Bank account ---")
# Your code here:
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds! Balance: ${balance}, Requested: ${amount}")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    print(f"Balance after withdrawing $30: ${account.withdraw(30)}")
    print(f"Balance after withdrawing $50: ${account.withdraw(50)}")
    print(f"Balance after withdrawing $30: ${account.withdraw(30)}")  # Should fail
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

# ============================================================================
# Task 10: Validation with custom exceptions
# 1. Create multiple custom exceptions for validation
# 2. Create a validate_user function
# 3. Raise appropriate exceptions for different validation failures
# ============================================================================

print("\n--- Task 10: Validation with custom exceptions ---")
# Your code here:
class ValidationError(Exception):
    """Base class for validation errors"""
    pass

class InvalidEmailError(ValidationError):
    pass

class InvalidAgeError(ValidationError):
    pass

class PasswordTooShortError(ValidationError):
    pass

def validate_user(email, age, password):
    errors = []
    
    if "@" not in email:
        raise InvalidEmailError(f"'{email}' is not a valid email")
    
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below minimum (18)")
    
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters")
    
    return "User validated successfully!"

test_users = [
    ("user@example.com", 25, "password123"),
    ("invalid-email", 25, "password123"),
    ("user@example.com", 15, "password123"),
    ("user@example.com", 25, "short"),
]

for email, age, password in test_users:
    try:
        result = validate_user(email, age, password)
        print(f"✓ {result}")
    except ValidationError as e:
        print(f"✗ Validation failed: {e}")

print("\n=== Exercise 2 Complete ===")

