"""
Exercise 1: Tuples - Packing, Unpacking, and Immutability

Problem:
You need to learn how to work with tuples in Python, including packing, unpacking, and understanding immutability.
"""

# Starting tuples (given):
coordinates = (3, 4)
person = ("Alice", 25, "Engineer")
numbers = (1, 2, 3, 4, 5)

# ============================================================================
# Task 1: Basic tuple operations
# - Access the first element of coordinates (index 0)
# - Access the last element using negative index
# - Get the length of person tuple using len()
# - Check if 3 is in numbers tuple using 'in' operator
# - Print all results
# ============================================================================

print("\n--- Task 1: Basic tuple operations ---")
# Your code here:
print(coordinates[0])
print(coordinates[-1])
print(len(person))
print(3 in numbers)


# ============================================================================
# Task 2: Tuple packing
# - Create a tuple by packing: my_tuple = 1, 2, 3 (no parentheses needed)
# - Create another: name, age = "Bob", 30 (packing two values)
# - Print both tuples
# - Note: Parentheses are optional when creating tuples
# ============================================================================

print("\n--- Task 2: Tuple packing ---")
# Your code here:
my_tuple=1,2,3
name,age="Bob",30
print(my_tuple)
print(name,age)

# ============================================================================
# Task 3: Tuple unpacking
# - Unpack coordinates into x and y: x, y = coordinates
# - Unpack person into name, age, job: name, age, job = person
# - Print all unpacked variables
# ============================================================================

print("\n--- Task 3: Tuple unpacking ---")
# Your code here:
x,y=coordinates
name,age,profession=person
print("x and y", x, y)
print("name and age", name, age)

# ============================================================================
# Task 4: Multiple assignment (tuple unpacking)
# - Swap two variables using tuple unpacking: a, b = b, a
# - Try: a = 5, b = 10, then swap them
# - Print before and after
# ============================================================================

print("\n--- Task 4: Multiple assignment (swapping) ---")
# Your code here:
a=5
b=10
print(a,",",b)
a,b = b,a
print(a,",",b)

# ============================================================================
# Task 5: Tuple immutability
# - Try to modify coordinates: coordinates[0] = 10
# - Observe what happens (you'll get an error)
# - Try to append to numbers: numbers.append(6)
# - Observe what happens
# - Print error messages or explain what happened
# ============================================================================

print("\n--- Task 5: Tuple immutability ---")
# Your code here:
# coordinates[0]=10
# numbers.append(6)

# ============================================================================
# Task 6: Tuple slicing
# - Get first 3 elements of numbers: numbers[0:3]
# - Get last 2 elements: numbers[-2:]
# - Reverse the tuple: numbers[::-1]
# - Print all results
# - Note: Slicing creates a new tuple (doesn't modify original)
# ============================================================================

print("\n--- Task 6: Tuple slicing ---")
# Your code here:
print(numbers[0:3])
print(numbers[-2:])
print(numbers[::-1])


# ============================================================================
# Task 7: Tuple methods
# - Count how many times 2 appears in numbers using count(2)
# - Find index of 3 in numbers using index(3)
# - Print both results
# ============================================================================

print("\n--- Task 7: Tuple methods ---")
# Your code here:
print(numbers.count(2))
print(numbers.index(3))

# ============================================================================
# Task 8: Nested tuples
# - Create a nested tuple: nested = ((1, 2), (3, 4), (5, 6))
# - Access the first inner tuple: nested[0]
# - Access element 3 from nested: nested[1][0]
# - Unpack nested tuple: (a, b), (c, d), (e, f) = nested
# - Print all results
# ============================================================================

print("\n--- Task 8: Nested tuples ---")
# Your code here:
nested = ((1, 2), (3, 4), (5, 6))
print(nested[0])
print(nested[1][0])
(a,b),(c,d),(e,f)=nested
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)



# ============================================================================
# Task 9: Converting between tuples and lists
# - Convert numbers tuple to list: list(numbers)
# - Convert a list back to tuple: tuple([1, 2, 3])
# - Print both results
# - Note: This is useful when you need to modify a tuple
# ============================================================================

print("\n--- Task 9: Converting tuples and lists ---")
# Your code here:
number_list=list(numbers)
tuple_numbers=tuple(number_list)
print(number_list)
print(tuple_numbers)

# ============================================================================
# Task 10: Tuple with one element
# - Create a tuple with one element: single = (5,) (note the comma!)
# - Try: not_single = (5) (without comma - what type is this?)
# - Check types using type()
# - Print both and their types
# ============================================================================

print("\n--- Task 10: Tuple with one element ---")
# Your code here:
x=(5,)
not_single=(5)
print(type(x))
print(type(not_single))


