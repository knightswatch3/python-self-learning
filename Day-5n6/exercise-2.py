"""
Exercise 2: Loops (for, while, break, continue, pass, loop else)

Problem:
You need to learn how to repeat code execution using loops.
"""

# Starting variables (given):
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
text = "Python"

# ============================================================================
# Task 1: Basic for loop with list
# - Loop through the numbers list and print each number
# - Loop through the fruits list and print each fruit
# - Print results
# ============================================================================

print("\n--- Task 1: Basic for loop with list ---")
# Your code here:
for n in numbers:
    print(n)

for fruit in fruits:
    print(fruit)

# ============================================================================
# Task 2: for loop with range()
# - Use range(5) to print numbers 0 to 4
# - Use range(1, 6) to print numbers 1 to 5
# - Use range(0, 10, 2) to print even numbers 0 to 8 (step by 2)
# - Print results
# ============================================================================

print("\n--- Task 2: for loop with range() ---")
# Your code here:
for i in range(0,5):
    print(i)

for r in range(1,6):
    print(r)
print("\n")
for even in range(0,10,2):
    print(even)

# ============================================================================
# Task 3: for loop with string
# - Loop through the text string and print each character
# - Loop through text and print each character with its index (use enumerate)
# - Print results
# ============================================================================

print("\n--- Task 3: for loop with string ---")
# Your code here:
for i in text:
    print(i)

# ============================================================================
# Task 4: Basic while loop
# - Create a counter starting at 0
# - Use while loop to print numbers 0 to 4 (increment counter each time)
# - Print results
# ============================================================================

print("\n--- Task 4: Basic while loop ---")
# Your code here:
counter=0
while(counter<5):
    print(counter)
    counter = counter+1

# ============================================================================
# Task 5: while loop with condition
# - Start with count = 5
# - Use while loop to count down: print count, then decrement
# - Stop when count reaches 0
# - Print results
# ============================================================================

print("\n--- Task 5: while loop countdown ---")
# Your code here:
count = 5
while(count>0):
    print(count)
    count = count-1

# ============================================================================
# Task 6: break statement
# - Loop through numbers 1 to 10 using for loop
# - Break the loop when you reach 5
# - Print the numbers you looped through
# - Print results
# ============================================================================

print("\n--- Task 6: break statement ---")
# Your code here:
for i in range(1,10):
    if(i<5):
        break
    print("Value :", i)

# ============================================================================
# Task 7: continue statement
# - Loop through numbers 1 to 10 using for loop
# - Use continue to skip even numbers (only print odd numbers)
# - Print results
# ============================================================================

print("\n--- Task 7: continue statement ---")
# Your code here:
for i in range(1,10):
    if(i%2==0):
        continue
    else:
        print(i)


# ============================================================================
# Task 8: pass statement
# - Loop through numbers 1 to 5
# - Use if to check if number is 3
# - If it's 3, use pass (do nothing)
# - Otherwise, print the number
# - Print results
# ============================================================================

print("\n--- Task 8: pass statement ---")
# Your code here:

for i in range(1,5):
    if(i==3):
        pass
    else:
        print(i)

# ============================================================================
# Task 9: Loop else clause (for loop)
# - Loop through numbers 1 to 5
# - After the loop completes normally (without break), print "Loop completed"
# - Use else clause with the for loop
# - Print results
# ============================================================================

print("\n--- Task 9: Loop else clause (for loop) ---")
# Your code here:
for i in range(1,6):
    print(i)
else:
    print("loop completed")


# ============================================================================
# Task 10: Loop else clause with break
# - Loop through numbers 1 to 10
# - Break when you find 5
# - Add else clause that prints "Loop completed"
# - Observe: else does NOT execute when break is used
# - Print results
# ============================================================================

print("\n--- Task 10: Loop else with break ---")
# Your code here:
for i in range(1,10):
    if(i==5):
        break;
    else:
        print(i)
else:
    print("Loop completed")
# ============================================================================
# Task 11: Nested loops
# - Create nested for loops:
#   - Outer loop: range(3) - prints "Outer: 0", "Outer: 1", "Outer: 2"
#   - Inner loop: range(2) - prints "Inner: 0", "Inner: 1"
# - Print results to see the pattern
# ============================================================================

print("\n--- Task 11: Nested loops ---")
# Your code here:
for i in range(3):
    print("Outer", i)
    for j in range(2):
        print("Inner", j)


# ============================================================================
# Task 12: while loop with break
# - Create a while True loop
# - Ask user for input: number = int(input("Enter a number (0 to exit): "))
# - If number is 0, break the loop
# - Otherwise, print "You entered:", number
# - Print results
# ============================================================================

print("\n--- Task 12: while loop with break (interactive) ---")
# Your code here:
while True:
    number=int(input("Please enter a number(0 to exit)"))
    if(number==0):
        break;
    else:
        print("You entered:",number)

