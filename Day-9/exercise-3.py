"""
Exercise 3: Generator Expressions and Converting Loops

Problem:
You need to learn generator expressions and convert previous loops into comprehensions.
"""

# Starting data (given):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["hello", "world", "python", "programming", "code"]

# ============================================================================
# Task 1: Generator expressions (basic)
# 1. Create a generator expression that yields squares of numbers from 0 to 4
# 2. Convert that generator to a list and print it
# 3. Use the generator expression directly in sum() to calculate the sum of squares
# Print all results.
# ============================================================================

print("\n--- Task 1: Generator expressions ---")
# Your code here:
sq_numbers=(x**2 for x in range(4))
print(list(sq_numbers))
print(sq_numbers)

# ============================================================================
# Task 2: Generator vs list comprehension
# Create both a list comprehension and a generator expression for squares of numbers 0 to 4.
# Print both results and observe the difference:
# - List comprehension creates the entire list immediately
# - Generator expression creates a generator object (lazy evaluation)
# ============================================================================

print("\n--- Task 2: Generator vs list comprehension ---")
# Your code here:
sq_gen=(num for num in range(4))
sq_list=[num for num in range(4)]
print(sq_gen)
print(sq_list)

# ============================================================================
# Task 3: Generator with condition
# 1. Create a generator expression that yields squares of only even numbers from 0 to 9
# 2. Convert it to a list and print it
# 3. Use the generator expression directly in max() to find the maximum even square
# Print all results.
# ============================================================================

print("\n--- Task 3: Generator with condition ---")
# Your code here:
even_sq=(x**2 for x in range(10) if x%2==0)
def even_sq_yield():
    for i in range(9):
        if i%2==0:
            yield i**2

l_even_sq=list(even_sq_yield())
print(max(l_even_sq))



# ============================================================================
# Task 4: Convert loop to list comprehension
# Write a traditional for loop that creates a list of squares for numbers 0 to 4.
# Then convert it to a list comprehension.
# Print both results (they should be the same).
# ============================================================================

print("\n--- Task 4: Convert loop to list comprehension ---")
# Your code here:
result=[]
for x in range(4):
    result.append(x**2)
    
sq_nums_list=[x**2 for x in range(5)]

print(result)
print(sq_nums_list)

# ============================================================================
# Task 5: Convert loop with condition
# Write a traditional for loop that creates a list containing only even numbers from 'numbers'.
# Then convert it to a list comprehension with a condition.
# Print both results (they should be the same).
# ============================================================================

print("\n--- Task 5: Convert loop with condition ---")
# Your code here:
answer=[]
for x in numbers:
    if(x%2==0):
        answer.append(x**2)

answer2=[x**2 for x in numbers if x%2==0]
print(answer)
print(answer2)



# ============================================================================
# Task 6: Convert loop with transformation
# Write a traditional for loop that creates a list containing the length of each word in 'words'.
# Then convert it to a list comprehension.
# Print both results (they should be the same).
# ============================================================================

print("\n--- Task 6: Convert loop with transformation ---")
# Your code here:
lengt_w=[]
for i in words:
    lengt_w.append(len(i))

print(lengt_w)
print([len(x) for x in words])

# ============================================================================
# Task 7: Convert nested loop
# Write a nested for loop that creates a list of tuples containing all pairs where
# the first element is from [1, 2] and the second element is from [3, 4].
# Then convert it to a nested list comprehension.
# Print both results (they should be the same).
# ============================================================================

print("\n--- Task 7: Convert nested loop ---")
# Your code here:
first=[1,2]
second=[3,4]
res=[]
for i in first:
    for j in second:
        res.append((i,j))
print(res)
ans2=[(i,j) for i in first  for j in second]
print(ans2)



# ============================================================================
# Task 8: Convert loop to dictionary comprehension
# Write a traditional for loop that creates a dictionary mapping each word in 'words' to its length.
# Then convert it to a dictionary comprehension.
# Print both results (they should be the same).
# ============================================================================

print("\n--- Task 8: Convert loop to dictionary comprehension ---")
# Your code here:
rex={}
for w in words:
    rex[w]=len(w)

print(rex)

rex2={x: len(x) for x in words}
print(rex2)

# ============================================================================
# Task 9: Convert loop to set comprehension
# Write a traditional for loop that creates a set containing the lengths of each word in 'words'.
# Then convert it to a set comprehension.
# Print both results (they should be the same).
# ============================================================================

print("\n--- Task 9: Convert loop to set comprehension ---")
# Your code here:
res=set({})
for i in words:
    res.add(len(i))

print(res)

res2={len(x) for x in words}
print(res2)
# ============================================================================
# Task 10: When to use generators
# Demonstrate the memory efficiency of generators:
# 1. Use a list comprehension in sum() for a large range (e.g., 0 to 999999)
# 2. Use a generator expression in sum() for the same range
# 3. Print both results (they should be the same)
# 4. Explain in a comment why generators are more memory efficient for large datasets
# ============================================================================

print("\n--- Task 10: When to use generators ---")
# Your code here:

l_comprehension=sum([x for x in range(1000000)])
print(l_comprehension)
f_gen=(x for x in range(1000000))
print(sum(f_gen))
# generators are better because they are memory efficient

