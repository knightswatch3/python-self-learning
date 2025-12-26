"""
Exercise 2: Lambda Functions

Problem:
You need to learn how to create and use lambda (anonymous) functions.
"""

# Starting data (given):
from operator import add


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "cherry", "date"]

# ============================================================================
# Task 1: Basic lambda function
# 1. Create a lambda function that squares a number
# 2. Assign it to a variable called 'square'
# 3. Test it with different numbers
# ============================================================================
print("\n--- Task 1: Basic lambda function ---")
# Your code here:

square=(lambda x: x**2)
print(square(4))

# ============================================================================
# Task 2: Lambda with multiple arguments
# 1. Create a lambda function that adds three numbers
# 2. Test it with different values
# ============================================================================

print("\n--- Task 2: Lambda with multiple arguments ---")
# Your code here:
adding=(lambda a,b,c: a+b+c)
print(adding(1,9,8))

# ============================================================================
# Task 3: Lambda with conditional expression
# 1. Create a lambda function that returns the maximum of two numbers
# 2. Create a lambda function that checks if a number is even
# 3. Test both functions
# ============================================================================

print("\n--- Task 3: Lambda with conditional ---")
# Your code here:
maxi=(lambda a,b: a if(a>b) else b)
print(maxi(9,7))
is_even=(lambda x: x%2==0)
print(is_even(4))
print(is_even(5))

# ============================================================================
# Task 4: Lambda with map()
# 1. Use lambda with map() to square all numbers in the 'numbers' list
# 2. Convert the result to a list and print it
# ============================================================================

print("\n--- Task 4: Lambda with map() ---")
# Your code here:
mappedSq=list(map(lambda x:x**2, numbers))
print(mappedSq[::-1])


# ============================================================================
# Task 5: Lambda with filter()
# 1. Use lambda with filter() to get only even numbers from 'numbers' list
# 2. Convert the result to a list and print it
# ============================================================================

print("\n--- Task 5: Lambda with filter() ---")
# Your code here:
filterEven=list(filter(lambda x:x%2==0, numbers))
print(filterEven[::-1])

# ============================================================================
# Task 6: Lambda with sorted()
# 1. Use lambda with sorted() to sort 'words' by length
# 2. Print the sorted list
# ============================================================================

print("\n--- Task 6: Lambda with sorted() ---")
# Your code here:
sortWords = sorted(words, key=lambda x: len(x), reverse=True)
print(sortWords)

# ============================================================================
# Task 7: Lambda in function arguments
# 1. Create a function called apply_operation() that takes a number and a lambda function
# 2. The function should apply the lambda to the number and return the result
# 3. Test with different lambda functions (square, double, etc.)
# ============================================================================

print("\n--- Task 7: Lambda as function argument ---")
# Your code here:
def apply_operation(number, operation):
    return operation(number)

square = lambda x: x**2
double = lambda x: x*2
cube = lambda x: x**3

print(apply_operation(5, square))
print(apply_operation(5, double))
print(apply_operation(5, cube))
# ============================================================================
# Task 8: Complex lambda expression
# 1. Create a lambda function that takes a number and returns:
#    - "Even" if number is even
#    - "Odd" if number is odd
# 2. Use it with map() on the 'numbers' list
# 3. Convert to list and print
# ============================================================================

print("\n--- Task 8: Complex lambda expression ---")
# Your code here:
even_odd=(lambda x: "Even" if x%2==0 else "Odd")
result=list(map(even_odd, numbers))
print(result)

