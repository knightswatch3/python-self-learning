"""
Exercise 2: Working with Packages

Problem:
You need to understand how to create and use packages (directories with multiple modules).
"""

# ============================================================================
# Task 1: Understand what a package is
# A package is a directory containing multiple Python modules
# It must have an __init__.py file (can be empty)
# ============================================================================

print("--- Task 1: Understanding Packages ---")
print("A package is a folder with multiple .py files (modules)")
print("It needs an __init__.py file to be recognized as a package")

# ============================================================================
# Task 2: Create a package structure
# 1. Create a directory called 'math_utils'
# 2. Create __init__.py file inside it
# 3. Create two modules: basic.py and advanced.py
# ============================================================================

print("\n--- Task 2: Creating Package Structure ---")

import os

# Create package directory
package_name = "math_utils"
if not os.path.exists(package_name):
    os.makedirs(package_name)
    print(f"Created directory: {package_name}/")

# Create __init__.py (can be empty, but we'll add some code)
init_content = '''"""
Math utilities package.
This package contains basic and advanced math operations.
"""

# You can import things here to make them available at package level
from .basic import add, subtract, multiply, divide
from .advanced import power, square_root

__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'square_root']
'''

with open(f"{package_name}/__init__.py", "w") as f:
    f.write(init_content)
print(f"Created {package_name}/__init__.py")

# Create basic.py module
basic_content = '''"""
Basic math operations module.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
'''

with open(f"{package_name}/basic.py", "w") as f:
    f.write(basic_content)
print(f"Created {package_name}/basic.py")

# Create advanced.py module
advanced_content = '''"""
Advanced math operations module.
"""

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def square_root(number):
    """Calculate square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return number ** 0.5

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
'''

with open(f"{package_name}/advanced.py", "w") as f:
    f.write(advanced_content)
print(f"Created {package_name}/advanced.py")

print(f"\nPackage structure created:")
print(f"{package_name}/")
print(f"  __init__.py")
print(f"  basic.py")
print(f"  advanced.py")

# ============================================================================
# Task 3: Import from package - Method 1 (import entire module)
# 1. Import the basic module from math_utils package
# 2. Use functions with package.module.function() syntax
# ============================================================================

print("\n--- Task 3: Import entire module from package ---")
# Your code here:
import math_utils.basic as basic_math

result1 = basic_math.add(10, 5)
result2 = basic_math.multiply(4, 7)
print(f"10 + 5 = {result1}")
print(f"4 * 7 = {result2}")

# ============================================================================
# Task 4: Import from package - Method 2 (from package import module)
# 1. Use 'from math_utils import basic'
# 2. Call functions using module.function()
# ============================================================================

print("\n--- Task 4: Import module using from...import ---")
# Your code here:
from math_utils import basic

result3 = basic.divide(20, 4)
result4 = basic.subtract(15, 8)
print(f"20 / 4 = {result3}")
print(f"15 - 8 = {result4}")

# ============================================================================
# Task 5: Import specific functions from package module
# 1. Use 'from math_utils.advanced import power, square_root'
# 2. Call functions directly without module prefix
# ============================================================================

print("\n--- Task 5: Import specific functions from package ---")
# Your code here:
from math_utils.advanced import power, square_root

result5 = power(2, 8)
result6 = square_root(64)
print(f"2^8 = {result5}")
print(f"√64 = {result6}")

# ============================================================================
# Task 6: Import from __init__.py (package-level imports)
# 1. Since we imported functions in __init__.py, we can use them directly
# 2. Try: from math_utils import add, multiply
# ============================================================================

print("\n--- Task 6: Import from package __init__.py ---")
# Your code here:
from math_utils import add, multiply, power, square_root

result7 = add(100, 200)
result8 = multiply(6, 7)
result9 = power(3, 4)
print(f"100 + 200 = {result7}")
print(f"6 * 7 = {result8}")
print(f"3^4 = {result9}")

# ============================================================================
# Task 7: Import entire package
# 1. Import the package: import math_utils
# 2. Access modules: math_utils.basic.add()
# ============================================================================

print("\n--- Task 7: Import entire package ---")
# Your code here:
import math_utils

# Access through package
result10 = math_utils.basic.add(50, 25)
result11 = math_utils.advanced.factorial(5)
print(f"50 + 25 = {result10}")
print(f"5! = {result11}")

# ============================================================================
# Task 8: Create a nested package (package inside package)
# 1. Create a 'geometry' package inside 'math_utils'
# 2. Create a 'shapes.py' module inside 'geometry'
# 3. Import and use it
# ============================================================================

print("\n--- Task 8: Create nested package ---")

# Create nested package
geometry_path = f"{package_name}/geometry"
if not os.path.exists(geometry_path):
    os.makedirs(geometry_path)

# Create __init__.py for geometry package
geometry_init = '''"""
Geometry package for shape calculations.
"""
'''

with open(f"{geometry_path}/__init__.py", "w") as f:
    f.write(geometry_init)
print(f"Created {package_name}/geometry/__init__.py")

# Create shapes.py
shapes_content = '''"""
Shape calculation functions.
"""

def circle_area(radius):
    """Calculate area of a circle."""
    return 3.14159 * radius ** 2

def rectangle_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height
'''

with open(f"{geometry_path}/shapes.py", "w") as f:
    f.write(shapes_content)
print(f"Created {package_name}/geometry/shapes.py")

# Import and use nested package
from math_utils.geometry import shapes

area1 = shapes.circle_area(5)
area2 = shapes.rectangle_area(4, 6)
print(f"Circle area (r=5): {area1:.2f}")
print(f"Rectangle area (4x6): {area2}")

# ============================================================================
# Task 9: Understand __all__ in packages
# 1. Check what __all__ does in __init__.py
# 2. It controls what gets imported with 'from package import *'
# ============================================================================

print("\n--- Task 9: Understanding __all__ ---")
print("__all__ in __init__.py controls what's available with 'import *'")
print("In our __init__.py, we defined:")
print("__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'square_root']")

# You can use import * (though not recommended)
from math_utils import *
result12 = add(1, 2)
result13 = power(2, 3)
print(f"Using import *: add(1, 2) = {result12}")
print(f"Using import *: power(2, 3) = {result13}")

# ============================================================================
# Task 10: Package vs Module comparison
# 1. Understand the difference
# 2. When to use packages vs single modules
# ============================================================================

print("\n--- Task 10: Package vs Module ---")
print("\nMODULE:")
print("  - Single .py file")
print("  - Example: file_utils.py")
print("  - Use when: You have a few related functions")
print("  - Import: import file_utils")
print("\nPACKAGE:")
print("  - Directory with multiple .py files")
print("  - Example: math_utils/ (with basic.py, advanced.py)")
print("  - Use when: You have many related modules to organize")
print("  - Import: from math_utils import basic")
print("\nKey difference: Package = folder with modules, Module = single file")

print("\n=== Exercise Complete ===")
print("You've learned how to create and use packages!")

