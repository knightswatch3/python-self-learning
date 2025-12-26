"""
Exercise 1: String Methods

Problem:
You need to learn common string methods for manipulating and working with strings.
"""

# Starting string (given):
text = "  Python Programming  "
sentence = "hello world python"
words = ["Python", "is", "fun"]
numbers = [1, 2, 3, 4, 5]

# ============================================================================
# Task 1: Case conversion methods
# - Convert text to uppercase using .upper()
# - Convert text to lowercase using .lower()
# - Convert sentence to title case using .title()
# - Convert sentence to capitalize (first letter uppercase) using .capitalize()
# - Print all results
# ============================================================================

print("\n--- Task 1: Case conversion methods ---")
# Your code here:
print(text.upper())
print(text.lower())
print(sentence.title())
print(sentence.capitalize())


# ============================================================================
# Task 2: String splitting
# - Split sentence by spaces using .split()
# - Split "apple,banana,cherry" by comma using .split(',')
# - Split "one-two-three" by hyphen using .split('-')
# - Print all results
# ============================================================================

print("\n--- Task 2: String splitting ---")
# Your code here:

print(sentence.split(" "))
print("apple,banana,cherry".split(','))
print("one-two-three".split('-'))


# ============================================================================
# Task 3: String joining
# - Join the words list with a space using ' '.join(words)
# - Join the words list with a hyphen using '-'.join(words)
# - Join the numbers list (convert to strings first) with ' -> ' using ' -> '.join()
# - Print all results
# ============================================================================

print("\n--- Task 3: String joining ---")
# Your code here:
print(" ".join(words))
print("-".join(words))
print(" -> ".join(str(n) for n in numbers))

# ============================================================================
# Task 4: String replacement
# - Replace "Python" with "Java" in text using .replace()
# - Replace all spaces with underscores in sentence using .replace(' ', '_')
# - Replace first occurrence only: "apple apple".replace("apple", "orange", 1)
# - Print all results
# ============================================================================

print("\n--- Task 4: String replacement ---")
# Your code here:

print(text.replace("Python", "Java"))
print(sentence.replace(" ", "_"))
print("apple apple".replace("apple", "orange", 1))

# ============================================================================
# Task 5: String stripping (removing whitespace)
# - Remove leading and trailing spaces from text using .strip()
# - Remove only leading spaces using .lstrip()
# - Remove only trailing spaces using .rstrip()
# - Print all results
# ============================================================================

print("\n--- Task 5: String stripping ---")
# Your code here:
print(text.strip())
print(text.lstrip(" "))
print(text.rstrip(" "))

# ============================================================================
# Task 6: String checking methods
# - Check if sentence starts with "hello" using .startswith()
# - Check if sentence ends with "python" using .endswith()
# - Check if "123" contains only digits using .isdigit()
# - Check if "Hello" contains only letters using .isalpha()
# - Check if "Hello123" is alphanumeric using .isalnum()
# - Print all results
# ============================================================================

print("\n--- Task 6: String checking methods ---")
# Your code here:
print(sentence.startswith("hello"))
print(sentence.endswith("python"))
print("123".isdigit())
print("Hello".isalpha())
print("Hello123".isalnum())

# ============================================================================
# Task 7: Finding and counting
# - Find the index of "world" in sentence using .find()
# - Count how many times "l" appears in sentence using .count()
# - Find the index of "z" in sentence (what happens if not found?)
# - Print all results
# ============================================================================

print("\n--- Task 7: Finding and counting ---")
# Your code here:
print(f'{sentence.find("world")}')
print(f'{sentence.count("l")}')
print(sentence.find('z'))


