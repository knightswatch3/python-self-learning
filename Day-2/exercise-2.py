"""
Exercise 2: Type Conversion/Casting

Problem:
You have some data in different formats that need to be converted:
- Your age is stored as a string "25" but you need it as a number for calculations
- A price is stored as an integer 100 but needs to be a decimal number
- A test score is 95.5 (a float) but needs to be displayed as text in a message

Your task:
Convert each value to the appropriate type and verify the conversions worked.
Print each variable with its type to confirm the conversion.

Hint: Think about what functions convert between int, float, and str types.
"""

# Starting variables (given):
age_str = "25"
price_int = 100
score_float = 95.5
 
new_age_str=int(age_str)
new_price_int = float(price_int)
new_score_float = str(score_float)
# Your code here:
print(f'{new_age_str} is Age and type is {type(new_age_str)}')
print(f'{new_price_int} is Price {type((new_price_int))}')
print(f'{new_score_float} is Score {(type(new_score_float))}')

