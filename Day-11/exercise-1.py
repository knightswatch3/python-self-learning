"""
Exercise 1: Scope (LEGB Rule)

Problem:
You need to understand how Python resolves variable names using the LEGB rule.
"""

# Global variable
x = 10

# ============================================================================
# Task 1: Local scope
# 1. Create a function called local_scope() that defines a local variable 'x = 5'
# 2. Print x inside the function
# 3. Call the function
# 4. Print the global x outside the function
# 5. Observe that local x doesn't affect global x
# ============================================================================

print("\n--- Task 1: Local scope ---")
# Your code here:
x=10
def local_scope():
    x=5
    print(x)

local_scope()
print(x)


# ============================================================================
# Task 2: Reading global variable
# 1. Create a function called read_global() that prints the global variable 'x'
# 2. Call the function
# 3. Observe that you can read global variables from inside functions
# ============================================================================

print("\n--- Task 2: Reading global variable ---")
# Your code here:
def read_global():
    global x
    print(x)

read_global()

# ============================================================================
# Task 3: Modifying global variable
# 1. Create a function called modify_global() that uses 'global x' keyword
# 2. Inside the function, change x to 20
# 3. Call the function
# 4. Print x outside the function to see if it changed
# ============================================================================

print("\n--- Task 3: Modifying global variable ---")
# Your code here:
def modify_global():
    global x
    x = 20

print(x)
modify_global()
print(x)

# ============================================================================
# Task 4: Local variable shadowing
# 1. Create a function called shadow() that defines a local variable 'x = 100'
# 2. Print x inside the function (should print 100)
# 3. Call the function
# 4. Print global x outside (should still be the global value)
# 5. Observe that local variable "shadows" (hides) global variable
# ============================================================================

print("\n--- Task 4: Local variable shadowing ---")
# Your code here:
def shadow():
    x=100
    print(x)
shadow()
print(x)


# ============================================================================
# Task 5: Enclosing scope (nested functions)
# 1. Create an outer function called outer() that defines 'y = 50'
# 2. Create an inner function called inner() inside outer()
# 3. Inner function should print y (should access enclosing scope)
# 4. Call outer() which should call inner()
# 5. Observe that inner function can access outer function's variables
# ============================================================================

print("\n--- Task 5: Enclosing scope ---")
# Your code here:
def outer():
    y=50
    def inner():
        print(y)
    inner()
outer()

# ============================================================================
# Task 6: Nonlocal keyword
# 1. Create an outer function called outer_nonlocal() with variable 'count = 0'
# 2. Create an inner function that uses 'nonlocal count' and increments it
# 3. Call inner function from outer function
# 4. Print count in outer function to see if it was modified
# ============================================================================

print("\n--- Task 6: Nonlocal keyword ---")
# Your code here:
def outer_nonlocal():
    y=9
    def inner():
        nonlocal y
        y=y+1
        print(y)
    inner()
outer_nonlocal()
# ============================================================================
# Task 7: LEGB lookup order
# 1. Create a function that demonstrates LEGB order:
#    - Define a local variable 'name = "Local"'
#    - Create an enclosing function with 'name = "Enclosing"'
#    - Use global 'name = "Global"' at module level
#    - Print name in inner function to see which one is used
# ============================================================================

print("\n--- Task 7: LEGB lookup order ---")
# Your code here:
name="Global"
def legb():
    name='Enclosing'
    def inner():
        name='local'
        print(name)
    inner()
legb()


# ============================================================================
# Task 8: Built-in scope
# 1. Create a function that uses built-in functions like len(), print(), sum()
# 2. Observe that built-ins are always available
# 3. Try to shadow a built-in (e.g., define len = 5) and see what happens
# ============================================================================

print("\n--- Task 8: Built-in scope ---")
# Your code here:
def use():
    len="ioiasdf"
    print(len)

use()
print(len("asdf"))



