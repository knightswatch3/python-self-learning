"""
Exercise 3: Practical Application - Finding Common Elements

Problem:
Use sets to find common elements between two lists using union, intersection, and other set operations.
"""

# Starting lists (given):
from unittest import result


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [5, 6, 7, 8, 9, 10, 11, 12]
students_math = ["Alice", "Bob", "Charlie", "David", "Eve"]
students_science = ["Bob", "David", "Frank", "Grace", "Henry"]

# ============================================================================
# Task 1: Find common elements (intersection)
# - Convert both lists to sets
# - Find common elements using intersection() method
# - Find common elements using & operator
# - Convert result back to list
# - Print: "Common elements: [5, 6, 7, 8]"
# ============================================================================

print("\n--- Task 1: Find common elements (intersection) ---")
# Your code here:
list1_set=set(list1)
list2_set=set(list2)

print(list1_set.intersection(list2_set))
result = list1_set&list2_set
print(result)
result_list=list(result)
print(result_list)
print(type(result))
print(type(result_list))



# ============================================================================
# Task 2: Find all unique elements (union)
# - Convert both lists to sets
# - Find all unique elements using union() method
# - Find all unique elements using | operator
# - Convert result back to list and sort it
# - Print: "All unique elements: [1, 2, 3, ..., 12]"
# ============================================================================

print("\n--- Task 2: Find all unique elements (union) ---")
# Your code here:
list1_set=set(list1)
list2_set=set(list2)

print(list1_set.union(list2_set))
result = list1_set|list2_set
print(result)
result_list=list(result).sort()
print(result_list)
print(type(result))
print(type(result_list))

# ============================================================================
# Task 3: Find elements only in list1 (difference)
# - Convert both lists to sets
# - Find elements in list1 but not in list2 using difference()
# - Find elements in list2 but not in list1
# - Convert results back to lists
# - Print both results
# ============================================================================

print("\n--- Task 3: Find elements only in one list (difference) ---")
# Your code here:
list1_set=set(list1)
list2_set=set(list2)

result = list1_set-list2_set
print(result)
print(list(result)) 

result = list2_set-list1_set
print(result) 
print(list(result)) 

# ============================================================================
# Task 4: Find elements in either list but not both (symmetric difference)
# - Convert both lists to sets
# - Find symmetric difference using symmetric_difference() or ^ operator
# - Convert result back to list and sort
# - Print result
# ============================================================================

print("\n--- Task 4: Find elements in either list but not both ---")
# Your code here:

list1_set=set(list1)
list2_set=set(list2)

result = list1_set^list2_set
x=list(result).sort()
print(x)
# ============================================================================
# Task 5: Students in both classes (intersection)
# - Convert student lists to sets
# - Find students taking both math and science
# - Print: "Students in both classes: ['Bob', 'David']"
# ============================================================================

print("\n--- Task 5: Students in both classes ---")
# Your code here:

list1=set(students_math)
list2=set(students_science)

result = list1.intersection(list2)
print(list(result).sort())

# ============================================================================
# Task 6: Students in only one class (symmetric difference)
# - Find students taking only math or only science (not both)
# - Print result
# ============================================================================

print("\n--- Task 6: Students in only one class ---")
# Your code here:
math = set(students_math)
science = set(students_science)

print(list(math.symmetric_difference(science)))


# ============================================================================
# Task 7: All students (union)
# - Find all unique students across both classes
# - Sort the result alphabetically
# - Print: "All students: ['Alice', 'Bob', ...]"
# ============================================================================

print("\n--- Task 7: All students (union) ---")
# Your code here:

math = set(students_math)
science = set(students_science)

print(list(math.union(science)).sort())

# ============================================================================
# Task 8: Create a function to find common elements
# - Create function: find_common(list1, list2) that returns common elements
# - Create function: find_unique(list1, list2) that returns all unique elements
# - Test both functions with list1 and list2
# - Print results
# ============================================================================

print("\n--- Task 8: Functions for set operations ---")
# Your code here:


def find_common(list1: list,list2: list):
    list1_set=set(list1)
    list2_set=set(list2)
    return list(list1_set.intersection(list2_set))
def find_unique(list1: list,list2: list):
    list1_set=set(list1)
    list2_set=set(list2)
    return list(list1_set.union(list2_set))
     

print(find_common(list1, list2))
print(find_unique(list1, list2))