"""
Exercise 4: Recursion

Problem:
You need to learn how to write recursive functions that call themselves.
"""

# ============================================================================
# Task 1: Factorial using recursion
# 1. Create a recursive function called factorial() that calculates factorial
# 2. Base case: factorial(0) = 1, factorial(1) = 1
# 3. Recursive case: factorial(n) = n * factorial(n-1)
# 4. Test with different numbers
# ============================================================================

import math


print("\n--- Task 1: Factorial recursion ---")
# Your code here:
def factorial(num):
    if(num==0):
        return 1
    while(num>0):
        return num*factorial(num-1)

print(factorial(5))


# ============================================================================
# Task 2: Fibonacci using recursion
# 1. Create a recursive function called fibonacci() that calculates Fibonacci number
# 2. Base case: fibonacci(0) = 0, fibonacci(1) = 1
# 3. Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# 4. Test with different numbers
# ============================================================================

print("\n--- Task 2: Fibonacci recursion ---")
# Your code here:
def fibonacci(number):
    if(number==0):
        return 0
    elif(number==1):
        return 1
    else:
        return number+fibonacci(number-1)

print(fibonacci(4))
print(fibonacci(10))
print(fibonacci(24))
# ============================================================================
# Task 3: Sum of list using recursion
# 1. Create a recursive function called sum_list() that sums all numbers in a list
# 2. Base case: empty list returns 0
# 3. Recursive case: return first element + sum of rest of list
# 4. Test with different lists
# ============================================================================

print("\n--- Task 3: Sum list recursion ---")
# Your code here:
def sum_list(lst: list):
    if(len(lst)==0):
        return 0
    else:
        x=lst.pop()
        return x+sum_list(lst)

print(sum_list([3,4,5]))
        


# ============================================================================
# Task 4: Count items using recursion
# 1. Create a recursive function called count_items() that counts items in a list
# 2. Base case: empty list returns 0
# 3. Recursive case: return 1 + count of rest of list
# 4. Test with different lists
# ============================================================================

print("\n--- Task 4: Count items recursion ---")
# Your code here:
def count_items(lst: list):
    if(len(lst)==0):
        return 0
    else:
        lst.pop()
        return  1+count_items(lst)

print(count_items([1,4,2,3,5,6,7,0]))
# ============================================================================
# Task 5: Find maximum using recursion
# 1. Create a recursive function called find_max() that finds maximum in a list
# 2. Base case: list with one element returns that element
# 3. Recursive case: compare first element with max of rest
# 4. Test with different lists
# ============================================================================

print("\n--- Task 5: Find max recursion ---")
# Your code here:
def find_max(lst: list):
    if(len(lst)==1):
        return lst[0]
    else:
        elementToCompare=lst[0]
        print("-",elementToCompare)
        lst.remove(lst[0])
        print("sendin", lst)
        leftOvermax=find_max(lst)
        if(elementToCompare > leftOvermax):
            return elementToCompare
        else:
            return leftOvermax 

print(find_max([82,15,9]))
        


# ============================================================================
# Task 6: Power function using recursion
# 1. Create a recursive function called power() that calculates base^exponent
# 2. Base case: exponent = 0 returns 1
# 3. Recursive case: base * power(base, exponent-1)
# 4. Test with different base and exponent values
# ============================================================================

print("\n--- Task 6: Power recursion ---")
# Your code here:
def power(base, exponent=1):
    if(exponent==0):
        return 1
    else:
        newExpo = exponent-1
        return base*power(base, newExpo)

print(power(5,3))
# ============================================================================
# Task 7: Reverse string using recursion
# 1. Create a recursive function called reverse_string() that reverses a string
# 2. Base case: empty string or single character returns itself
# 3. Recursive case: last character + reverse of rest
# 4. Test with different strings
# ============================================================================

print("\n--- Task 7: Reverse string recursion ---")
# Your code here:
def reverse_string(string=""):
    # Base case: empty string or single character returns itself
    if len(string) <= 1:
        return string
    # Recursive case: last character + reverse of rest
    else:
        return string[-1] + reverse_string(string[:-1])
        
print(reverse_string("abch"))
print(reverse_string("hello"))
print(reverse_string("a"))
print(reverse_string(""))


# ============================================================================
# Task 8: Check palindrome using recursion
# 1. Create a recursive function called is_palindrome() that checks if string is palindrome
# 2. Base case: empty string or single character returns True
# 3. Recursive case: check if first and last characters match, then check middle
# 4. Test with palindrome and non-palindrome strings
# ============================================================================

print("\n--- Task 8: Palindrome recursion ---")
# Your code here:

def is_palindrom(string):
        return string==reverse_string(string)

print(is_palindrom("sxos"))
