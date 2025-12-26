"""
Exercise 3: *args and **kwargs

Problem:
You need to learn how to create flexible functions using *args and **kwargs.
"""

# ============================================================================
# Task 1: Basic *args
# 1. Create a function called sum_all() that uses *args
# 2. The function should return the sum of all arguments passed
# 3. Test with different numbers of arguments
# ============================================================================

print("\n--- Task 1: Basic *args ---")
# Your code here:
def sum_all(*args):
    return sum(args)
print(sum_all(4,3,2))

# ============================================================================
# Task 2: *args with regular parameters
# 1. Create a function called greet_many() that takes:
#    - 'greeting' as a regular parameter
#    - *names to accept multiple names
# 2. The function should print the greeting for each name
# 3. Test with different numbers of names
# ============================================================================

print("\n--- Task 2: *args with regular parameters ---")
# Your code here:
def greet_many(greeting:str,*arguments):
    for name in arguments:
        print(greeting + name)

greet_many("Namaste!", "satish","chandra")
    

# ============================================================================
# Task 3: Basic **kwargs
# 1. Create a function called print_info() that uses **kwargs
# 2. The function should print all key-value pairs
# 3. Test with different keyword arguments
# ============================================================================

print("\n--- Task 3: Basic **kwargs ---")
# Your code here:
def print_info(**kwargs):
    print(kwargs)

print_info(name="satish", lastname="palakoti")

# ============================================================================
# Task 4: Combining *args and **kwargs
# 1. Create a function called flexible_function() that takes:
#    - Regular parameter 'title'
#    - *args for numbers
#    - **kwargs for metadata
# 2. Print title, sum of args, and all kwargs
# 3. Test with different combinations
# ============================================================================

print("\n--- Task 4: Combining *args and **kwargs ---")
# Your code here:
def flexible_function(title, *args, **kwargs):
    print("Title is: ", title)
    print("Sum of args: ", sum(args))
    print("kwargs are: ", kwargs)

flexible_function("Hello", 1, 4, 5, namedArg=34)
# ============================================================================
# Task 5: Unpacking with *
# 1. Create a function called add_three() that takes three parameters: a, b, c
# 2. Create a list [1, 2, 3]
# 3. Call the function by unpacking the list with *
# ============================================================================

print("\n--- Task 5: Unpacking with * ---")
# Your code here:
def add_three(a,b,c):
    print("Sum is", a+b+c)

x=[1,12,3]
add_three(*x)

# ============================================================================
# Task 6: Unpacking with **
# 1. Create a function called create_profile() that takes: name, age, city
# 2. Create a dictionary with these keys and values
# 3. Call the function by unpacking the dictionary with **
# ============================================================================

print("\n--- Task 6: Unpacking with ** ---")
# Your code here:
def create_profile(name, age, city):
    print("Name is:", name)
    print("Age is:", age)
    print("City is:", city)

u={"name": "sat", "age": 34, "city": "usa"}
create_profile(**u)
# ============================================================================
# Task 7: Custom print function
# Create a custom print function called my_print() that:
# 1. Takes *args for values to print
# 2. Takes **kwargs for options like sep and end (with defaults)
# 3. Mimics the behavior of built-in print() function
# 4. Test with different arguments
# ============================================================================

print("\n--- Task 7: Custom print function ---")
# Your code here: 
# ============================================================================
# Task 8: Flexible calculator function
# Create a function called calculate() that:
# 1. Takes *args for numbers
# 2. Takes **kwargs for operation (default: "sum")
# 3. Supports operations: "sum", "product", "max", "min"
# 4. Returns the result based on operation
# 5. Test with different operations and numbers
# ============================================================================

print("\n--- Task 8: Flexible calculator function ---")
# Your code here:


