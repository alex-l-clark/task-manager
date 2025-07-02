"""
Task Management System - Delete Task Module

This module provides the delete_task operation for tasks.
"""

from .load_task import load_tasks, get_task_by_id

def delete_task(task_id: str, username: str) -> bool:
    """
    Delete a task.
    Args:
        task_id (str): The unique identifier of the task
        username (str): Username of the task owner
    Returns:
        bool: True if task was deleted successfully, False otherwise
    """
    task = get_task_by_id(task_id, username)
    if not task:
        print("Task not found or you don't have permission to delete it.")
        return False
    confirm = input(f"Are you sure you want to delete '{task['title']}'? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Deletion cancelled.")
        return False
    all_tasks = load_tasks()
    all_tasks = [task_item for task_item in all_tasks if not (task_item["id"] == task_id and task_item["username"] == username)]
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task_item in all_tasks:
                task_line = f"{task_item['id']}|{task_item['username']}|{task_item['title']}|{task_item['status']}\n"
                file.write(task_line)
        print("Task deleted successfully!")
        return True
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False 