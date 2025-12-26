`import`, `from...import`, `__name__ == "__main__"`, creating modules, `open()`, `with` statement (text/binary modes)
Create a simple module and use it to read/write data to a `.txt` file.

================================================================================
IMPORT AND FROM...IMPORT - Comprehensive Guide
================================================================================

1. WHAT ARE MODULES?
   - A module is a Python file containing functions, classes, and variables
   - Modules help organize code into reusable components
   - Python has built-in modules (like math, os, sys) and you can create your own
   - Modules make code more maintainable and organized

2. USING `import` STATEMENT:
   - Imports an entire module
   - Access functions/classes using module_name.function_name()
   
   Syntax:
   import module_name
   
   Example:
   import math
   result = math.sqrt(16)  # 4.0
   pi_value = math.pi      # 3.14159...
   
   - Must use module name prefix to access contents
   - Prevents naming conflicts

3. USING `from...import` STATEMENT:
   - Imports specific items from a module
   - Can use imported items directly without module prefix
   
   Syntax:
   from module_name import item1, item2, item3
   
   Example:
   from math import sqrt, pi
   result = sqrt(16)  # 4.0 (no math. prefix needed)
   pi_value = pi      # 3.14159...
   
   - More convenient for frequently used items
   - Can cause naming conflicts if names overlap

4. IMPORTING ALL WITH `*`:
   - Imports everything from a module
   - Not recommended (can cause naming conflicts)
   
   Syntax:
   from module_name import *
   
   Example:
   from math import *
   result = sqrt(16)  # Works without math. prefix
   
   - Use sparingly, only when necessary
   - Makes it unclear where functions come from

5. ALIASING MODULES:
   - Give module a shorter or different name
   - Useful for long module names
   
   Syntax:
   import module_name as alias_name
   
   Example:
   import numpy as np
   import pandas as pd
   
   result = np.array([1, 2, 3])
   
   - Makes code more readable
   - Common practice in data science

6. ALIASING SPECIFIC IMPORTS:
   - Can alias specific imports too
   
   Syntax:
   from module_name import item as alias
   
   Example:
   from math import sqrt as square_root
   result = square_root(16)

7. MULTIPLE IMPORTS:
   - Can import multiple modules or items
   
   Example:
   import math, os, sys
   from math import sqrt, pi, sin, cos

8. CREATING YOUR OWN MODULES:
   - Any Python file (.py) can be a module
   - Save functions/classes in a file
   - Import it in another file
   
   Example:
   # File: my_module.py
   def greet(name):
       return f"Hello, {name}!"
   
   def add(x, y):
       return x + y
   
   # File: main.py
   import my_module
   print(my_module.greet("Alice"))
   result = my_module.add(5, 3)

9. MODULE SEARCH PATH:
   - Python searches for modules in:
     1. Current directory
     2. Directories in PYTHONPATH
     3. Standard library directories
     4. Site-packages directory
   
   - Can check with: import sys; print(sys.path)

10. RELATIVE VS ABSOLUTE IMPORTS:
    - Absolute: import my_module (from project root)
    - Relative: from . import my_module (from same package)
    - Use absolute imports when possible

================================================================================
__name__ == "__main__" - Comprehensive Guide
================================================================================

1. WHAT IS __name__?
   - Special variable in Python
   - Contains the name of the current module
   - When file is run directly: __name__ = "__main__"
   - When file is imported: __name__ = module_name

2. WHY USE __name__ == "__main__"?
   - Allows code to run only when file is executed directly
   - Prevents code from running when file is imported as module
   - Makes files work both as scripts and as modules

3. BASIC SYNTAX:
   if __name__ == "__main__":
       # Code here runs only when file is executed directly
       # Not when imported
       pass

4. EXAMPLE WITHOUT __name__ == "__main__":
   # File: calculator.py
   def add(x, y):
       return x + y
   
   print("Calculator module loaded")  # Runs even when imported!
   result = add(5, 3)
   print(f"Result: {result}")  # Runs even when imported!
   
   Problem: When you import this module, the print statements execute

5. EXAMPLE WITH __name__ == "__main__":
   # File: calculator.py
   def add(x, y):
       return x + y
   
   if __name__ == "__main__":
       print("Calculator module loaded")  # Only runs when executed directly
       result = add(5, 3)
       print(f"Result: {result}")  # Only runs when executed directly
   
   Now:
   - python calculator.py → Prints messages
   - import calculator → No messages printed

6. COMMON USE CASES:
   
   Testing code:
   if __name__ == "__main__":
       # Test your functions
       assert add(2, 3) == 5
       print("All tests passed!")
   
   Main execution:
   if __name__ == "__main__":
       # Main program logic
       main()

7. BEST PRACTICES:
   - Always use __name__ == "__main__" for executable code
   - Keep module code separate from script code
   - Makes modules reusable and testable

================================================================================
CREATING MODULES - Comprehensive Guide
================================================================================

1. WHAT IS A MODULE?
   - A Python file (.py) containing code
   - Can contain functions, classes, variables, constants
   - Can be imported and used in other files

2. CREATING A SIMPLE MODULE:
   
   Step 1: Create a Python file
   # File: utils.py
   def greet(name):
       return f"Hello, {name}!"
   
   def calculate_area(radius):
       return 3.14159 * radius ** 2
   
   PI = 3.14159
   
   Step 2: Use it in another file
   # File: main.py
   import utils
   
   print(utils.greet("Alice"))
   area = utils.calculate_area(5)
   print(f"Area: {area}")

3. MODULE STRUCTURE:
   - Docstring at top (optional but recommended)
   - Imports
   - Constants
   - Functions
   - Classes
   - if __name__ == "__main__": block
   
   Example:
   """
   This module provides utility functions.
   """
   
   import math
   
   VERSION = "1.0"
   
   def helper_function():
       pass
   
   def public_function():
       pass
   
   if __name__ == "__main__":
       # Test code
       pass

4. ORGANIZING MODULES:
   - Group related functions together
   - Use descriptive file names
   - Keep modules focused on one purpose
   - Document with docstrings

5. MODULE DOCUMENTATION:
   - Use docstrings to document modules
   - Access with: module_name.__doc__
   
   Example:
   """
   Math utilities module.
   
   This module provides various mathematical functions.
   """
   
   def square(x):
       """Returns the square of x."""
       return x ** 2

6. PACKAGES (MULTIPLE MODULES):
   - A package is a directory containing multiple modules
   - Must have __init__.py file (can be empty)
   - Allows organizing related modules
   
   Example structure:
   my_package/
       __init__.py
       module1.py
       module2.py
   
   Usage:
   from my_package import module1
   import my_package.module2

================================================================================
open() FUNCTION - Comprehensive Guide
================================================================================

1. WHAT IS open()?
   - Built-in function to open files
   - Returns a file object
   - Used to read from or write to files
   - Must close file when done (or use 'with' statement)

2. BASIC SYNTAX:
   file_object = open(filename, mode)
   
   Parameters:
   - filename: Path to file (string)
   - mode: How to open file ('r', 'w', 'a', etc.)

3. FILE MODES:
   
   Text Modes:
   - 'r': Read mode (default, file must exist)
   - 'w': Write mode (creates new file, overwrites existing)
   - 'a': Append mode (adds to end of file)
   - 'x': Exclusive creation (fails if file exists)
   - 'r+': Read and write mode
   
   Binary Modes:
   - 'rb': Read binary
   - 'wb': Write binary
   - 'ab': Append binary
   - 'rb+': Read and write binary
   
   Text with Encoding:
   - 'rt': Read text (default)
   - 'wt': Write text
   - 'at': Append text

4. READING FROM A FILE:
   
   Example 1: Read entire file
   file = open("data.txt", "r")
   content = file.read()
   file.close()
   print(content)
   
   Example 2: Read line by line
   file = open("data.txt", "r")
   for line in file:
       print(line.strip())  # strip() removes newline
   file.close()
   
   Example 3: Read all lines into list
   file = open("data.txt", "r")
   lines = file.readlines()
   file.close()
   print(lines)

5. WRITING TO A FILE:
   
   Example 1: Write text
   file = open("output.txt", "w")
   file.write("Hello, World!\n")
   file.write("This is a new line.")
   file.close()
   
   Example 2: Write multiple lines
   file = open("output.txt", "w")
   lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
   file.writelines(lines)
   file.close()

6. APPENDING TO A FILE:
   file = open("data.txt", "a")
   file.write("New line appended\n")
   file.close()

7. FILE OBJECT METHODS:
   - read(): Read entire file or specified number of bytes
   - readline(): Read one line
   - readlines(): Read all lines into list
   - write(): Write string to file
   - writelines(): Write list of strings
   - close(): Close the file
   - seek(): Move file pointer
   - tell(): Get current position

8. IMPORTANT: CLOSING FILES:
   - Always close files when done
   - Frees system resources
   - Use 'with' statement for automatic closing (recommended)

9. FILE PATHS:
   - Relative path: "data.txt" (current directory)
   - Absolute path: "/Users/name/data.txt" (full path)
   - Use forward slashes (/) or raw strings on Windows

10. ENCODING:
    - Text files have encoding (UTF-8 is default in Python 3)
    - Can specify encoding explicitly:
      file = open("data.txt", "r", encoding="utf-8")

11. ERROR HANDLING:
    - Files might not exist
    - Use try-except:
      try:
          file = open("data.txt", "r")
          content = file.read()
      except FileNotFoundError:
          print("File not found!")
      finally:
          file.close()

================================================================================
WITH STATEMENT - Comprehensive Guide
================================================================================

1. WHAT IS THE `with` STATEMENT?
   - Context manager for resource management
   - Automatically handles opening and closing files
   - Ensures files are closed even if errors occur
   - Recommended way to work with files

2. BASIC SYNTAX:
   with open(filename, mode) as file:
       # Use file here
       pass
   # File automatically closed here

3. READING WITH `with`:
   Example:
   with open("data.txt", "r") as file:
       content = file.read()
       print(content)
   # File is automatically closed

4. WRITING WITH `with`:
   Example:
   with open("output.txt", "w") as file:
       file.write("Hello, World!\n")
       file.write("Second line\n")
   # File is automatically closed

5. APPENDING WITH `with`:
   Example:
   with open("data.txt", "a") as file:
       file.write("Appended line\n")
   # File is automatically closed

6. READING LINE BY LINE WITH `with`:
   Example:
   with open("data.txt", "r") as file:
       for line in file:
           print(line.strip())
   # File is automatically closed

7. MULTIPLE FILES WITH `with`:
   Example:
   with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
       content = infile.read()
       outfile.write(content)
   # Both files automatically closed

8. TEXT MODE (DEFAULT):
   - Files opened in text mode by default
   - Content is strings
   - Handles newlines automatically
   - Encoding: UTF-8 (default)
   
   Example:
   with open("data.txt", "r") as file:  # Text mode
       content = file.read()  # Returns string

9. BINARY MODE:
   - Use 'b' in mode for binary files
   - Content is bytes
   - Used for images, videos, executables
   
   Example:
   with open("image.jpg", "rb") as file:  # Binary read
       data = file.read()  # Returns bytes
   
   with open("copy.jpg", "wb") as file:  # Binary write
       file.write(data)

10. ADVANTAGES OF `with` STATEMENT:
    - Automatic file closing
    - Exception safety (closes even on errors)
    - Cleaner code
    - No need to remember close()
    - Best practice in Python

11. COMPARISON:
    
    Without `with` (manual):
    file = open("data.txt", "r")
    content = file.read()
    file.close()  # Must remember to close!
    
    With `with` (automatic):
    with open("data.txt", "r") as file:
        content = file.read()
    # Automatically closed!

12. TEXT VS BINARY MODES:
    
    Text Mode:
    - Use for: .txt, .csv, .json, .py files
    - Content: strings
    - Handles encoding/decoding
    - Example: with open("data.txt", "r") as file:
    
    Binary Mode:
    - Use for: .jpg, .png, .pdf, .exe files
    - Content: bytes
    - No encoding/decoding
    - Example: with open("image.jpg", "rb") as file:

13. COMMON PATTERNS:
    
    Read entire file:
    with open("file.txt", "r") as f:
        content = f.read()
    
    Read line by line:
    with open("file.txt", "r") as f:
        for line in f:
            process(line)
    
    Write to file:
    with open("file.txt", "w") as f:
        f.write("content")
    
    Copy file:
    with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
        dst.write(src.read())

14. ERROR HANDLING WITH `with`:
    - `with` statement handles closing even on errors
    - Still use try-except for file not found:
    
    Example:
    try:
        with open("data.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found!")

15. BEST PRACTICES:
    - Always use `with` statement for file operations
    - Specify encoding for text files if needed
    - Use binary mode for non-text files
    - Handle exceptions appropriately
    - Use descriptive file names

