"""
Exercise 2: Dictionary and Set Comprehensions

Problem:
You need to learn how to create dictionaries and sets using comprehensions.
"""

# Starting data (given):
numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", "date"]
names = ["Alice", "Bob", "Charlie"]

# ============================================================================
# Task 1: Basic dictionary comprehension
# Using dictionary comprehension, create:
# 1. A dictionary that maps numbers from 0 to 4 to their squares
# 2. A dictionary that maps each word in 'words' to its length
# Print both results.
# ============================================================================

print("\n--- Task 1: Basic dictionary comprehension ---")
# Your code here:
numbersMap= {x: x**2 for x in numbers}
wordsMap= {x: len(x) for x in words}
print(numbersMap)
print(wordsMap)

# ============================================================================
# Task 2: Dictionary comprehension with condition
# Using dictionary comprehension with a condition, create:
# 1. A dictionary that maps only the even numbers from 'numbers' to their squares
# 2. A dictionary that maps only words from 'words' that are longer than 5 characters to their lengths
# Print both results.
# ============================================================================

print("\n--- Task 2: Dictionary comprehension with condition ---")
# Your code here:
evenNums = { x: x**2 for x in numbers if x%2==0}
charWords_5= {x: len(x) for x in words if len(x)>5}

print(evenNums)
print(charWords_5)

# ============================================================================
# Task 3: Dictionary comprehension with if-else
# Using dictionary comprehension with if-else (ternary expression), create:
# 1. A dictionary that maps each number in 'numbers' to "Even" if it's even, "Odd" if it's odd
# 2. A dictionary that maps each word in 'words' to "long" if it has more than 5 characters, otherwise "short"
# Print both results.
# ============================================================================

print("\n--- Task 3: Dictionary comprehension with if-else ---")
# Your code here:
mappedNumTypes={x: "Even" if x%2==0 else "Odd" for x in numbers}
mappedWordLen={x: "long" if len(x)>5 else "short" for x in words}
print(mappedNumTypes)
print(mappedWordLen)

# ============================================================================
# Task 4: Dictionary from two lists
# Create a dictionary that pairs each name from 'names' with the corresponding number from 'numbers'
# (first name with first number, second name with second number, etc.)
# You can use indexing or the zip() function.
# Print the result.
# ============================================================================

print("\n--- Task 4: Dictionary from two lists ---")
# Your code here:
mixedList={names[i]:numbers[i] for i in range(len(names))}
mixedListZip={name: num for name, num in zip(names, numbers)}
print(mixedList)
print(mixedListZip)
# ============================================================================
# Task 5: Basic set comprehension
# Using set comprehension, create:
# 1. A set containing the squares of numbers from 0 to 4
# 2. A set containing the lengths of each word in 'words'
# Print both results.
# ============================================================================

print("\n--- Task 5: Basic set comprehension ---")
# Your code here:
sq_set={x**2 for x in range(5)}
print(sq_set)
word_set={len(x) for x in words}
print(word_set)


# ============================================================================
# Task 6: Set comprehension with condition
# Using set comprehension with a condition, create:
# 1. A set containing the squares of only the even numbers from 0 to 9
# 2. A set containing the first letter of each word in 'words' that is longer than 5 characters
# Print both results.
# ============================================================================

print("\n--- Task 6: Set comprehension with condition ---")
# Your code here:
even_sq_set={x**2 for x in range(1,9) if x%2==0}
print(even_sq_set)
firstchar_set={x[0] for x in words if len(x)>5}
print(firstchar_set)
# ============================================================================
# Task 7: Nested dictionary comprehension
# Using nested dictionary comprehension, create:
# A dictionary where each key is a number from 1 to 3, and each value is itself a dictionary
# that maps numbers from 1 to 3 to their product with the outer key.
# Example structure: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
# Print the result.
# ============================================================================

print("\n--- Task 7: Nested dictionary comprehension ---")
# Your code here:
result={x: {y: y*x for y in range(1,4)} for x in range(1,4)}
print(result)

# ============================================================================
# Task 8: Converting between comprehensions
# 1. Create a list of tuples where each tuple contains (number, square) for numbers 0 to 4
# 2. Convert that list of tuples to a dictionary using dict()
# 3. Create the same dictionary directly using dictionary comprehension
# Print all three results (the last two should produce the same dictionary).
# ============================================================================

print("\n--- Task 8: Converting between comprehensions ---")
# Your code here:
lofT= [(x,x**2) for x in range(4)]
print(lofT)
lofT_dict_conv=dict(lofT)
print(lofT_dict_conv)
loft_dict={ x: x**2 for x in range(4)}
print(loft_dict)


