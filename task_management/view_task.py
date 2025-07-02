"""
Task Management System - View Module

This module provides functions for displaying tasks in various formats and layouts.
It includes utilities for formatting task output and creating user-friendly displays.
"""

from typing import List, Dict, Optional
from .load_task import load_tasks, get_tasks_by_status
from .complete_task import complete_task, select_task_by_id, display_task_with_id
from .delete_task import delete_task
from .add_task import add_task


def display_task(task: Dict[str, str], show_id: bool = False) -> None:
    """
    Display a single task in a formatted way.
    
    Args:
        task (Dict[str, str]): Task dictionary with 'id', 'title', and 'status' keys
        show_id (bool): Whether to display the full task ID (default: False)
    """
    status_icon = "✓" if task["status"] == "completed" else "○"
    id_display = task["id"] if show_id else task["id"][:8] + "..."
    
    print(f"{status_icon} {task['title']}")
    if show_id:
        print(f"   ID: {id_display}")
        print(f"   Status: {task['status']}")


def display_tasks(tasks: List[Dict[str, str]], title: str = "Tasks", show_id: bool = False) -> None:
    """
    Display a list of tasks with a title.
    
    Args:
        tasks (List[Dict[str, str]]): List of task dictionaries
        title (str): Title to display above the task list
        show_id (bool): Whether to display full task IDs
    """
    if not tasks:
        print(f"No {title.lower()} found.")
        return
    
    print(f"\n=== {title} ({len(tasks)}) ===")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. ", end="")
        display_task(task, show_id)
        if not show_id:
            print()  # Add spacing between tasks


def display_task_summary() -> None:
    """
    Display a summary of all tasks grouped by status.
    """
    all_tasks = load_tasks()
    
    if not all_tasks:
        print("No tasks found.")
        return
    
    # Group tasks by status
    pending_tasks = [task for task in all_tasks if task["status"] == "pending"]
    completed_tasks = [task for task in all_tasks if task["status"] == "completed"]
    other_tasks = [task for task in all_tasks if task["status"] not in ["pending", "completed"]]
    
    print("\n=== Task Summary ===")
    print(f"Total Tasks: {len(all_tasks)}")
    print(f"Pending: {len(pending_tasks)}")
    print(f"Completed: {len(completed_tasks)}")
    if other_tasks:
        print(f"Other: {len(other_tasks)}")
    
    # Display recent tasks (last 5)
    recent_tasks = all_tasks[-5:] if len(all_tasks) > 5 else all_tasks
    if recent_tasks:
        print(f"\nRecent Tasks:")
        for task in recent_tasks:
            display_task(task)


def display_detailed_task(task_id: str) -> bool:
    """
    Display detailed information about a specific task.
    
    Args:
        task_id (str): The unique identifier of the task
        
    Returns:
        bool: True if task was found and displayed, False otherwise
    """
    from .load_task import get_task_by_id
    
    task = get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return False
    
    print(f"\n=== Task Details ===")
    print(f"ID: {task['id']}")
    print(f"Title: {task['title']}")
    print(f"Status: {task['status']}")
    return True


def display_main_task_menu(username: str) -> None:
    """
    Display the main task management menu with all core operations.
    Args:
        username (str): Username of the current user
    """
    while True:
        print(f"\n=== Task Management for {username} ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Tasks by Status")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_task(username)
        
        elif choice == "2":
            tasks = load_tasks(username)
            if not tasks:
                print("No tasks found.")
            else:
                print(f"\n=== All Tasks ({len(tasks)}) ===")
                for i, task in enumerate(tasks, 1):
                    display_task_with_id(task, i)
                    print()
        
        elif choice == "3":
            print("\nView by status:")
            print("1. Pending")
            print("2. Completed")
            print("3. In Progress")
            print("4. Cancelled")
            print("5. Back")
            status_map = {"1": "pending", "2": "completed", "3": "in_progress", "4": "cancelled"}
            status_choice = input("Enter your choice (1-5): ").strip()
            if status_choice in status_map:
                status = status_map[status_choice]
                tasks = get_tasks_by_status(status, username)
                if tasks:
                    print(f"\n=== {status.title()} Tasks ({len(tasks)}) ===")
                    for i, task in enumerate(tasks, 1):
                        display_task_with_id(task, i)
                        print()
                else:
                    print(f"No {status} tasks found.")
            elif status_choice == "5":
                continue
            else:
                print("Invalid choice.")
        
        elif choice == "4":
            tasks = get_tasks_by_status("pending", username)
            if not tasks:
                print("No pending tasks to complete.")
            else:
                print("\nPending tasks:")
                for i, task in enumerate(tasks, 1):
                    display_task_with_id(task, i)
                    print()
                task_id = select_task_by_id(username, "Enter task ID to complete: ")
                if task_id:
                    complete_task(task_id, username)
        
        elif choice == "5":
            tasks = load_tasks(username)
            if not tasks:
                print("No tasks to delete.")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, 1):
                    display_task_with_id(task, i)
                    print()
                task_id = select_task_by_id(username, "Enter task ID to delete: ")
                if task_id:
                    delete_task(task_id, username)
        
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


# Example usage and testing (when run as main module)
if __name__ == "__main__":
    print("Task Management System - View Module")
    print("=" * 40)
    
    # Display task summary
    display_task_summary()
    
    # Display all tasks
    all_tasks = load_tasks()
    display_tasks(all_tasks, "All Tasks")
    
    # Display pending tasks
    pending_tasks = get_tasks_by_status("pending")
    display_tasks(pending_tasks, "Pending Tasks")
