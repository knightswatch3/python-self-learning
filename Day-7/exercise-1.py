"""
Exercise 1: Lists - Indexing, Slicing, and Methods

Problem:
You need to learn how to work with lists in Python, including indexing, slicing, and common methods.
"""

# Starting lists (given):
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# ============================================================================
# Task 1: List Indexing
# - Access the first element of numbers (index 0)
# - Access the last element of numbers (using negative index)
# - Access the middle element of fruits
# - Try to access index 10 in numbers (what happens?)
# - Print all results
# ============================================================================

print("\n--- Task 1: List Indexing ---")
# Your code here:
print(numbers[0])
print(numbers[-1])
print(fruits[int((len(fruits)-1)/2)])

# ============================================================================
# Task 2: List Slicing
# - Get first 3 elements of numbers: numbers[0:3]
# - Get last 2 elements of fruits: fruits[-2:]
# - Get elements from index 1 to 3 of numbers: numbers[1:4]
# - Get all elements except first and last: numbers[1:-1]
# - Reverse the list using slicing: numbers[::-1]
# - Print all results
# ============================================================================

print("\n--- Task 2: List Slicing ---")
# Your code here:
print(numbers[0:3])
print(fruits[-2:])
print(numbers[1:4])
print(numbers[1:-1])
print(numbers[::-1])

# ============================================================================
# Task 3: append() method
# - Add "orange" to fruits using append()
# - Add 60 to numbers using append()
# - Print both lists after appending
# ============================================================================

print("\n--- Task 3: append() method ---")
# Your code here:
fruits.append("orange")
print("->",fruits)

# ============================================================================
# Task 4: extend() method
# - Create a new list: more_fruits = ["grape", "kiwi"]
# - Extend fruits with more_fruits using extend()
# - Create another list: more_numbers = [70, 80]
# - Extend numbers with more_numbers
# - Print both lists after extending
# - Note: Compare extend() vs append() - what's the difference?
# ============================================================================

print("\n--- Task 4: extend() method ---")
# Your code here:
more_fruits = ["grape", "kiwi"]
more_fruits.extend(fruits)
print(more_fruits)

# ============================================================================
# Task 5: insert() method
# - Insert "mango" at index 1 in fruits using insert(1, "mango")
# - Insert 25 at index 2 in numbers using insert(2, 25)
# - Print both lists after inserting
# ============================================================================

print("\n--- Task 5: insert() method ---")
# Your code here:
fruits.insert(1,"mango")
print(fruits)

# ============================================================================
# Task 6: remove() method
# - Remove "banana" from fruits using remove("banana")
# - Remove 30 from numbers using remove(30)
# - Print both lists after removing
# - Try to remove something that doesn't exist - what happens?
# ============================================================================

print("\n--- Task 6: remove() method ---")
# Your code here:
fruits.remove("banana")
print(fruits)

# ============================================================================
# Task 7: pop() method
# - Remove and return the last element of fruits using pop()
# - Store it in a variable and print it
# - Remove and return element at index 1 of numbers using pop(1)
# - Store it and print it
# - Print both lists after popping
# ============================================================================

print("\n--- Task 7: pop() method ---")
# Your code here:
popped = fruits.pop()
print(popped)
popped_again = fruits.pop(1)
print(popped_again)


# ============================================================================
# Task 8: sort() method
# - Create a list: unsorted = [5, 2, 8, 1, 9, 3]
# - Sort it using sort() (modifies the list)
# - Create a list of strings: words = ["zebra", "apple", "banana"]
# - Sort it using sort()
# - Print both sorted lists
# - Try sort(reverse=True) to sort in descending order
# ============================================================================

print("\n--- Task 8: sort() method ---")
# Your code here:
unsorted = [5, 2, 8, 1, 9, 3]
unsorted.sort()
print(unsorted)
words = ["zebra", "apple", "banana"]
words.sort()
print(words)
# ============================================================================
# Task 9: reverse() method
# - Create a list: original = [1, 2, 3, 4, 5]
# - Reverse it using reverse() (modifies the list)
# - Print the reversed list
# - Compare with slicing [::-1] - what's the difference?
# with slicing it is only in place operation where reverse will update the variable
# ============================================================================

print("\n--- Task 9: reverse() method ---")
# Your code here:
original = [1, 2, 3, 4, 5]
print(original[::-1])
print(original)
original.reverse()
print(original)

# ============================================================================
# Task 10: index() method
# - Find the index of "cherry" in fruits using index("cherry")
# - Find the index of 40 in numbers using index(40)
# - Print both indices
# - Try to find index of something that doesn't exist - what happens?
# ============================================================================

print("\n--- Task 10: index() method ---")
# Your code here:
print(fruits.index("cherry"))
print(numbers.index(40))


# ============================================================================
# Task 11: count() method
# - Create a list with duplicates: duplicates = [1, 2, 2, 3, 2, 4, 2]
# - Count how many times 2 appears using count(2)
# - Count how many times 5 appears using count(5)
# - Print both counts
# ============================================================================

print("\n--- Task 11: count() method ---")
# Your code here:
duplicates = [1, 2, 2, 3, 2, 4, 2]
print(duplicates.count(2))
print(duplicates.count(5))

# ============================================================================
# Task 12: Other useful list operations
# - Get the length of fruits using len(fruits)
# - Check if "apple" is in fruits using "apple" in fruits
# - Concatenate two lists: [1, 2] + [3, 4]
# - Repeat a list: [1, 2] * 3
# - Print all results
# ============================================================================

print("\n--- Task 12: Other useful list operations ---")
# Your code here:
print(len(fruits))
print(fruits.count("apple")==1)
extended_list = [1, 2]+([3, 4])
print(extended_list)
print([1,2]*3)
