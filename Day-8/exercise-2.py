"""
Exercise 2: Sets - Operations and Methods

Problem:
You need to learn how to work with sets in Python, including operations and methods.
"""

# Starting sets (given):
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}

# ============================================================================
# Task 1: Basic set operations
# - Check if "apple" is in fruits using 'in' operator
# - Get the length of numbers using len()
# - Loop through fruits and print each item
# - Print all results
# ============================================================================

print("\n--- Task 1: Basic set operations ---")
# Your code here:
print(fruits.issuperset(["apple"]))
print(len(numbers))
for fruit in fruits:
    print(fruit)

# ============================================================================
# Task 2: Adding and removing elements
# - Add "orange" to fruits using add()
# - Add multiple items: fruits.update(["grape", "kiwi"])
# - Remove "banana" using remove() (will error if not exists)
# - Remove "cherry" using discard() (won't error if not exists)
# - Try pop() to remove and return an arbitrary element
# - Print fruits after each operation
# ============================================================================

print("\n--- Task 2: Adding and removing elements ---")
# Your code here:
fruits.add("orange")
print(fruits)
fruits.update(["orange","grapes"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("cherry")
x=fruits.pop()
print("removed ",x)

# ============================================================================
# Task 3: Set operations - Union
# - Create two sets: set1 = {1, 2, 3}, set2 = {3, 4, 5}
# - Find union using union() method: set1.union(set2)
# - Find union using | operator: set1 | set2
# - Print both results (they should be the same)
# ============================================================================

print("\n--- Task 3: Set operations - Union ---")
# Your code here:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1|set2)

# ============================================================================
# Task 4: Set operations - Intersection
# - Use the same sets from Task 3
# - Find intersection using intersection() method: set1.intersection(set2)
# - Find intersection using & operator: set1 & set2
# - Print both results
# ============================================================================

print("\n--- Task 4: Set operations - Intersection ---")
# Your code here:
print(set1.intersection(set2))
print(set1&set2)


# ============================================================================
# Task 5: Set operations - Difference
# - Use the same sets from Task 3
# - Find difference using difference() method: set1.difference(set2)
# - Find difference using - operator: set1 - set2
# - Find symmetric difference: set1.symmetric_difference(set2) or set1 ^ set2
# - Print all results
# ============================================================================

print("\n--- Task 5: Set operations - Difference ---")
# Your code here:
print(set1.difference(set2))
print(set1-set2)
print(set1.symmetric_difference(set2))
print(set1^set2)


# ============================================================================
# Task 6: Set comparison methods
# - Create sets: set_a = {1, 2, 3}, set_b = {1, 2, 3, 4, 5}
# - Check if set_a is subset of set_b: set_a.issubset(set_b) or set_a <= set_b
# - Check if set_b is superset of set_a: set_b.issuperset(set_a) or set_b >= set_a
# - Check if sets are disjoint (no common elements): set_a.isdisjoint({6, 7, 8})
# - Print all results
# ============================================================================

print("\n--- Task 6: Set comparison methods ---")
# Your code here:
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))
print(set_b.issuperset(set_a))
print(set_a.isdisjoint(set_b))

# ============================================================================
# Task 7: Converting lists to sets (removing duplicates)
# - Create a list with duplicates: duplicates = [1, 2, 2, 3, 3, 3, 4]
# - Convert to set to remove duplicates: set(duplicates)
# - Convert back to list: list(set(duplicates))
# - Print results
# ============================================================================

print("\n--- Task 7: Converting lists to sets (removing duplicates) ---")
# Your code here:
duplicates = [1, 2, 2, 3, 3, 3, 4]
no_dups=set(duplicates)
print(no_dups)
no_dups_list=list(no_dups)
print(no_dups)
print(type(no_dups))
print(type(no_dups_list))

# ============================================================================
# Task 8: Frozenset (immutable set)
# - Create a frozenset: frozen = frozenset([1, 2, 3, 4, 5])
# - Try to add to it: frozen.add(6) (will error)
# - Try set operations: frozen.union({6, 7}) (this works, returns new frozenset)
# - Print results
# ============================================================================

print("\n--- Task 8: Frozenset (immutable set) ---")
# Your code here:
frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
print(frozen.union({6,9}))

# ============================================================================
# Task 9: Set comprehension (advanced)
# - Create a set of squares: {x**2 for x in range(5)}
# - Create a set of even numbers: {x for x in range(10) if x % 2 == 0}
# - Print both results
# ============================================================================

print("\n--- Task 9: Set comprehension ---")
# Your code here:
square_set={x**2 for x in range(5)}
even_set={x for x in range(1,10,2)}
print(square_set)
print(even_set)

