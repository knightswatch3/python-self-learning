"""
Exercise 3: Logical Operators

Problem:
You need to understand how logical operators work to combine multiple conditions.
"""

# Starting variables (given):
age = 25
has_license = True
has_car = False
score = 85
is_student = True

# ============================================================================
# Task 1: Use the `and` operator
# - Check if age >= 18 AND has_license is True
# - Check if age >= 18 AND has_car is True
# - Print both results and explain when `and` returns True.
# ============================================================================

# Your code here:
print(f'{age >= 18 and has_license}')
print(f'{age >= 18 and has_car}')

# ============================================================================
# Task 2: Use the `or` operator
# - Check if has_license OR has_car is True
# - Check if age < 18 OR is_student is True
# - Print both results and explain when `or` returns True.
# ============================================================================

# Your code here:

print(f'{has_car or has_license}')
print(f'{age < 18 or is_student}')

# ============================================================================
# Task 3: Use the `not` operator
# - Check if NOT has_car
# - Check if NOT (age < 18)
# - Print both results and explain what `not` does.
# ============================================================================

# Your code here:
print(f'{not has_car}')
print(f'{not age<18}')

# ============================================================================
# Task 4: Combine multiple operators
# - Check if (age >= 18 AND has_license) OR has_car
# - Check if score >= 80 AND (is_student OR age < 25)
# - Print both results.
# ============================================================================

# Your code here:

print(f'{(age >= 18 and has_license) or has_car}')
print(f'{score >= 80 and (is_student or age < 25)}')

# ============================================================================
# Task 5: Truthiness
# - Try: `not 0` (what does this return?)
# - Try: `not ""` (empty string)
# - Try: `not None`
# - Try: `5 and 10` (what does this return?)
# - Try: `0 or 5` (what does this return?)
# - Print all results and observe what Python considers "truthy" and "falsy".
# ============================================================================

# Your code here:

print(f'{not 0}')
print(f'{not ""}')
print(f'{not None}')
print(f'{5 and 10}')
print(f'{0 or 5}')


