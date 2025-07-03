"""
User Management System - Core Module

This module provides the core functionality for user authentication and registration
in the task management system. It includes functions for user login, registration,
and credential management.

The module is organized into the following components:
- login: Functions for user authentication and login verification
- register: Functions for user registration and account creation
- utils: Utility functions for input validation and user operations

Author: Alex Clark
Date: July 2nd, 2025
Version: 1.0.0
"""

# Import main functions for easy access
from .login import login
from .register import sign_up

# Define what should be available when importing the module
__all__ = [
    'login',
    'sign_up'
]

# Module metadata
__version__ = "1.0.0"
__author__ = "Alex Clark"
__description__ = "Core user authentication and registration functionality" 