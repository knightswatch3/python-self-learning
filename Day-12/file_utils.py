
# ============================================================================
# Task 1: Create a module file (file_utils.py)
# 1. Create a new file called 'file_utils.py' in the same directory
# 2. Add a function called read_file() that takes a filename and returns file content
# 3. Add a function called write_file() that takes filename and content, writes to file
# 4. Add a function called append_file() that appends content to a file
# 5. Use 'with' statement in all functions
# 6. Add docstrings to all functions
# ============================================================================

def read_file(filename: str):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def write_file(filename: str, content: str):
    with open(filename, 'r') as file:
        file.write(content)

def append_file(filename: str, content: str):
    with open(filename, 'a') as file:
        file.write(content)