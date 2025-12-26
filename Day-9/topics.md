List, Dictionary, and Set Comprehensions (basic, nested, with conditions), Generator Expressions
Convert previous list loops into single-line comprehensions for practice.

================================================================================
EXERCISE 1: LIST COMPREHENSIONS - Comprehensive Guide
================================================================================

1. WHAT ARE LIST COMPREHENSIONS?
   - Concise way to create lists in Python
   - One-line alternative to for loops
   - More readable and Pythonic
   - Example: [x**2 for x in range(5)] instead of a multi-line loop

2. BASIC SYNTAX:
   [expression for item in iterable]
   
   - expression: What to do with each item
   - for item in iterable: Loop through items
   - Result: New list with transformed items

3. BASIC LIST COMPREHENSION:
   - Pattern: [transform(item) for item in iterable]
   - Example: [x**2 for x in range(5)] → [0, 1, 4, 9, 16]
   - Example: [x*2 for x in [1, 2, 3]] → [2, 4, 6]
   - Applies transformation to each element

4. LIST COMPREHENSION WITH CONDITION (FILTERING):
   - Pattern: [expression for item in iterable if condition]
   - Example: [x for x in range(10) if x % 2 == 0] → [0, 2, 4, 6, 8]
   - Only includes items that meet the condition
   - The 'if' comes AFTER the 'for' loop

5. TRANSFORMATION WITH CONDITION:
   - Pattern: [transform(item) for item in iterable if condition]
   - Example: [x**2 for x in range(10) if x % 2 == 0] → [0, 4, 16, 36, 64]
   - First filters, then transforms
   - Only transforms items that pass the condition

6. LIST COMPREHENSION WITH IF-ELSE (TERNARY):
   - Pattern: [value_if_true if condition else value_if_false for item in iterable]
   - Example: ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
   - Returns different values based on condition
   - The if-else comes BEFORE the 'for' loop (unlike filtering)

7. NESTED LIST COMPREHENSIONS:
   - Pattern: [expression for outer in outer_iterable for inner in inner_iterable]
   - Example: [(x, y) for x in [1, 2] for y in [3, 4]]
   - Creates combinations/cartesian product
   - Outer loop first, then inner loop
   - Can create nested lists: [[i*j for j in range(3)] for i in range(3)]

8. MULTIPLE CONDITIONS:
   - Use 'and' or 'or' in the condition
   - Pattern: [expression for item in iterable if condition1 and condition2]
   - Example: [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
   - All conditions must be met (if using 'and')

9. COMPREHENSION VS TRADITIONAL LOOP:
   Traditional:
   squares = []
   for x in range(5):
       squares.append(x**2)
   
   Comprehension:
   squares = [x**2 for x in range(5)]
   
   - Same result, but comprehension is more concise
   - Comprehension is generally faster
   - More Pythonic (idiomatic Python)

10. READING ORDER (IMPORTANT):
    - Read from left to right, but understand the flow:
    - [expression for item in iterable if condition]
    - Flow: 1) Loop through iterable
            2) Check condition (if present)
            3) Apply expression
            4) Add to list

11. COMMON PATTERNS:
    - Transform all: [x**2 for x in numbers]
    - Filter: [x for x in numbers if x > 5]
    - Transform and filter: [x**2 for x in numbers if x > 5]
    - Conditional transform: [x if x > 5 else 0 for x in numbers]
    - String operations: [w.upper() for w in words]
    - Extract attributes: [len(w) for w in words]

12. WHEN TO USE LIST COMPREHENSIONS:
    - Creating new lists from existing iterables
    - Simple transformations and filtering
    - When you want concise, readable code
    - When performance matters (slightly faster than loops)

13. WHEN NOT TO USE:
    - Complex logic (use regular loops for clarity)
    - When you need side effects (printing, file operations)
    - When the expression is too complex to read

14. ADVANTAGES:
    - More concise than loops
    - More readable (once you understand the syntax)
    - Slightly faster execution
    - Pythonic (idiomatic Python style)

15. IMPORTANT NOTES:
    - Comprehensions create NEW lists (don't modify original)
    - Can use any iterable (lists, strings, ranges, etc.)
    - Can nest multiple levels (but be careful with readability)
    - The variable name (x, w, etc.) is local to the comprehension

================================================================================
EXERCISE 2: DICTIONARY AND SET COMPREHENSIONS - Comprehensive Guide
================================================================================

1. WHAT ARE DICTIONARY COMPREHENSIONS?
   - Concise way to create dictionaries in Python
   - Similar to list comprehensions, but creates key-value pairs
   - Uses curly braces {} instead of square brackets []
   - Syntax: {key: value for item in iterable}
   - Example: {x: x**2 for x in range(5)} → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

2. BASIC DICTIONARY COMPREHENSION SYNTAX:
   {key_expression: value_expression for item in iterable}
   
   - key_expression: What becomes the key
   - value_expression: What becomes the value
   - for item in iterable: Loop through items
   - Result: New dictionary with key-value pairs

3. BASIC DICTIONARY COMPREHENSION:
   - Pattern: {key: value for item in iterable}
   - Example: {x: x**2 for x in range(5)} → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
   - Example: {w: len(w) for w in ["apple", "banana"]} → {"apple": 5, "banana": 6}
   - Creates key-value pairs from each item

4. DICTIONARY COMPREHENSION WITH CONDITION (FILTERING):
   - Pattern: {key: value for item in iterable if condition}
   - Example: {x: x**2 for x in range(10) if x % 2 == 0} → {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
   - Only includes items that meet the condition
   - The 'if' comes AFTER the 'for' loop

5. DICTIONARY COMPREHENSION WITH IF-ELSE (TERNARY):
   - Pattern: {key: value_if_true if condition else value_if_false for item in iterable}
   - Example: {x: "Even" if x % 2 == 0 else "Odd" for x in range(5)}
   - Returns different values based on condition
   - The if-else comes BEFORE the 'for' loop (unlike filtering)

6. CREATING DICTIONARY FROM TWO LISTS:
   Method 1 - Using indexing:
   {names[i]: numbers[i] for i in range(len(names))}
   
   Method 2 - Using zip() (more Pythonic):
   {name: num for name, num in zip(names, numbers)}
   
   - zip() pairs elements from multiple iterables
   - More readable and handles different lengths better

7. NESTED DICTIONARY COMPREHENSION:
   - Pattern: {outer_key: {inner_key: expression for inner in inner_iterable} for outer in outer_iterable}
   - Example: {x: {y: x*y for y in range(1, 4)} for x in range(1, 4)}
   - Creates a dictionary where each value is itself a dictionary
   - Outer comprehension creates the main dictionary
   - Inner comprehension creates the nested dictionaries

8. WHAT ARE SET COMPREHENSIONS?
   - Concise way to create sets in Python
   - Similar to list comprehensions, but creates sets (unique elements)
   - Uses curly braces {} like dictionaries, but without key-value pairs
   - Syntax: {expression for item in iterable}
   - Example: {x**2 for x in range(5)} → {0, 1, 4, 9, 16}

9. BASIC SET COMPREHENSION SYNTAX:
   {expression for item in iterable}
   
   - expression: What to include in the set
   - for item in iterable: Loop through items
   - Result: New set with unique elements
   - Note: Sets automatically remove duplicates

10. BASIC SET COMPREHENSION:
    - Pattern: {transform(item) for item in iterable}
    - Example: {x**2 for x in range(5)} → {0, 1, 4, 9, 16}
    - Example: {len(w) for w in ["apple", "banana", "apple"]} → {5, 6} (duplicates removed)
    - Applies transformation and removes duplicates automatically

11. SET COMPREHENSION WITH CONDITION (FILTERING):
    - Pattern: {expression for item in iterable if condition}
    - Example: {x**2 for x in range(10) if x % 2 == 0} → {0, 4, 16, 36, 64}
    - Only includes items that meet the condition
    - The 'if' comes AFTER the 'for' loop

12. DICTIONARY VS SET COMPREHENSION - KEY DIFFERENCES:
    Dictionary: {key: value for item in iterable}  → Creates key-value pairs
    Set:        {expression for item in iterable}    → Creates unique values
    
    - Dictionary uses colon (:) to separate key and value
    - Set has no colon, just the expression
    - Both use curly braces {}

13. CONVERTING BETWEEN COMPREHENSIONS:
    List of tuples to dictionary:
    - List: [(x, x**2) for x in range(5)] → [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
    - Convert: dict([(x, x**2) for x in range(5)]) → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    - Direct: {x: x**2 for x in range(5)} → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    
    - dict() constructor can convert list of tuples to dictionary
    - Dictionary comprehension is more direct and efficient

14. COMMON PATTERNS:
    Dictionary:
    - Map to squares: {x: x**2 for x in numbers}
    - Map to lengths: {w: len(w) for w in words}
    - Filter keys: {x: x**2 for x in numbers if x > 5}
    - Conditional values: {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
    - From two lists: {name: age for name, age in zip(names, ages)}
    
    Set:
    - Unique squares: {x**2 for x in numbers}
    - Unique lengths: {len(w) for w in words}
    - Filtered unique: {x**2 for x in numbers if x > 5}
    - Unique characters: {char for char in "hello"} → {'h', 'e', 'l', 'o'}

15. WHEN TO USE DICTIONARY COMPREHENSIONS:
    - Creating dictionaries from existing iterables
    - Mapping one set of values to another
    - Filtering and transforming dictionary data
    - When you need key-value pairs

16. WHEN TO USE SET COMPREHENSIONS:
    - Creating sets from existing iterables
    - Removing duplicates automatically
    - Finding unique values
    - When you need unique elements only

17. ADVANTAGES OF DICTIONARY/SET COMPREHENSIONS:
    - More concise than loops
    - More readable (once you understand the syntax)
    - Slightly faster execution
    - Pythonic (idiomatic Python style)
    - Set comprehensions automatically handle uniqueness

18. IMPORTANT NOTES:
    - Dictionary comprehensions create NEW dictionaries (don't modify original)
    - Set comprehensions create NEW sets (don't modify original)
    - Dictionary keys must be unique (duplicate keys overwrite previous values)
    - Sets automatically remove duplicate values
    - Can use any iterable (lists, strings, ranges, etc.)
    - The variable name (x, w, etc.) is local to the comprehension
    - Dictionary comprehension requires key:value format
    - Set comprehension is just expression (no colon)

================================================================================
EXERCISE 3: GENERATOR EXPRESSIONS AND CONVERTING LOOPS - Comprehensive Guide
================================================================================

1. WHAT ARE GENERATOR EXPRESSIONS?
   - Similar to list comprehensions, but use parentheses () instead of brackets []
   - Syntax: (expression for item in iterable)
   - Creates a generator object (not a list)
   - Lazy evaluation: values are generated on-demand, not stored in memory
   - Example: (x**2 for x in range(5)) → generator object

2. BASIC GENERATOR EXPRESSION SYNTAX:
   (expression for item in iterable)
   
   - expression: What to generate
   - for item in iterable: Loop through items
   - Result: Generator object (not a list)
   - Must be consumed (converted to list, used in functions, or iterated)

3. GENERATOR VS LIST COMPREHENSION:
   List Comprehension: [x**2 for x in range(5)]
   - Creates entire list immediately
   - Stores all values in memory
   - Returns: [0, 1, 4, 9, 16]
   
   Generator Expression: (x**2 for x in range(5))
   - Creates generator object
   - Doesn't store values (lazy evaluation)
   - Returns: <generator object at 0x...>
   - Values generated only when needed

4. HOW TO USE GENERATORS:
   Method 1 - Convert to list:
   list((x**2 for x in range(5))) → [0, 1, 4, 9, 16]
   
   Method 2 - Use in functions that accept iterables:
   sum((x**2 for x in range(5))) → 30
   max((x**2 for x in range(5))) → 16
   min((x**2 for x in range(5))) → 0
   
   Method 3 - Iterate directly:
   for value in (x**2 for x in range(5)):
       print(value)

5. GENERATOR WITH CONDITION:
   - Pattern: (expression for item in iterable if condition)
   - Example: (x**2 for x in range(10) if x % 2 == 0) → even squares
   - Only generates values that meet the condition
   - Same syntax as list comprehensions, but with ()

6. MEMORY EFFICIENCY - KEY ADVANTAGE:
   List Comprehension (memory intensive):
   sum([x**2 for x in range(1000000)])
   - Creates list of 1,000,000 numbers in memory
   - Uses significant memory
   
   Generator Expression (memory efficient):
   sum((x**2 for x in range(1000000)))
   - Generates values one at a time
   - Uses minimal memory
   - Perfect for large datasets

7. WHEN TO USE GENERATORS:
   - Large datasets (memory efficient)
   - When you only need to iterate once
   - When you don't need random access (can't use indexing)
   - When using with functions like sum(), max(), min(), any(), all()
   - When processing data streams

8. WHEN NOT TO USE GENERATORS:
   - When you need the data multiple times (generators are consumed once)
   - When you need indexing or slicing
   - When you need to know the length (len() doesn't work)
   - When you need to modify the data

9. CONVERTING LOOPS TO LIST COMPREHENSIONS:
   
   Pattern 1 - Basic loop:
   Traditional:
   squares = []
   for x in range(5):
       squares.append(x**2)
   
   Comprehension:
   squares = [x**2 for x in range(5)]
   
   Pattern 2 - Loop with condition:
   Traditional:
   evens = []
   for x in numbers:
       if x % 2 == 0:
           evens.append(x)
   
   Comprehension:
   evens = [x for x in numbers if x % 2 == 0]
   
   Pattern 3 - Loop with transformation:
   Traditional:
   lengths = []
   for w in words:
       lengths.append(len(w))
   
   Comprehension:
   lengths = [len(w) for w in words]

10. CONVERTING NESTED LOOPS:
    Traditional:
    pairs = []
    for x in [1, 2]:
        for y in [3, 4]:
            pairs.append((x, y))
    
    Comprehension:
    pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
    
    - Outer loop first, then inner loop
    - Same order as nested loops

11. CONVERTING LOOPS TO DICTIONARY COMPREHENSIONS:
    Traditional:
    word_dict = {}
    for w in words:
        word_dict[w] = len(w)
    
    Comprehension:
    word_dict = {w: len(w) for w in words}
    
    - Pattern: {key: value for item in iterable}
    - Key and value can be expressions

12. CONVERTING LOOPS TO SET COMPREHENSIONS:
    Traditional:
    lengths_set = set()
    for w in words:
        lengths_set.add(len(w))
    
    Comprehension:
    lengths_set = {len(w) for w in words}
    
    - Pattern: {expression for item in iterable}
    - Automatically handles uniqueness

13. CONVERSION PATTERNS SUMMARY:
    Loop → List Comprehension:
    - result = []
    - for item in iterable:
    -     result.append(expression)
    → [expression for item in iterable]
    
    Loop with condition → List Comprehension:
    - result = []
    - for item in iterable:
    -     if condition:
    -         result.append(expression)
    → [expression for item in iterable if condition]
    
    Loop → Dictionary Comprehension:
    - result = {}
    - for item in iterable:
    -     result[key] = value
    → {key: value for item in iterable}
    
    Loop → Set Comprehension:
    - result = set()
    - for item in iterable:
    -     result.add(expression)
    → {expression for item in iterable}

14. GENERATOR EXPRESSIONS IN FUNCTION CALLS:
    - Can use generator expressions directly in function calls
    - No need for extra parentheses if it's the only argument
    - Example: sum(x**2 for x in range(5))  (outer parentheses optional)
    - Example: max(x for x in numbers if x > 5)
    - More memory efficient than passing lists

15. KEY DIFFERENCES SUMMARY:
    List Comprehension:     [x**2 for x in range(5)]  → List
    Generator Expression:  (x**2 for x in range(5))  → Generator
    Dictionary Comp:       {x: x**2 for x in range(5)} → Dictionary
    Set Comprehension:     {x**2 for x in range(5)}  → Set
    
    - List: Square brackets [], creates list immediately
    - Generator: Parentheses (), creates generator (lazy)
    - Dictionary: Curly braces {} with colon, creates dictionary
    - Set: Curly braces {} without colon, creates set

16. IMPORTANT NOTES:
    - Generators are consumed once (can't iterate twice)
    - Generators don't support indexing or slicing
    - Generators are memory efficient for large datasets
    - List comprehensions are faster for small datasets
    - Use generators when memory is a concern
    - Use list comprehensions when you need the data multiple times
    - Converting loops to comprehensions makes code more Pythonic
