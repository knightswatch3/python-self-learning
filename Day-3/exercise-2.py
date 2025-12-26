"""
Exercise 2: Comparison Operators

Problem:
You need to compare different values and understand how comparison operators work.

Given values:
- num1 = 10
- num2 = 5
- num3 = 10
- name1 = "Alice"
- name2 = "Bob"
- name3 = "Alice"

Your task:
1. Compare num1 and num2 using all comparison operators:
   - Is num1 == num2? (equal to)
   - Is num1 != num2? (not equal to)
   - Is num1 > num2? (greater than)
   - Is num1 < num2? (less than)
   - Is num1 >= num2? (greater than or equal to)
   - Is num1 <= num2? (less than or equal to)
   Print each result with a clear label.

2. Compare num1 and num3:
   - Check if they are equal (==)
   - Check if num1 is greater than or equal to num3 (>=)
   - Check if num1 is less than or equal to num3 (<=)
   Print the results.

3. Compare strings name1 and name2:
   - Check if they are equal
   - Check if name1 > name2 (lexicographic comparison)
   - Check if name1 < name2
   Print the results and explain what lexicographic comparison means.

4. Compare name1 and name3:
   - Check if they are equal
   Print the result.

5. Try comparing different types:
   - Can you compare a number and a string? Try: 5 == "5"
   - Print the result and explain what you observe.
"""

# Starting variables (given):
num1 = 10
num2 = 5
num3 = 10
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

# Your code here:

print(f'Is num1 == num2 : {num1 == num2}')
print(f'Is num1 != num2 : {num1 != num2}')
print(f'Is num1 > num2 : {num1 > num2}')
print(f'Is num1 < num2 : {num1 < num2}')
print(f'Is num1 >= num2 : {num1 >= num2}')
print(f'Is num1 <= num2 : {num1 <= num2}')

print('\npart-2')


print(f'Is num1 == num3 : {num1 == num3}')
print(f'Is num1 != num3 : {num1 <= num3}')
print(f'Is num1 > num3 : {num1 >= num3}')

print('\npart-3')

print(f'Equals: {name1 == name2}')
print(f'Greater: {name1 > name2}')
print(f'Lesser: {name1 < name2}')

print('\npart-4')
print(f'Equals: {name1 == name3}')



print(f'{ 5 == "5"}')