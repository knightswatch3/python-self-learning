"""
Exercise 3: Variable Scope Basics

Problem:
You have a global variable and a function. Your task is to understand how scope works.

Given code:
- A global variable `count = 10`
- A function `increment()` that should modify the count

Your task:
1. Create a function called `increment()` that adds 5 to the count variable
2. Print the count before calling the function
3. Call the function
4. Print the count after calling the function
5. Observe what happens - does the global count change?

Then:
6. Create a local variable inside the function with the same name `count = 20`
7. Print the local count inside the function
8. Print the global count after the function call
9. Explain what you observe about scope

Hint: Think about global vs local scope. You might need to use the `global` keyword.
"""

# Starting code (given):
count = 20

# Your code here:
print("Before", count)
# def increment():
#     global count
#     count=count+5
# increment()
# print("After", count)

def increment_2():
    print(f'{count} inside the function')
increment_2()
print("After", count)
