# *args and **kwargs - Study Notes for Exercise 3

## 1. What is *args?

**`*args`** allows a function to accept **any number of positional arguments**.
- The `*` unpacks arguments into a tuple
- `args` is just a convention (you can use any name like `*numbers`, `*values`, etc.)
- All extra positional arguments are collected into a tuple

### Basic Syntax:
```python
def function(*args):
    # args is a tuple of all positional arguments
    # You can iterate over it, index it, etc.
```

### Example 1: Sum all arguments
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
    # Or simply: return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10))             # 10
print(sum_all())               # 0 (empty tuple)
```

### Example 2: Accessing args as tuple
```python
def show_args(*args):
    print(f"Type: {type(args)}")  # <class 'tuple'>
    print(f"Args: {args}")        # (1, 2, 3)
    print(f"First: {args[0]}")    # 1
    print(f"Length: {len(args)}") # 3

show_args(1, 2, 3)
```

---

## 2. *args with Regular Parameters

**Important rule**: Regular parameters must come **before** `*args`

### Syntax:
```python
def function(regular_param, *args):
    # regular_param gets the first argument
    # *args gets all remaining positional arguments
```

### Example: Greeting multiple people
```python
def greet_many(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_many("Hello", "Alice", "Bob", "Charlie")
# greeting = "Hello"
# names = ("Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Order matters!
```python
# ✅ CORRECT:
def func(a, b, *args):
    pass

# ❌ WRONG (will cause error):
def func(*args, a, b):
    pass
```

---

## 3. What is **kwargs?

**`**kwargs`** allows a function to accept **any number of keyword arguments**.
- The `**` unpacks keyword arguments into a dictionary
- `kwargs` is just a convention (you can use any name like `**options`, `**data`, etc.)
- All extra keyword arguments are collected into a dictionary

### Basic Syntax:
```python
def function(**kwargs):
    # kwargs is a dictionary of all keyword arguments
    # Access like: kwargs['key'] or kwargs.get('key')
```

### Example: Print all information
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Example: Accessing kwargs as dictionary
```python
def show_kwargs(**kwargs):
    print(f"Type: {type(kwargs)}")  # <class 'dict'>
    print(f"Kwargs: {kwargs}")      # {'a': 1, 'b': 2}
    print(f"Value of 'a': {kwargs.get('a')}")  # 1

show_kwargs(a=1, b=2, c=3)
```

---

## 4. Combining *args and **kwargs

**Important rule**: The order must be:
1. Regular parameters
2. `*args`
3. `**kwargs`

### Syntax:
```python
def function(regular_param, *args, **kwargs):
    # regular_param: first positional argument
    # args: tuple of remaining positional arguments
    # kwargs: dictionary of keyword arguments
```

### Example: Flexible function
```python
def flexible_function(title, *numbers, **metadata):
    print(f"Title: {title}")
    print(f"Numbers: {numbers}")  # tuple
    print(f"Sum: {sum(numbers)}")
    print("Metadata:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")

flexible_function("Data", 1, 2, 3, 4, author="John", date="2024")
# Output:
# Title: Data
# Numbers: (1, 2, 3, 4)
# Sum: 10
# Metadata:
#   author: John
#   date: 2024
```

### Complete example:
```python
def my_function(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

my_function(1, 2, 3, 4, 5, x=10, y=20)
# Output:
# a=1, b=2
# args=(3, 4, 5)
# kwargs={'x': 10, 'y': 20}
```

---

## 5. Unpacking with * (Unpacking lists/tuples)

Use `*` to **unpack** a list or tuple when calling a function.

### Example: Unpacking a list
```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add_three(*numbers)  # Unpacks to: add_three(1, 2, 3)
print(result)  # 6

# Without unpacking (would cause error):
# add_three(numbers)  # ❌ Error: expects 3 arguments, got 1
```

### Example: Unpacking in print
```python
numbers = [1, 2, 3]
print(*numbers)  # Unpacks to: print(1, 2, 3)
# Output: 1 2 3
```

---

## 6. Unpacking with ** (Unpacking dictionaries)

Use `**` to **unpack** a dictionary when calling a function.

### Example: Unpacking a dictionary
```python
def create_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

info = {"name": "Alice", "age": 25, "city": "NYC"}
create_profile(**info)  # Unpacks to: create_profile(name="Alice", age=25, city="NYC")
# Output: Name: Alice, Age: 25, City: NYC

# Without unpacking (would cause error):
# create_profile(info)  # ❌ Error: expects 3 keyword arguments
```

### Dictionary keys must match parameter names
```python
def greet(name, age):
    print(f"{name} is {age}")

data = {"name": "Bob", "age": 30}
greet(**data)  # ✅ Works

wrong_data = {"first_name": "Bob", "years": 30}
greet(**wrong_data)  # ❌ Error: keys don't match parameters
```

---

## 7. Practical Examples

### Example 1: Custom print function
```python
def my_print(*args, sep=" ", end="\n"):
    # Join all args with separator
    result = sep.join(str(arg) for arg in args)
    print(result, end=end)

my_print(1, 2, 3, sep="-", end="!")
# Output: 1-2-3!

my_print("Hello", "World")
# Output: Hello World
```

### Example 2: Flexible calculator
```python
def calculate(*numbers, operation="sum"):
    if operation == "sum":
        return sum(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)

print(calculate(1, 2, 3, 4))                    # 10 (default: sum)
print(calculate(1, 2, 3, 4, operation="product")) # 24
print(calculate(1, 2, 3, 4, operation="max"))     # 4
```

### Example 3: Function with defaults and kwargs
```python
def process_data(title, *values, **options):
    print(f"Title: {title}")
    print(f"Values: {values}")
    
    # Get options with defaults
    verbose = options.get("verbose", False)
    limit = options.get("limit", 10)
    
    if verbose:
        print("Verbose mode enabled")
    print(f"Limit: {limit}")

process_data("Results", 1, 2, 3, verbose=True, limit=5)
```

---

## 8. Key Points to Remember

1. **Order matters**: `regular_params, *args, **kwargs`
2. **`*args`** collects positional arguments into a **tuple**
3. **`**kwargs`** collects keyword arguments into a **dictionary**
4. **Unpacking `*`**: Use when calling functions with lists/tuples
5. **Unpacking `**`**: Use when calling functions with dictionaries
6. **Naming**: `args` and `kwargs` are conventions, you can use any names
7. **Optional**: Both `*args` and `**kwargs` can be empty

---

## 9. Common Mistakes to Avoid

### ❌ Wrong order:
```python
def wrong(*args, regular_param):  # Error!
    pass
```

### ❌ Wrong unpacking:
```python
numbers = [1, 2, 3]
def add(a, b, c):
    return a + b + c
result = add(numbers)  # ❌ Should be: add(*numbers)
```

### ❌ Wrong dictionary unpacking:
```python
info = {"name": "Alice", "age": 25}
def greet(name, age):
    print(f"{name} is {age}")
greet(info)  # ❌ Should be: greet(**info)
```

---

## 10. Quick Reference

```python
# Defining functions:
def func(param, *args, **kwargs):
    pass

# Calling with unpacking:
func(1, *[2, 3], **{"key": "value"})

# *args = tuple of positional arguments
# **kwargs = dict of keyword arguments
# *list = unpacks list to positional args
# **dict = unpacks dict to keyword args
```

Good luck with Exercise 3! 🚀

