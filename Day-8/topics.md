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
EXERCISE 2: SETS - Comprehensive Guide
================================================================================

1. WHAT ARE SETS?
   - Unordered, mutable collections of unique elements
   - No duplicates allowed (automatically removed)
   - Created with curly braces {} or set() function
   - Example: {1, 2, 3} or set([1, 2, 3])

2. KEY CHARACTERISTICS:
   - Unordered: Elements have no defined order (order may change)
   - Mutable: Can add/remove elements after creation
   - Unique: No duplicate values (duplicates automatically removed)
   - Unindexed: Cannot access elements by position (no [0], [1], etc.)
   - Hashable elements only: Can only contain immutable types (numbers, strings, tuples)

3. CREATING SETS:
   - With curly braces: my_set = {1, 2, 3}
   - With set() function: my_set = set([1, 2, 3])
   - Empty set: my_set = set() (NOT {} - that's an empty dict!)
   - From string: set("hello") → {'h', 'e', 'l', 'o'} (removes duplicates)

4. SET OPERATIONS - UNION (All elements from both sets):
   - Method: set1.union(set2)
   - Operator: set1 | set2
   - Example: {1,2,3} | {3,4,5} → {1,2,3,4,5}
   - Returns new set (doesn't modify originals)

5. SET OPERATIONS - INTERSECTION (Common elements):
   - Method: set1.intersection(set2)
   - Operator: set1 & set2
   - Example: {1,2,3} & {3,4,5} → {3}
   - Returns new set with common elements

6. SET OPERATIONS - DIFFERENCE (Elements in first but not second):
   - Method: set1.difference(set2)
   - Operator: set1 - set2
   - Example: {1,2,3} - {3,4,5} → {1,2}
   - Returns elements in set1 but not in set2

7. SET OPERATIONS - SYMMETRIC DIFFERENCE (Elements in either but not both):
   - Method: set1.symmetric_difference(set2)
   - Operator: set1 ^ set2
   - Example: {1,2,3} ^ {3,4,5} → {1,2,4,5}
   - Returns elements in either set but not in both

8. ADDING ELEMENTS:
   - add(element): Add single element
     Example: my_set.add(4)
   - update(iterable): Add multiple elements
     Example: my_set.update([4, 5, 6])
     Can update with any iterable (list, tuple, another set, string)

9. REMOVING ELEMENTS:
   - remove(element): Remove element, raises KeyError if not exists
     Example: my_set.remove(3)
   - discard(element): Remove element, does nothing if not exists
     Example: my_set.discard(3) (safer than remove)
   - pop(): Remove and return arbitrary element, raises KeyError if empty
     Example: element = my_set.pop()
   - clear(): Remove all elements
     Example: my_set.clear()

10. SET COMPARISON METHODS:
    - issubset(other): Check if all elements are in other set
      Operator: set1 <= set2
      Example: {1,2}.issubset({1,2,3}) → True
    - issuperset(other): Check if all elements of other are in this set
      Operator: set1 >= set2
      Example: {1,2,3}.issuperset({1,2}) → True
    - isdisjoint(other): Check if sets have no common elements
      Example: {1,2}.isdisjoint({3,4}) → True

11. OTHER SET OPERATIONS:
    - Membership: element in set (check if element exists)
    - Length: len(set) (number of elements)
    - Loop: for item in set: (iterate through elements)
    - Copy: new_set = set.copy() or new_set = set(set)

12. FROZENSET (Immutable Set):
    - Created with: frozenset([1, 2, 3])
    - Cannot add/remove elements after creation
    - Can use set operations (union, intersection, etc.) - returns new frozenset
    - Can be used as dictionary keys (because it's immutable)
    - Example: frozen = frozenset([1, 2, 3])
      frozen.add(4) → AttributeError (cannot modify)

13. CONVERTING LISTS TO SETS (Removing Duplicates):
    - set([1,2,2,3,3,3]) → {1,2,3} (removes duplicates)
    - list(set([1,2,2,3])) → [1,2,3] (convert back to list)
    - Common pattern: unique_list = list(set(duplicate_list))

14. SET COMPREHENSION (Advanced):
    - Similar to list comprehension but creates sets
    - Example: {x**2 for x in range(5)} → {0, 1, 4, 9, 16}
    - Example: {x for x in range(10) if x % 2 == 0} → {0, 2, 4, 6, 8}

15. IMPORTANT NOTES:
    - Empty set: Use set() not {} ({} is empty dictionary)
    - Sets cannot contain lists or other sets (but can contain frozensets)
    - Sets can contain tuples (because tuples are immutable)
    - Order is not guaranteed (may appear in different order each time)
    - Sets are faster than lists for membership testing (in operator)

16. COMMON USE CASES:
    - Removing duplicates from lists
    - Fast membership testing
    - Finding common/unique elements between collections
    - Mathematical set operations
    - Tagging/categorization systems

================================================================================
EXERCISE 3: PRACTICAL APPLICATION - Finding Common Elements
================================================================================

CONCEPT: Using Sets to Compare Lists

The main idea is to convert lists to sets, perform set operations, then convert
back to lists if needed. This is useful for finding relationships between
collections of data.

1. WHY CONVERT LISTS TO SETS?
   - Sets automatically remove duplicates
   - Set operations are fast and efficient
   - Set operations are designed for comparing collections
   - Lists don't have built-in intersection/union operations

2. THE WORKFLOW:
   Step 1: Convert lists to sets → set(list1), set(list2)
   Step 2: Perform set operation → result_set = set1.operation(set2)
   Step 3: Convert back to list (if needed) → list(result_set)
   Step 4: Sort (if order matters) → sorted(list(result_set))

3. INTERSECTION - Finding Common Elements:
   - Concept: Elements that appear in BOTH collections
   - Use case: "Which students are in both classes?"
   - Method: set1.intersection(set2) or set1 & set2
   - Result: New set containing only common elements

4. UNION - Finding All Unique Elements:
   - Concept: All elements from BOTH collections (no duplicates)
   - Use case: "What are all the unique items across both lists?"
   - Method: set1.union(set2) or set1 | set2
   - Result: New set containing all unique elements

5. DIFFERENCE - Finding Elements in One but Not Other:
   - Concept: Elements in first collection but NOT in second
   - Use case: "What items are only in list1?"
   - Method: set1.difference(set2) or set1 - set2
   - Result: New set with elements in set1 but not in set2
   - Note: set2 - set1 gives elements only in set2

6. SYMMETRIC DIFFERENCE - Finding Elements in Either but Not Both:
   - Concept: Elements in EITHER collection but NOT in both
   - Use case: "What items are unique to each list (not shared)?"
   - Method: set1.symmetric_difference(set2) or set1 ^ set2
   - Result: New set with elements in either but not both

7. REAL-WORLD APPLICATIONS:
   - Finding common friends between two users
   - Finding students in multiple classes
   - Finding products in multiple categories
   - Finding tags common to multiple items
   - Data analysis and comparison

8. IMPORTANT CONSIDERATIONS:
   - Sets are unordered, so convert to list and sort if order matters
   - Sets remove duplicates automatically
   - All set operations return NEW sets (don't modify originals)
   - Can chain operations: set1.union(set2).intersection(set3)

9. CONVERTING BACK TO LISTS:
   - Use list() to convert set back to list
   - Use sorted() if you need ordered results
   - Example: sorted(list(set1 & set2))

10. FUNCTION CREATION:
    - You can create reusable functions that take two lists
    - Convert to sets inside the function
    - Perform operation
    - Return result (as list or set, depending on need)
