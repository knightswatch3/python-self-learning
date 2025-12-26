"""
Exercise 1: Conditional Statements (if, elif, else, Nested, Ternary)

Problem:
You need to learn how to make decisions in your code using conditional statements.
"""

# Starting variables (given):
from os import minor


age = 20
score = 85
temperature = 25
number = 7

# ============================================================================
# Task 1: Basic if statement
# - Check if age is greater than or equal to 18
# - If true, print "You are an adult"
# - Print the result
# ============================================================================

print("\n--- Task 1: Basic if statement ---")
# Your code here:
if(age>=18):
    print("You are an adult") 

# ============================================================================
# Task 2: if-else statement
# - Check if score is greater than or equal to 60
# - If true, print "You passed"
# - Otherwise (else), print "You failed"
# - Print the result
# ============================================================================

print("\n--- Task 2: if-else statement ---")
# Your code here:

if(score>=60):
    print("You Passed") 
else:
    print("You failed")

# ============================================================================
# Task 3: if-elif-else statement
# - Check temperature:
#   - If temperature > 30: print "It's hot"
#   - Else if temperature > 20: print "It's warm"
#   - Else if temperature > 10: print "It's cool"
#   - Else: print "It's cold"
# - Print the result
# ============================================================================

print("\n--- Task 3: if-elif-else statement ---")
# Your code here:

if(int(temperature) > 30):
    print("It's hot")
elif(int(temperature) > 20):
    print("It's warm")
elif(int(temperature) > 10):
    print("It's cool")
else:
    print("It's cold")
# ============================================================================
# Task 4: Multiple conditions with and/or
# - Check if age is between 18 and 65 (inclusive) using 'and'
# - If true, print "Working age"
# - Check if score is above 90 OR age is below 18 using 'or'
# - If true, print "Special category"
# - Print results
# ============================================================================

print("\n--- Task 4: Multiple conditions (and/or) ---")
# Your code here:
if(age>=18 and age<65):
    print("Working age")
if(age>=90 or age<18):
    print("Special category")


# ============================================================================
# Task 5: Nested conditionals
# - Check if number is positive
#   - If positive, check if it's even or odd
#     - If even: print "Positive even number"
#     - If odd: print "Positive odd number"
#   - If not positive, print "Number is not positive"
# - Print the result
# ============================================================================

print("\n--- Task 5: Nested conditionals ---")
# Your code here:

if(number>0):
    if(number%2==0):
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")

# ============================================================================
# Task 6: Ternary expressions (conditional expressions)
# - Use ternary to assign: status = "Adult" if age >= 18 else "Minor"
# - Use ternary to assign: result = "Pass" if score >= 60 else "Fail"
# - Use ternary in print: print("Even" if number % 2 == 0 else "Odd")
# - Print all results
# ============================================================================

print("\n--- Task 6: Ternary expressions ---")
# Your code here:
status =  "Adult" if age>=18 else "minor"
result =  "Pass" if score>=60 else "Fail"
print("Even" if number%2==0 else "Odd")

# ============================================================================
# Task 7: Complex nested conditions
# - Check if age >= 18:
#   - If true, check if score >= 80:
#     - If true: print "Adult with high score"
#     - Else: print "Adult with low score"
#   - Else (age < 18):
#     - Check if score >= 80:
#       - If true: print "Minor with high score"
#       - Else: print "Minor with low score"
# - Print the result
# ============================================================================

print("\n--- Task 7: Complex nested conditions ---")
# Your code here:
if(age>=18):
    print("Adult with " "high score" if score>=80 else "low score" )
else:
    print("Minot with " "high score" if score>=80 else "low score" )


