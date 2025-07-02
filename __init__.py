"""
Task Manager Project

A command-line task management system with user authentication and task management capabilities.

This project is organized into the following modules:
- user_management: User authentication and registration functionality
- task_management: Core task management operations (add, load, view tasks)
- utils: Utility functions and helpers

Author: Alex Clark
Version: 1.0.0
"""

# Import main modules for easy access
from user_management import login, sign_up
from task_management import (
    add_task, load_tasks, get_task_by_id, get_tasks_by_status,
    display_task, display_tasks, display_task_summary, display_detailed_task
)

# Define what should be available when importing the package
__all__ = [
    # User management functions
    'login',
    'sign_up',
    # Task management functions
    'add_task',
    'load_tasks', 
    'get_task_by_id',
    'get_tasks_by_status',
    # Task display functions
    'display_task',
    'display_tasks',
    'display_task_summary',
    'display_detailed_task'
]

__version__ = "1.0.0"
__author__ = "Alex Clark"
__description__ = "A command-line task management system with user authentication" 