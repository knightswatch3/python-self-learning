"""
Exercise 1: Creating a Module and File Operations

Problem:
You need to create a simple module for file operations and use it to read/write data to a .txt file.
"""

# ============================================================================
# Task 1: Create a module file (file_utils.py)
# 1. Create a new file called 'file_utils.py' in the same directory
# 2. Add a function called read_file() that takes a filename and returns file content
# 3. Add a function called write_file() that takes filename and content, writes to file
# 4. Add a function called append_file() that appends content to a file
# 5. Use 'with' statement in all functions
# 6. Add docstrings to all functions
# ============================================================================

# First, let's create the module file
module_content = '''"""
File utilities module for reading and writing text files.
"""

def read_file(filename):
    """
    Read content from a text file.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        str: Content of the file
    """
    with open(filename, "r") as file:
        content = file.read()
    return content


def write_file(filename, content):
    """
    Write content to a text file (overwrites if file exists).
    
    Args:
        filename (str): Path to the file to write
        content (str): Content to write to the file
    """
    with open(filename, "w") as file:
        file.write(content)


def append_file(filename, content):
    """
    Append content to a text file.
    
    Args:
        filename (str): Path to the file to append to
        content (str): Content to append to the file
    """
    with open(filename, "a") as file:
        file.write(content)


def read_lines(filename):
    """
    Read all lines from a text file into a list.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        list: List of lines from the file
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines


if __name__ == "__main__":
    # Test the module functions
    print("Testing file_utils module...")
    
    # Test write
    write_file("test.txt", "Hello, World!\\nThis is a test file.\\n")
    print("File written successfully!")
    
    # Test read
    content = read_file("test.txt")
    print(f"File content: {content}")
    
    # Test append
    append_file("test.txt", "This line was appended.\\n")
    print("Content appended!")
    
    # Test read again
    content = read_file("test.txt")
    print(f"Updated content: {content}")
'''

# Create the module file
with open("file_utils.py", "w") as f:
    f.write(module_content)

print("Module file_utils.py created!")

# ============================================================================
# Task 2: Import the module
# 1. Import the file_utils module using 'import' statement
# 2. Test that you can access the functions
# ============================================================================

print("\n--- Task 2: Import the module ---")
# Your code here:
import file_utils

# ============================================================================
# Task 3: Use from...import
# 1. Use 'from file_utils import read_file, write_file'
# 2. Call the functions directly without module prefix
# ============================================================================

print("\n--- Task 3: Use from...import ---")
# Your code here:
from file_utils import read_file, write_file, append_file

# ============================================================================
# Task 4: Write data to a file
# 1. Use write_file() to create a file called 'data.txt'
# 2. Write some sample data (e.g., names, numbers, or a short story)
# 3. Verify the file was created
# ============================================================================

print("\n--- Task 4: Write data to a file ---")
# Your code here:
write_file("data.txt", "Alice\nBob\nCharlie\nDiana\nEve\n")

# ============================================================================
# Task 5: Read data from the file
# 1. Use read_file() to read the content from 'data.txt'
# 2. Print the content
# 3. Observe the output
# ============================================================================

print("\n--- Task 5: Read data from the file ---")
# Your code here:
content = read_file("data.txt")
print("File content:")
print(content)

# ============================================================================
# Task 6: Append data to the file
# 1. Use append_file() to add more data to 'data.txt'
# 2. Read the file again to see the appended content
# 3. Print the updated content
# ============================================================================

print("\n--- Task 6: Append data to the file ---")
# Your code here:
append_file("data.txt", "Frank\nGrace\nHenry\n")
updated_content = read_file("data.txt")
print("Updated file content:")
print(updated_content)

# ============================================================================
# Task 7: Read file line by line
# 1. Import read_lines() from file_utils
# 2. Use it to read 'data.txt' line by line
# 3. Print each line with its line number
# ============================================================================

print("\n--- Task 7: Read file line by line ---")
# Your code here:
from file_utils import read_lines
lines = read_lines("data.txt")
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}")

# ============================================================================
# Task 8: Create a data processing function
# 1. Create a function called process_data() that:
#    - Reads data from 'data.txt'
#    - Counts the number of lines
#    - Writes a summary to 'summary.txt'
# 2. Use file_utils functions in your process_data() function
# 3. Call the function and verify 'summary.txt' was created
# ============================================================================

print("\n--- Task 8: Create a data processing function ---")
# Your code here:
def process_data():
    """Process data from data.txt and create a summary."""
    content = read_file("data.txt")
    lines = content.strip().split("\n")
    line_count = len([line for line in lines if line.strip()])
    
    summary = f"Data Summary\n"
    summary += f"============\n"
    summary += f"Total lines: {line_count}\n"
    summary += f"\nLines:\n"
    for i, line in enumerate(lines, 1):
        if line.strip():
            summary += f"{i}. {line.strip()}\n"
    
    write_file("summary.txt", summary)
    print("Summary file created!")

process_data()
summary_content = read_file("summary.txt")
print("\nSummary content:")
print(summary_content)

# ============================================================================
# Task 9: Test __name__ == "__main__"
# 1. Check what __name__ is in this file
# 2. Print the value of __name__
# 3. Add an if __name__ == "__main__": block that runs some test code
# ============================================================================

print("\n--- Task 9: Test __name__ == "__main__" ---")
# Your code here:
print(f"Current __name__ value: {__name__}")

if __name__ == "__main__":
    print("This code runs only when the file is executed directly!")
    print("It won't run when this file is imported as a module.")
    
    # Test all file operations
    print("\nRunning file operation tests...")
    write_file("test_main.txt", "This file was created in __main__ block.\n")
    content = read_file("test_main.txt")
    print(f"Test file content: {content}")

# ============================================================================
# Task 10: Binary file operations (bonus)
# 1. Create a function that reads a file in binary mode
# 2. Create a function that writes a file in binary mode
# 3. Test with a simple text file (convert string to bytes)
# ============================================================================

print("\n--- Task 10: Binary file operations (bonus) ---")
# Your code here:
def read_binary(filename):
    """Read a file in binary mode."""
    with open(filename, "rb") as file:
        content = file.read()
    return content

def write_binary(filename, data):
    """Write data to a file in binary mode."""
    with open(filename, "wb") as file:
        file.write(data)

# Test binary operations
text_data = "Hello, Binary World!\nThis is binary mode.\n"
binary_data = text_data.encode("utf-8")  # Convert string to bytes

write_binary("binary_test.txt", binary_data)
read_back = read_binary("binary_test.txt")
decoded = read_back.decode("utf-8")  # Convert bytes back to string

print("Binary write/read test:")
print(f"Original: {text_data}")
print(f"Decoded: {decoded}")
print("Binary operations successful!")

print("\n=== Exercise Complete ===")
print("All file operations completed successfully!")

