"""
Exercise 2: To-Do List Application

Problem:
Create a simple to-do list application using list methods.
The application should allow users to:
- Add tasks
- View all tasks
- Remove tasks
- Mark tasks as complete
- Sort tasks
- Count tasks
"""

# Initialize an empty to-do list
todo_list = []

# ============================================================================
# Task 1: Add a task
# - Create a function add_task(task) that adds a task to the list
# - Use append() to add the task
# - Print a confirmation message
# ============================================================================

print("\n--- Task 1: Add a task function ---")
# Your code here:
def add_task(task):
    todo_list.append(task)
    print("Task successfully added")



# ============================================================================
# Task 2: View all tasks
# - Create a function view_tasks() that displays all tasks
# - If the list is empty, print "No tasks in the list"
# - Otherwise, print each task with its index number
# - Use enumerate() to get both index and task
# ============================================================================

print("\n--- Task 2: View all tasks function ---")
# Your code here:
def view_tasks():
    print(todo_list)


# ============================================================================
# Task 3: Remove a task
# - Create a function remove_task(task) that removes a task
# - Use remove() method
# - Handle the case where task doesn't exist (print error message)
# - Print a confirmation message
# ============================================================================

print("\n--- Task 3: Remove a task function ---")
# Your code here:
def remove_task(task):
    todo_list.remove(task)

# ============================================================================
# Task 4: Remove task by index
# - Create a function remove_task_by_index(index) that removes a task at a specific index
# - Use pop() method
# - Handle the case where index is out of range
# - Return and print the removed task
# ============================================================================

print("\n--- Task 4: Remove task by index function ---")
# Your code here:
def remove_task_by_index(index):
    if(index >= len(todo_list)):
        print("Invalid index")
    else:
        popped = todo_list.pop(index)
        print("removed:", popped)
        return popped


# ============================================================================
# Task 5: Mark task as complete
# - Create a function complete_task(task)
# - Find the task using index() method
# - Modify it to add " [COMPLETED]" to the task
# - Print a confirmation message
# ============================================================================

print("\n--- Task 5: Mark task as complete function ---")
# Your code here:
def complete_task(task):
    t_index = todo_list.index(task)
    todo_list[t_index]+="[COMPLETED]"

# ============================================================================
# Task 6: Count tasks
# - Create a function count_tasks() that returns the number of tasks
# - Use len() function
# - Print the count
# ============================================================================

print("\n--- Task 6: Count tasks function ---")
# Your code here:
def count_tasks():
    return len(todo_list)

# ============================================================================
# Task 7: Sort tasks
# - Create a function sort_tasks() that sorts the tasks alphabetically
# - Use sort() method
# - Print a confirmation message
# ============================================================================

print("\n--- Task 7: Sort tasks function ---")
# Your code here:
def sort_tasks():
    todo_list.sort()
    print("List sorted!")

# ============================================================================
# Task 8: Clear all tasks
# - Create a function clear_tasks() that removes all tasks
# - Use clear() method or assign empty list
# - Print a confirmation message
# ============================================================================

print("\n--- Task 8: Clear all tasks function ---")
# Your code here:
def clear_tasks():
    todo_list.clear()
    print("Cleared all tasks")

# ============================================================================
# Task 9: Test the application
# - Add several tasks: "Buy groceries", "Finish homework", "Call mom"
# - View all tasks
# - Remove one task
# - Mark one task as complete
# - Count tasks
# - Sort tasks
# - View tasks again
# - Test all functions
# ============================================================================

print("\n--- Task 9: Test the application ---")
# Your code here:
add_task("Buy groceries")
add_task("Finish homework")
add_task("Call mom")
view_tasks() 
remove_task("Finish homework")
complete_task("Call mom")
print(count_tasks() )
sort_tasks() 
view_tasks() 
clear_tasks()
view_tasks()  