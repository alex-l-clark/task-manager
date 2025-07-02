import uuid
import os
from typing import Optional


def generate_task_id() -> str:
    """
    Generate a unique identifier for a task.
    
    Returns:
        str: A unique UUID string for the task
        
    Note:
        Uses UUID4 for generating cryptographically secure random identifiers
        to ensure uniqueness across the entire system.
    """
    return str(uuid.uuid4())


def save_task(task_id: str, username: str, task_title: str, task_status: str) -> bool:
    """
    Save a task to the persistent storage file.
    
    Args:
        task_id (str): Unique identifier for the task
        username (str): Username of the task owner
        task_title (str): Title/description of the task
        task_status (str): Current status of the task (e.g., 'pending', 'completed')
    
    Returns:
        bool: True if task was saved successfully, False otherwise
        
    Raises:
        IOError: If there are issues with file operations
        Exception: For any other unexpected errors during save operation
    """
    # Validate input parameters
    if not all([task_id, username, task_title, task_status]):
        print("Error: All task parameters must be provided")
        return False
    
    # Sanitize input to prevent injection attacks
    if "|" in task_title or "|" in username:
        print("Error: Task title and username cannot contain the '|' character")
        return False
    
    try:
        # Use 'with' statement for proper file handling and automatic cleanup
        with open("tasks.txt", "a", encoding="utf-8") as file:
            # Format: task_id|username|task_title|task_status
            task_line = f"{task_id}|{username}|{task_title}|{task_status}\n"
            file.write(task_line)
            print("Task added successfully!")
            return True
            
    except IOError as e:
        print(f"IO Error saving task: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error saving task: {e}")
        return False


def add_task(username: str) -> bool:
    """
    Interactive function to add a new task to the system.
    
    This function prompts the user for task details, generates a unique ID,
    and saves the task to persistent storage.
    
    Args:
        username (str): Username of the current user
        
    Returns:
        bool: True if task was added successfully, False otherwise
        
    Note:
        - Task status is automatically set to 'pending' for new tasks
        - User input is validated before processing
        - Provides user feedback for success/failure scenarios
    """
    # Get user input with validation
    task_title = input("Enter a task: ").strip()
    
    # Validate user input
    if not task_title:
        print("Error: Task title cannot be empty")
        return False
    
    # Generate unique identifier for the task
    task_id = generate_task_id()
    
    # Set default status for new tasks
    task_status = "pending"
    
    # Attempt to save the task
    if save_task(task_id, username, task_title, task_status):
        return True
    else:
        print("Failed to add task.")
        return False


# Example usage and testing (when run as main module)
if __name__ == "__main__":
    print("Task Management System - Add Task")
    print("=" * 40)
    test_username = input("Enter username for testing: ")
    success = add_task(test_username)
    if success:
        print("Task addition completed successfully!")
    else:
        print("Task addition failed. Please try again.")