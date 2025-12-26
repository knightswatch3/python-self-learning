"""
Exercise 3: Add Exception Handling to File Operations

Problem:
Add robust exception handling to the file operations from Day 12.
Make file_utils.py more robust with proper error handling.
"""

# Import the file_utils module from Day 12
# We'll create an improved version with exception handling

# ============================================================================
# Task 1: Create improved file_utils with exception handling
# 1. Create file_utils_safe.py with exception handling
# 2. Handle FileNotFoundError, PermissionError, IOError
# 3. Add try/except/finally blocks
# ============================================================================

print("--- Task 1: Create improved file_utils with exception handling ---")

improved_module = '''"""
Safe file utilities module with robust exception handling.
"""

class FileOperationError(Exception):
    """Base exception for file operations"""
    pass

class FileNotFoundError(FileOperationError):
    """Raised when file is not found"""
    pass

class FilePermissionError(FileOperationError):
    """Raised when file permission is denied"""
    pass


def read_file(filename):
    """
    Read content from a text file with exception handling.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        str: Content of the file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        PermissionError: If permission denied
        IOError: For other I/O errors
    """
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found!")
    except PermissionError:
        raise PermissionError(f"Permission denied to read '{filename}'")
    except IOError as e:
        raise IOError(f"Error reading file '{filename}': {e}")


def write_file(filename, content):
    """
    Write content to a text file with exception handling.
    
    Args:
        filename (str): Path to the file to write
        content (str): Content to write to the file
        
    Raises:
        PermissionError: If permission denied
        IOError: For other I/O errors
    """
    try:
        with open(filename, "w") as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied to write '{filename}'")
    except IOError as e:
        raise IOError(f"Error writing file '{filename}': {e}")


def append_file(filename, content):
    """
    Append content to a text file with exception handling.
    
    Args:
        filename (str): Path to the file to append to
        content (str): Content to append to the file
        
    Raises:
        PermissionError: If permission denied
        IOError: For other I/O errors
    """
    try:
        with open(filename, "a") as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied to append to '{filename}'")
    except IOError as e:
        raise IOError(f"Error appending to file '{filename}': {e}")


def read_file_safe(filename, default=""):
    """
    Safely read a file, returning default if file doesn't exist.
    
    Args:
        filename (str): Path to the file to read
        default (str): Default content if file doesn't exist
        
    Returns:
        str: File content or default value
    """
    try:
        return read_file(filename)
    except FileNotFoundError:
        return default
    except Exception as e:
        print(f"Warning: Could not read file '{filename}': {e}")
        return default


def read_lines(filename):
    """
    Read all lines from a text file into a list with exception handling.
    
    Args:
        filename (str): Path to the file to read
        
    Returns:
        list: List of lines from the file
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found!")
    except Exception as e:
        raise IOError(f"Error reading lines from '{filename}': {e}")


if __name__ == "__main__":
    # Test the module functions
    print("Testing file_utils_safe module...")
    
    # Test write
    try:
        write_file("test.txt", "Hello, World!\\nThis is a test file.\\n")
        print("File written successfully!")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test read
    try:
        content = read_file("test.txt")
        print(f"File content: {content}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test read non-existent file
    try:
        content = read_file("nonexistent.txt")
    except FileNotFoundError as e:
        print(f"Expected error: {e}")
    
    # Test safe read
    content = read_file_safe("nonexistent.txt", "Default content")
    print(f"Safe read result: {content}")
'''

# Create the improved module
with open("file_utils_safe.py", "w") as f:
    f.write(improved_module)

print("Created file_utils_safe.py with exception handling!")

# ============================================================================
# Task 2: Test file operations with exception handling
# 1. Import file_utils_safe
# 2. Test reading a file that exists
# 3. Test reading a file that doesn't exist
# 4. Handle exceptions appropriately
# ============================================================================

print("\n--- Task 2: Test file operations with exception handling ---")
# Your code here:
import file_utils_safe

# Test reading existing file
try:
    file_utils_safe.write_file("test_data.txt", "Line 1\nLine 2\nLine 3\n")
    content = file_utils_safe.read_file("test_data.txt")
    print(f"Successfully read file: {content}")
except Exception as e:
    print(f"Error: {e}")

# Test reading non-existent file
try:
    content = file_utils_safe.read_file("nonexistent_file.txt")
except FileNotFoundError as e:
    print(f"Caught FileNotFoundError: {e}")
except Exception as e:
    print(f"Other error: {e}")

# ============================================================================
# Task 3: Use safe read function
# 1. Use read_file_safe() to read a file
# 2. If file doesn't exist, it returns default value
# 3. No exception raised
# ============================================================================

print("\n--- Task 3: Use safe read function ---")
# Your code here:
# Read existing file
content1 = file_utils_safe.read_file_safe("test_data.txt", "Default")
print(f"Content from existing file: {content1[:30]}...")

# Read non-existent file (returns default)
content2 = file_utils_safe.read_file_safe("missing.txt", "File not found, using default")
print(f"Content from missing file: {content2}")

# ============================================================================
# Task 4: File operations with complete error handling
# 1. Create a function that reads, processes, and writes data
# 2. Handle all possible exceptions
# 3. Use try/except/else/finally appropriately
# ============================================================================

print("\n--- Task 4: Complete error handling pattern ---")
# Your code here:
def process_file(input_file, output_file):
    """Read from input file, process, write to output file."""
    input_content = None
    output_file_handle = None
    
    try:
        # Read input file
        try:
            input_content = file_utils_safe.read_file(input_file)
            print(f"Successfully read {input_file}")
        except FileNotFoundError:
            print(f"Input file '{input_file}' not found!")
            return False
        
        # Process content (convert to uppercase)
        processed = input_content.upper()
        
        # Write output file
        try:
            file_utils_safe.write_file(output_file, processed)
            print(f"Successfully wrote {output_file}")
        except PermissionError:
            print(f"Permission denied to write {output_file}")
            return False
        except Exception as e:
            print(f"Error writing file: {e}")
            return False
            
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    else:
        print("File processing completed successfully!")
        return True
    finally:
        print("Cleanup: File processing operation finished")

# Test the function
process_file("test_data.txt", "output_processed.txt")

# ============================================================================
# Task 5: Validate file operations
# 1. Create a function that validates file before operations
# 2. Raise custom exceptions for invalid files
# 3. Check file extension, size, etc.
# ============================================================================

print("\n--- Task 5: Validate file operations ---")
# Your code here:
class InvalidFileError(Exception):
    """Raised when file is invalid"""
    pass

class FileTooLargeError(InvalidFileError):
    """Raised when file is too large"""
    pass

class InvalidFileExtensionError(InvalidFileError):
    """Raised when file has invalid extension"""
    pass

def validate_file_for_reading(filename, max_size_mb=10):
    """Validate file before reading."""
    import os
    
    # Check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist")
    
    # Check file extension
    if not filename.endswith('.txt'):
        raise InvalidFileExtensionError(f"File '{filename}' must be a .txt file")
    
    # Check file size
    file_size = os.path.getsize(filename)
    max_size_bytes = max_size_mb * 1024 * 1024
    if file_size > max_size_bytes:
        raise FileTooLargeError(f"File '{filename}' is too large ({file_size / 1024 / 1024:.2f} MB)")
    
    return True

# Test validation
try:
    validate_file_for_reading("test_data.txt")
    print("File validation passed!")
except (FileNotFoundError, InvalidFileExtensionError, FileTooLargeError) as e:
    print(f"Validation failed: {e}")

# ============================================================================
# Task 6: Batch file operations with error handling
# 1. Process multiple files
# 2. Continue processing even if one file fails
# 3. Collect and report all errors
# ============================================================================

print("\n--- Task 6: Batch file operations ---")
# Your code here:
def process_multiple_files(filenames, output_dir="processed"):
    """Process multiple files, handling errors for each."""
    import os
    
    results = {"success": [], "failed": []}
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in filenames:
        try:
            # Validate file
            validate_file_for_reading(filename)
            
            # Read and process
            content = file_utils_safe.read_file(filename)
            processed = content.upper()
            
            # Write output
            output_file = os.path.join(output_dir, f"processed_{os.path.basename(filename)}")
            file_utils_safe.write_file(output_file, processed)
            
            results["success"].append(filename)
            print(f"✓ Processed {filename}")
            
        except FileNotFoundError as e:
            results["failed"].append((filename, str(e)))
            print(f"✗ {filename}: {e}")
        except InvalidFileExtensionError as e:
            results["failed"].append((filename, str(e)))
            print(f"✗ {filename}: {e}")
        except Exception as e:
            results["failed"].append((filename, f"Unexpected error: {e}"))
            print(f"✗ {filename}: {e}")
    
    return results

# Test batch processing
test_files = ["test_data.txt", "nonexistent.txt", "test_data.txt"]
results = process_multiple_files(test_files)
print(f"\nResults: {len(results['success'])} succeeded, {len(results['failed'])} failed")

# ============================================================================
# Task 7: Context manager for file operations
# 1. Create a custom context manager for safe file operations
# 2. Handle exceptions automatically
# 3. Ensure cleanup happens
# ============================================================================

print("\n--- Task 7: Custom context manager ---")
# Your code here:
from contextlib import contextmanager

@contextmanager
def safe_file_operation(filename, mode="r", default_content=""):
    """Context manager for safe file operations."""
    file_handle = None
    try:
        if mode == "r":
            try:
                file_handle = open(filename, mode)
                yield file_handle
            except FileNotFoundError:
                print(f"File '{filename}' not found, using default content")
                yield default_content
        else:
            file_handle = open(filename, mode)
            yield file_handle
    except Exception as e:
        print(f"Error in file operation: {e}")
        raise
    finally:
        if file_handle:
            file_handle.close()

# Use the context manager
try:
    with safe_file_operation("test_data.txt", "r") as file:
        if isinstance(file, str):
            content = file
        else:
            content = file.read()
        print(f"Read content: {content[:50]}...")
except Exception as e:
    print(f"Error: {e}")

# ============================================================================
# Task 8: Logging errors from file operations
# 1. Create a function that logs file operation errors
# 2. Write errors to a log file
# 3. Include timestamp and error details
# ============================================================================

print("\n--- Task 8: Logging file operation errors ---")
# Your code here:
from datetime import datetime

def log_file_error(operation, filename, error):
    """Log file operation errors to a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {operation} on '{filename}': {error}\n"
    
    try:
        with open("file_errors.log", "a") as log_file:
            log_file.write(log_entry)
    except Exception:
        print(f"Could not write to log file: {log_entry}")

def read_file_with_logging(filename):
    """Read file and log any errors."""
    try:
        return file_utils_safe.read_file(filename)
    except Exception as e:
        log_file_error("READ", filename, str(e))
        raise

# Test logging
try:
    read_file_with_logging("nonexistent.txt")
except FileNotFoundError:
    print("Error logged to file_errors.log")

# ============================================================================
# Task 9: Retry mechanism for file operations
# 1. Create a function that retries file operations
# 2. Retry on certain exceptions (like PermissionError)
# 3. Give up after max retries
# ============================================================================

print("\n--- Task 9: Retry mechanism ---")
# Your code here:
import time

def read_file_with_retry(filename, max_retries=3, delay=1):
    """Read file with retry mechanism."""
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            return file_utils_safe.read_file(filename)
        except PermissionError as e:
            last_exception = e
            if attempt < max_retries - 1:
                print(f"Permission denied, retrying in {delay} seconds... (attempt {attempt + 1}/{max_retries})")
                time.sleep(delay)
            else:
                print("Max retries reached, giving up")
        except FileNotFoundError:
            # Don't retry for file not found
            raise
    
    raise last_exception

# Note: This would work better with actual permission issues
# For demo, we'll just show the structure
print("Retry mechanism created (would retry on PermissionError)")

# ============================================================================
# Task 10: Complete robust file utility
# 1. Combine all error handling patterns
# 2. Create a comprehensive file operation function
# 3. Handle all edge cases
# ============================================================================

print("\n--- Task 10: Complete robust file utility ---")
# Your code here:
def robust_file_copy(source, destination):
    """
    Robustly copy a file with comprehensive error handling.
    
    Returns:
        bool: True if successful, False otherwise
    """
    source_handle = None
    dest_handle = None
    
    try:
        # Validate source file
        try:
            validate_file_for_reading(source)
        except (FileNotFoundError, InvalidFileExtensionError, FileTooLargeError) as e:
            log_file_error("VALIDATE", source, str(e))
            return False
        
        # Read source
        try:
            content = file_utils_safe.read_file(source)
        except Exception as e:
            log_file_error("READ", source, str(e))
            return False
        
        # Write destination
        try:
            file_utils_safe.write_file(destination, content)
            print(f"Successfully copied {source} to {destination}")
            return True
        except Exception as e:
            log_file_error("WRITE", destination, str(e))
            return False
            
    except Exception as e:
        log_file_error("COPY", f"{source} -> {destination}", str(e))
        return False
    finally:
        print("File copy operation completed")

# Test robust copy
result = robust_file_copy("test_data.txt", "copied_file.txt")
print(f"Copy operation result: {'Success' if result else 'Failed'}")

print("\n=== Exercise 3 Complete ===")
print("File operations now have robust exception handling!")

