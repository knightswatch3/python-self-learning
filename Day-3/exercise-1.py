"""
Exercise 1: Arithmetic Operators

Problem:
You're building a simple calculator. You need to perform various arithmetic operations.

Given values:
- num1 = 15
- num2 = 4

Your task:
1. Calculate and print the result of: num1 + num2
2. Calculate and print the result of: num1 - num2
3. Calculate and print the result of: num1 * num2
4. Calculate and print the result of: num1 / num2
5. Calculate and print the result of: num1 // num2
6. Calculate and print the result of: num1 % num2
7. Calculate and print the result of: num1 ** num2

Then:
8. Calculate: (10 + 5) * 2 - 8 / 4
   Print the result and explain the order of operations.

9. Use string operations:
   - Concatenate "Hello" and " World"
   - Repeat "Python " three times
   Print both results.
"""

# Starting variables (given):
num1 = 17
num2 = 4


# Your code here:


print(f'result of num1 + num2 : {num1 + num2}')
print(f'result of num1 - num2 : {num1 - num2}')
print(f'result of num1 * num2 : {num1 * num2}')
print(f'result of num1 / num2 : {num1 / num2}')
print(f'result of num1 // num2 : {num1 // num2}')
print(f'result of num1 % num2 : {num1 % num2}')
print(f'result of num1 ** num2 : {num1 ** num2}')

print((10 + 5) * 2 - 8 / 4, 'Should be 28 because as per BODMAS brackets take first preference then, 8/4 division and then the product of 15*2 and then the subtraction of 2 from it')

print("Hello"+" World")
print("Python " * 3) 