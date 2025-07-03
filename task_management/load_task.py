"""
Task Management System - Load Task Module

This module provides functionality to load and retrieve tasks from the persistent storage.
It includes functions for reading tasks from the storage file and converting them to
structured data for use in the application.

Author: Alex Clark
Date: July 2nd, 2025
Version: 1.0.0
"""

import os
from typing import List, Dict, Optional


def load_tasks(username: str = None) -> List[Dict[str, str]]:
    """
    Load tasks from the persistent storage file, optionally filtered by username.
    
    Reads the tasks.txt file and parses each line to extract task information.
    Each task is represented as a dictionary with 'id', 'username', 'title', and 'status' keys.
    
    Args:
        username (str, optional): If provided, only return tasks for this user.
                                 If None, return all tasks (for admin purposes).
    
    Returns:
        List[Dict[str, str]]: List of task dictionaries, each containing:
            - 'id': Unique task identifier
            - 'username': Username of the task owner
            - 'title': Task title/description
            - 'status': Current task status
            
    Raises:
        FileNotFoundError: If the tasks.txt file doesn't exist
        IOError: If there are issues reading the file
        ValueError: If the file format is invalid
        
    Note:
        - Returns an empty list if the file doesn't exist or is empty
        - Assumes file format: task_id|username|task_title|task_status (one per line)
        - Handles malformed lines gracefully by skipping them
        - If username is provided, only returns tasks belonging to that user
    """
    tasks = []
    
    # Check if the tasks file exists
    if not os.path.exists("tasks.txt"):
        print("No tasks file found. Starting with empty task list.")
        return tasks
    
    try:
        # Use 'with' statement for proper file handling and automatic cleanup
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                # Skip empty lines
                if not line.strip():
                    continue
                
                try:
                    # Parse the line: task_id|username|task_title|task_status
                    parts = line.strip().split("|")
                    
                    # Handle both old format (3 parts) and new format (4 parts)
                    if len(parts) == 3:
                        # Old format: task_id|task_title|task_status
                        task_id, task_title, task_status = parts
                        task_username = "unknown"  # Default for old format
                    elif len(parts) == 4:
                        # New format: task_id|username|task_title|task_status
                        task_id, task_username, task_title, task_status = parts
                    else:
                        print(f"Warning: Skipping malformed line {line_number}: {line.strip()}")
                        continue
                    
                    # Validate that all parts are non-empty
                    if not all([task_id, task_title, task_status]):
                        print(f"Warning: Skipping line {line_number} with empty fields")
                        continue
                    
                    # Filter by username if specified
                    if username is not None and task_username != username:
                        continue
                    
                    # Create task dictionary with structured data
                    task = {
                        "id": task_id,
                        "username": task_username,
                        "title": task_title,
                        "status": task_status
                    }
                    
                    tasks.append(task)
                    
                except Exception as e:
                    print(f"Warning: Error parsing line {line_number}: {e}")
                    continue
                    
    except FileNotFoundError:
        print("Tasks file not found. Starting with empty task list.")
        return tasks
    except IOError as e:
        print(f"IO Error reading tasks file: {e}")
        return tasks
    except Exception as e:
        print(f"Unexpected error loading tasks: {e}")
        return tasks
    
    return tasks


def get_task_by_id(task_id: str, username: str = None) -> Optional[Dict[str, str]]:
    """
    Retrieve a specific task by its unique identifier.
    
    Args:
        task_id (str): The unique identifier of the task to retrieve
        username (str, optional): If provided, only return the task if it belongs to this user
        
    Returns:
        Optional[Dict[str, str]]: Task dictionary if found, None otherwise
        
    Note:
        This function loads all tasks and searches for the specified ID.
        For large task lists, consider implementing a more efficient search mechanism.
    """
    if not task_id:
        print("Error: Task ID cannot be empty")
        return None
    
    tasks = load_tasks(username)
    
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    return None


def get_tasks_by_status(status: str, username: str = None) -> List[Dict[str, str]]:
    """
    Retrieve all tasks with a specific status, optionally filtered by username.
    
    Args:
        status (str): The status to filter by (e.g., 'pending', 'completed')
        username (str, optional): If provided, only return tasks for this user
        
    Returns:
        List[Dict[str, str]]: List of tasks matching the specified status
        
    Note:
        Case-sensitive matching. Consider using case-insensitive comparison
        if needed for your use case.
    """
    if not status:
        print("Error: Status cannot be empty")
        return []
    
    tasks = load_tasks(username)
    return [task for task in tasks if task["status"] == status]


# Example usage and testing (when run as main module)
if __name__ == "__main__":
    print("Task Management System - Load Tasks")
    print("=" * 40)
    
    # Test with specific username
    test_username = input("Enter username to filter tasks (or press Enter for all): ").strip()
    username_filter = test_username if test_username else None
    
    # Load tasks for the specified user
    all_tasks = load_tasks(username_filter)
    
    if all_tasks:
        print(f"Found {len(all_tasks)} tasks:")
        for i, task in enumerate(all_tasks, 1):
            print(f"{i}. [{task['status']}] {task['title']} (User: {task['username']}, ID: {task['id'][:8]}...)")
    else:
        print("No tasks found.")
    
    # Example: Get pending tasks for the user
    pending_tasks = get_tasks_by_status("pending", username_filter)
    if pending_tasks:
        print(f"\nPending tasks: {len(pending_tasks)}")
    else:
        print("\nNo pending tasks found.")