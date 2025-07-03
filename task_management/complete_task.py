"""
Task Management System - Complete Task Module

This module provides the complete_task operation and helpers.

Author: Alex Clark
Date: July 2nd, 2025
Version: 1.0.0
"""

from .load_task import load_tasks, get_task_by_id
from typing import Dict, Optional


def complete_task(task_id: str, username: str) -> bool:
    """
    Mark a task as completed.
    Args:
        task_id (str): The unique identifier of the task
        username (str): Username of the task owner
    Returns:
        bool: True if task was completed successfully, False otherwise
    """
    task = get_task_by_id(task_id, username)
    if not task:
        print("Task not found or you don't have permission to modify it.")
        return False
    if task["status"] == "completed":
        print("Task is already completed.")
        return False
    return update_task_status(task_id, username, "completed")


def update_task_status(task_id: str, username: str, new_status: str) -> bool:
    valid_statuses = ["pending", "completed", "in_progress", "cancelled"]
    if new_status not in valid_statuses:
        print(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return False
    all_tasks = load_tasks()  # Load all tasks to rewrite the file
    user_tasks = load_tasks(username)
    task_found = False
    for task in user_tasks:
        if task["id"] == task_id:
            task_found = True
            break
    if not task_found:
        print("Task not found or you don't have permission to modify it.")
        return False
    for task in all_tasks:
        if task["id"] == task_id and task["username"] == username:
            task["status"] = new_status
            break
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in all_tasks:
                task_line = f"{task['id']}|{task['username']}|{task['title']}|{task['status']}\n"
                file.write(task_line)
        status_display = "completed" if new_status == "completed" else new_status
        print(f"Task marked as {status_display} successfully!")
        return True
    except Exception as e:
        print(f"Error updating task: {e}")
        return False


def display_task_with_id(task: Dict[str, str], index: int = None) -> None:
    status_icon = "✓" if task["status"] == "completed" else "○"
    index_display = f"{index}. " if index is not None else ""
    print(f"{index_display}{status_icon} {task['title']}")
    print(f"   ID: {task['id']}")
    print(f"   Status: {task['status']}")


def select_task_by_id(username: str, prompt: str = "Enter task ID: ") -> Optional[str]:
    task_id = input(prompt).strip()
    if not task_id:
        print("No task ID provided.")
        return None
    task = get_task_by_id(task_id, username)
    if not task:
        print("Task not found or you don't have permission to access it.")
        return None
    return task_id 