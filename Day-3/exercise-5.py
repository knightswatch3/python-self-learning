"""
Exercise 5: String Indexing and Slicing

Problem:
You need to understand how to access individual characters and extract substrings from strings.
"""

# Starting string (given):
from operator import le


text = "Python Programming"

# ============================================================================
# Task 1: String Indexing (accessing individual characters)
# - Print the first character of text (index 0)
# - Print the last character of text
# - Print the character at index 5
# - Try to access index 100 (what happens?)
# ============================================================================

print("\n--- Task 1: String Indexing ---")
# Your code here:
print(text[0])
print(text[len(text)-1])
print(text[5])

# ============================================================================
# Task 2: Negative Indexing
# - Print the last character using negative index (-1)
# - Print the second-to-last character using negative index
# - Print the first character using negative index (calculate: -len(text))
# ============================================================================

print("\n--- Task 2: Negative Indexing ---")
# Your code here:
print(text[-1])
print(text[-2])
print(text[-len(text)])

# ============================================================================
# Task 3: String Slicing (extracting substrings)
# - Extract "Python" from text (first 6 characters)
# - Extract "Programming" from text (from index 7 to end)
# - Extract "thon" from text (characters from index 2 to 6)
# - Print all three results
# ============================================================================

print("\n--- Task 3: String Slicing ---")
# Your code here:

print(text[:6])
print(text[7:])
print(text[2:6])

# ============================================================================
# Task 4: Slicing with start, stop, and step
# - Extract every second character: text[::2]
# - Reverse the string: text[::-1]
# - Extract characters from index 0 to 10, stepping by 2
# - Print all three results
# ============================================================================

print("\n--- Task 4: Slicing with step ---")
# Your code here:
print(text[::2])
print(text[::-1])
print(text[0:10:2])

# ============================================================================
# Task 5: Slicing with negative indices
# - Extract the last 5 characters using negative indices
# - Extract from index -10 to -1 (excluding last character)
# - Extract from start to -8 (everything except last 8 characters)
# - Print all three results
# ============================================================================

print("\n--- Task 5: Slicing with negative indices ---")
# Your code here:
print(text[-5::])
print(text[-10:-1:])
print(text[0:-8:])

# ============================================================================
# Task 6: String length and bounds
# - Find the length of text using len()
# - Try to access text[len(text)] (what happens? why?)
# - Access the last valid index: text[len(text) - 1]
# - Print the length and the last character
# ============================================================================

print("\n--- Task 6: String length and bounds ---")
# Your code here:
print(len(text))
# print(text[len(text)])
print(text[len(text)-1])
print(f'Length is {len(text)} and last char is{text[len(text)-1]}')

# ============================================================================
# Task 7: Practice with a new string
# - Create a string: word = "Hello"
# - Extract "ell" using slicing
# - Extract "Hlo" using slicing with step
# - Reverse the word
# - Print all results
# ============================================================================

print("\n--- Task 7: Practice with Hello ---")
# Your code here:

word = "Hello"
print(word[1:4])
print(word[::2])
print(word[::-1])
