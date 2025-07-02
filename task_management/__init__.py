"""
Task Management System - Core Module

This module provides the core functionality for managing tasks in the task management system.
It includes functions for adding, loading, viewing, and manipulating tasks.

The module is organized into the following components:
- add_task: Functions for creating and saving new tasks
- load_task: Functions for retrieving and querying existing tasks
- view_task: Functions for displaying tasks in various formats
- complete_task: Functions for completing tasks
- delete_task: Functions for deleting tasks
- utils: Utility functions for task operations

Version: 1.0.0
"""

from .add_task import add_task, generate_task_id, save_task
from .load_task import load_tasks, get_task_by_id, get_tasks_by_status
from .view_task import display_task, display_tasks, display_task_summary, display_detailed_task, display_main_task_menu
from .complete_task import complete_task, update_task_status, display_task_with_id, select_task_by_id
from .delete_task import delete_task

__all__ = [
    'add_task',
    'generate_task_id',
    'save_task',
    'load_tasks',
    'get_task_by_id',
    'get_tasks_by_status',
    'display_task',
    'display_tasks',
    'display_task_summary',
    'display_detailed_task',
    'display_main_task_menu',
    'complete_task',
    'update_task_status',
    'display_task_with_id',
    'select_task_by_id',
    'delete_task'
]

__version__ = "1.0.0"
__author__ = "Task Manager System"
__description__ = "Core task management functionality" 
