"""
Exercise 2: String Formatting (F-strings, .format(), % operator)

Problem:
You need to learn different ways to format strings in Python.
"""

# Starting variables (given):
name = "Alice"
age = 25
score = 95.5
item = "book"
price = 19.99
quantity = 3

# ============================================================================
# Task 1: F-strings (f-strings) - Modern Python way
# - Create an f-string: "My name is {name} and I am {age} years old"
# - Create an f-string with calculation: "I have {quantity} items, total: ${quantity * price}"
# - Create an f-string with formatting: "Score: {score:.2f}" (2 decimal places)
# - Print all results
# ============================================================================

print("\n--- Task 1: F-strings ---")
# Your code here:
print(f'My name is {name} and I am {age} years old')
print(f'I have {quantity} items, total: ${quantity * price}')
print(f'Score: {score:.2f}')

# ============================================================================
# Task 2: .format() method - Older but still common
# - Use .format() with positional arguments: "Hello, {}! You are {} years old".format(name, age)
# - Use .format() with named arguments: "Hello, {n}! You are {a} years old".format(n=name, a=age)
# - Use .format() with index: "First: {0}, Second: {1}, First again: {0}".format(name, age)
# - Use .format() with formatting: "Price: ${:.2f}".format(price)
# - Print all results
# ============================================================================

print("\n--- Task 2: .format() method ---")
# Your code here:
print('Hello, {}! You are {} years old'.format(name, age))
print('Hello, {n}! You are {a} years old'.format(n=name, a=age))
print('First: {0}, Second: {1}, First again'.format(name,age))
print('Price: {0:.2f}'.format(price))

# ============================================================================
# Task 3: % operator (Old-style formatting) - Legacy but still used
# - Use %s for strings: "Hello, %s!" % name
# - Use %d for integers: "Age: %d" % age
# - Use %f for floats: "Score: %.2f" % score (2 decimal places)
# - Use multiple values: "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
# - Print all results
# ============================================================================

print("\n--- Task 3: % operator (old-style) ---")
# Your code here:

print("Hello %s!" %name)
print("Age %d!" %age)
print("Score %.2f!" %score)
print("Name: %s, Age: %d, Score: %.2f" %(name, age, score))

# ============================================================================
# Task 4: Comparison - Same output, different methods
# - Format this message using all three methods: "Alice is 25 years old and scored 95.50"
# - Use f-string
# - Use .format()
# - Use % operator
# - Print all three (they should produce the same output)
# ============================================================================

print("\n--- Task 4: Comparison (same output, different methods) ---")
# Your code here:
print(f"{name} is {age} years old and scored {score:.2f}")
print('{} is {} years old and scored {:.2f}'.format(name, age, float(score,)))
print('%s is %d years old and scored %.2f' %(name, age, score))

# ============================================================================
# Task 5: Advanced formatting
# - F-string with alignment: f"{name:>10}" (right align, 10 chars wide)
# - F-string with padding: f"{age:05d}" (zero-padded, 5 digits)
# - .format() with alignment: "{:^20}".format(name) (center align, 20 chars)
# - % operator with padding: "%05d" % age (zero-padded, 5 digits)
# - Print all results
# ============================================================================

print("\n--- Task 5: Advanced formatting ---")
# Your code here:
print(f'{name:>10}')
print(f'{age:05d}')
print("{:^20}".format(name))
print("%05d"%(age))

