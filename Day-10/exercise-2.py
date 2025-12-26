"""
Exercise 2: Function Parameters (Positional, Keyword, Default)

Problem:
You need to learn about different types of function parameters and how to use them.
"""

# ============================================================================
# Task 1: Positional parameters
# 1. Define a function called create_profile() that takes three parameters in order:
#    'name', 'age', and 'city'
# 2. The function should print: "Name: [name], Age: [age], City: [city]"
# 3. Call the function using positional arguments (in order)
# 4. Try calling with arguments in wrong order and observe what happens
# ============================================================================

print("\n--- Task 1: Positional parameters ---")
# Your code here:


# ============================================================================
# Task 2: Keyword arguments
# 1. Using the create_profile() function from Task 1, call it using keyword arguments
# 2. Try calling with keyword arguments in different orders
# 3. Observe that order doesn't matter with keyword arguments
# ============================================================================

print("\n--- Task 2: Keyword arguments ---")
# Your code here:


# ============================================================================
# Task 3: Mixing positional and keyword arguments
# 1. Define a function called calculate() that takes four parameters: 'a', 'b', 'c', 'd'
# 2. The function should return: (a + b) * (c + d)
# 3. Call the function mixing positional and keyword arguments
# 4. Remember: positional arguments must come before keyword arguments
# ============================================================================

print("\n--- Task 3: Mixing positional and keyword arguments ---")
# Your code here:


# ============================================================================
# Task 4: Default parameters
# 1. Define a function called greet() that takes two parameters:
#    'name' (required) and 'greeting' (default value: "Hello")
# 2. The function should print: "[greeting], [name]!"
# 3. Call the function with just 'name' (should use default greeting)
# 4. Call the function with both 'name' and 'greeting' (should override default)
# ============================================================================

print("\n--- Task 4: Default parameters ---")
# Your code here:


# ============================================================================
# Task 5: Multiple default parameters
# 1. Define a function called create_message() that takes three parameters:
#    'message' (required), 'prefix' (default: "INFO"), 'suffix' (default: "!")
# 2. The function should return: "[prefix]: [message][suffix]"
# 3. Call the function with different combinations of arguments
# ============================================================================

print("\n--- Task 5: Multiple default parameters ---")
# Your code here:


# ============================================================================
# Task 6: Default parameters with calculations
# 1. Define a function called power() that takes two parameters:
#    'base' (required) and 'exponent' (default: 2)
# 2. The function should return base raised to the power of exponent
# 3. Call the function with just base (should square it)
# 4. Call the function with both base and exponent
# ============================================================================

print("\n--- Task 6: Default parameters with calculations ---")
# Your code here:


# ============================================================================
# Task 7: Complex parameter combination
# 1. Define a function called format_text() that takes:
#    'text' (required, positional)
#    'uppercase' (default: False)
#    'prefix' (default: "")
#    'suffix' (default: "")
# 2. The function should:
#    - Convert to uppercase if uppercase=True
#    - Add prefix and suffix
#    - Return the formatted text
# 3. Test with different combinations
# ============================================================================

print("\n--- Task 7: Complex parameter combination ---")
# Your code here:


# ============================================================================
# Task 8: Understanding parameter order
# 1. Define a function called process_data() with parameters in this order:
#    'data' (required), 'multiplier' (default: 1), 'offset' (default: 0)
# 2. The function should return: (data * multiplier) + offset
# 3. Call it using:
#    - Only positional: process_data(10)
#    - Positional + keyword: process_data(10, offset=5)
#    - All keyword: process_data(data=10, multiplier=2, offset=3)
# ============================================================================

print("\n--- Task 8: Parameter order ---")
# Your code here:


