"""
Exercise 1: List Comprehensions - Basic and Conditional

Problem:
You need to learn how to create lists concisely using list comprehensions.
"""

# Starting data (given):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["hello", "world", "python", "programming"]

# ============================================================================
# Task 1: Basic list comprehension
# Using list comprehension, create:
# 1. A list containing the squares of numbers from 0 to 4
# 2. A list containing each number from the 'numbers' list multiplied by 2
# Print both results.
# ============================================================================

print("\n--- Task 1: Basic list comprehension ---")
# Your code here:
number_sq=[x**2 for x in range(5)]
number_db=[x*2 for x in numbers]

# ============================================================================
# Task 2: List comprehension with condition (filtering)
# Using list comprehension with a condition, create:
# 1. A list containing only the even numbers from the 'numbers' list
# 2. A list containing only words from 'words' that have more than 5 characters
# Print both results.
# ============================================================================

print("\n--- Task 2: List comprehension with condition ---")
# Your code here:
newList =[x for x in numbers if x%2]
newWordlist=[x for x in words if len(x)>5]
print(newList)
print(newWordlist)

# ============================================================================
# Task 3: List comprehension with transformation and condition
# Using list comprehension that both filters and transforms, create:
# 1. A list containing the squares of only the even numbers from 'numbers'
# 2. A list containing uppercase versions of words from 'words' that are longer than 5 characters
# Print both results.
# ============================================================================

print("\n--- Task 3: Transformation with condition ---")
# Your code here:
evenListSq=[x**2 for x in numbers if x%2==0]
upperWords=[w.upper() for w in words if len(w)>5]
print(evenListSq)
print(upperWords)
# ============================================================================
# Task 4: List comprehension with if-else (ternary)
# Using list comprehension with if-else (ternary expression), create:
# 1. A list where each number from 'numbers' is replaced with "Even" if it's even, "Odd" if it's odd
# 2. A list where each word from 'words' is replaced with its length if it's longer than 5 characters, otherwise "short"
# Print both results.
# ============================================================================

print("\n--- Task 4: List comprehension with if-else ---")
# Your code here:
Even=[x for x in numbers if x%2==0]
Odd=[x for x in numbers if x%2!=0]
upperWords=[len(w) if len(w)>5 else "short" for w in words]
print(Even)
print(Odd)
print(upperWords)

# ============================================================================
# Task 5: Nested list comprehension
# Using nested list comprehensions, create:
# 1. A multiplication table with 2 rows and 2 columns:
#    - "2x2" means 2 ROWS × 2 COLUMNS (the dimensions), not multiplying by 2
#    - Row numbers: 1, 2
#    - Column numbers: 1, 2
#    - Each cell = row_number × column_number
#    - Row 1: [1×1, 1×2] = [1, 2]
#    - Row 2: [2×1, 2×2] = [2, 4]
#    - Expected result: [[1, 2], [2, 4]]
#    - Think of it like a table:
#        Column:  1   2
#      Row 1:    [1,  2]
#      Row 2:    [2,  4]
# 2. A list of tuples containing all possible pairs where first element is from [1, 2] and second is from [3, 4]
#    - All combinations: (1,3), (1,4), (2,3), (2,4)
#    - Expected result: [(1, 3), (1, 4), (2, 3), (2, 4)]
# Print both results.
# ============================================================================

print("\n--- Task 5: Nested list comprehension ---")
# Your code here:
by2and2=[[i*j for i in range(1,3)] for j in range(1,3)]
print(by2and2)
x=[1,2]
y=[3,4]
tupleMix=[(p,q) for q in y for p in x]
print(tupleMix)
# ============================================================================
# Task 6: List comprehension vs traditional loop
# Write a traditional for loop that creates a list of squares for numbers 0 to 4.
# Then write the equivalent list comprehension.
# Print both results to verify they produce the same output.
# ============================================================================

print("\n--- Task 6: List comprehension vs traditional loop ---")
# Your code here:
x=[]
for i in range(4):
    x.append(i*i)
print(x)

print([x**2 for x in range(4)])

# ============================================================================
# Task 7: List comprehension with multiple conditions
# Using list comprehension with multiple conditions (using 'and'), create:
# 1. A list of numbers from 0 to 19 that are divisible by both 2 AND 3
# 2. A list of words from 'words' that start with 'p' AND have more than 5 characters
# Print both results.
# ============================================================================

print("\n--- Task 7: Multiple conditions ---")
# Your code here:
print([p for p in range(0,19) if(p%2==0 and p%3==0)])
print([p for p in words if(p[0]=='p' and len(p)>5)])


# ============================================================================
# Task 8: List comprehension with string operations
# Using list comprehension with string operations, create:
# 1. A list containing the first letter of each word in 'words'
# 2. A list containing each word from 'words' reversed
# 3. A list containing the length of each word in 'words'
# Print all three results.
# ============================================================================

print("\n--- Task 8: String operations in comprehensions ---")
# Your code here:

print([x[0] for x in words])
print([x[::-1] for x in words])
print([len(x) for x in words])
