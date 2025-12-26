"""
Exercise 4: Assignment Operators

Problem:
You need to understand different assignment operators that combine assignment with operations.
"""

# Starting variables (given):
num = 10
count = 5
value = 20
total = 0

# ============================================================================
# Task 1: Basic assignment operator (=)
# - Assign 15 to a variable called `x`
# - Print x
# ============================================================================

print("\n--- Task 1: Basic assignment (=) ---")
# Your code here:
x = 15
print(x)

# ============================================================================
# Task 2: Addition assignment (+=)
# - Start with num = 10
# - Use += to add 5 to num (equivalent to: num = num + 5)
# - Print num
# ============================================================================

print("\n--- Task 2: Addition assignment (+=) ---")
# Your code here:
num = 10
num+=5
print(num)

# ============================================================================
# Task 3: Subtraction assignment (-=)
# - Start with count = 5
# - Use -= to subtract 2 from count
# - Print count
# ============================================================================

print("\n--- Task 3: Subtraction assignment (-=) ---")
# Your code here:
count = 5
count-=2
print(count)

# ============================================================================
# Task 4: Multiplication assignment (*=)
# - Start with value = 20
# - Use *= to multiply value by 3
# - Print value
# ============================================================================

print("\n--- Task 4: Multiplication assignment (*=) ---")
# Your code here:
value = 20
value+=5
print(value)

# ============================================================================
# Task 5: Division assignment (/=)
# - Start with value = 20 (or use the updated value from Task 4)
# - Use /= to divide value by 2
# - Print value
# ============================================================================

print("\n--- Task 5: Division assignment (/=) ---")
# Your code here:
value = 20
value/=2
print(value)

# ============================================================================
# Task 6: Floor division assignment (//=)
# - Start with value (use current value)
# - Use //= to do floor division by 3
# - Print value
# ============================================================================

print("\n--- Task 6: Floor division assignment (//=) ---")
# Your code here:

value//=3
print(value)

# ============================================================================
# Task 7: Modulo assignment (%=)
# - Start with value (use current value)
# - Use %= to get remainder after dividing by 4
# - Print value
# ============================================================================

print("\n--- Task 7: Modulo assignment (%=) ---")
# Your code here:

value%=4
print(value)

# ============================================================================
# Task 8: Exponentiation assignment (**=)
# - Start with num = 2 (create a new variable or reset)
# - Use **= to raise num to the power of 3
# - Print num
# ============================================================================

print("\n--- Task 8: Exponentiation assignment (**=) ---")
# Your code here:
num = 2
num**=3
print(num)

# ============================================================================
# Task 9: String assignment operators
# - Create a string variable `text = "Hello"`
# - Use += to concatenate " World" to it
# - Use *= to repeat the string 2 times
# - Print text after each operation
# ============================================================================

print("\n--- Task 9: String assignment operators ---")
# Your code here:

text = "Hello"
text+=" World"
text*=2
print(text)
