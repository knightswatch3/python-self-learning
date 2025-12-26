Data Structures: Tuples & Sets
Tuples (packing/unpacking, immutability), Sets (operations, frozenset)
Use sets to find common elements between two lists (union, intersection).

================================================================================
EXERCISE 1: TUPLES - Key Concepts Summary
================================================================================

1. WHAT ARE TUPLES?
   - Ordered, immutable sequences
   - Created with parentheses () or just commas
   - Example: (1, 2, 3) or 1, 2, 3

2. KEY CHARACTERISTICS:
   - Immutable: Cannot be changed after creation
   - Ordered: Elements have defined order
   - Indexed: Access by position (starts at 0)
   - Allow duplicates: Same value can appear multiple times

3. TUPLE PACKING:
   - Putting values together into a tuple
   - Example: my_tuple = 1, 2, 3 (no parentheses needed)

4. TUPLE UNPACKING:
   - Extracting values from tuple into separate variables
   - Example: x, y = (3, 4) → x=3, y=4
   - Number of variables must match number of elements

5. MULTIPLE ASSIGNMENT (SWAPPING):
   - a, b = b, a swaps values
   - Works because Python creates tuple then unpacks

6. IMMUTABILITY:
   - Cannot modify: tuple[0] = 10 → TypeError
   - Cannot add/remove: tuple.append() → AttributeError
   - Slicing creates new tuple (doesn't modify original)

7. TUPLE OPERATIONS:
   - Indexing: tuple[0], tuple[-1]
   - Slicing: tuple[1:3], tuple[::-1]
   - Membership: value in tuple
   - Length: len(tuple)

8. TUPLE METHODS (only 2):
   - count(value): Count occurrences
   - index(value): Find first index

9. NESTED TUPLES:
   - Tuples can contain other tuples
   - Access: nested[0][1]

10. CONVERTING:
    - tuple to list: list(tuple)
    - list to tuple: tuple(list)

11. SINGLE-ELEMENT TUPLE:
    - Must have comma: (5,) not (5)
    - (5) is just an integer, not a tuple

================================================================================
EXERCISE 2: SETS - Key Concepts Summary
================================================================================

1. WHAT ARE SETS?
   - Unordered, mutable collections of unique elements
   - No duplicates allowed
   - Created with {} or set()

2. KEY CHARACTERISTICS:
   - Unordered: No defined order
   - Mutable: Can add/remove elements
   - Unique: No duplicate values
   - Unindexed: Cannot access by position

3. SET OPERATIONS:
   - Union (| or .union()): All elements from both sets
   - Intersection (& or .intersection()): Common elements
   - Difference (- or .difference()): Elements in first but not second
   - Symmetric Difference (^ or .symmetric_difference()): Elements in either but not both

4. SET METHODS:
   - add(): Add single element
   - update(): Add multiple elements
   - remove(): Remove element (errors if not exists)
   - discard(): Remove element (no error if not exists)
   - pop(): Remove and return arbitrary element

5. SET COMPARISON:
   - issubset() or <= : Check if subset
   - issuperset() or >= : Check if superset
   - isdisjoint(): Check if no common elements

6. FROZENSET:
   - Immutable version of set
   - Cannot add/remove elements
   - Can use set operations (returns new frozenset)

7. CONVERTING LISTS TO SETS:
   - Removes duplicates: set([1,2,2,3]) → {1,2,3}

================================================================================
EXERCISE 3: PRACTICAL APPLICATION
================================================================================

Use sets to find common elements between lists:
- Convert lists to sets
- Use intersection() or & for common elements
- Use union() or | for all unique elements
- Use difference() or - for elements in one but not other
- Use symmetric_difference() or ^ for elements in either but not both
