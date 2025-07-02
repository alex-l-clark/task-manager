"""
User Management System - Registration Module

This module provides functionality for user registration and account creation.
It includes functions for username validation, user credential storage, and
the main registration process.

Author: Task Manager System
Date: 2024
Version: 1.0.0
"""

import hashlib
import sys
import os
from typing import Optional, Tuple, Callable

# Add parent directory to path for utils import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_valid_input


def check_username(username: str) -> bool:
    """
    Check if a username already exists in the system.
    
    Args:
        username (str): The username to check for existence
        
    Returns:
        bool: True if username exists, False otherwise
        
    Note:
        Searches the users.txt file for the specified username.
        Returns True if found, False if not found or file doesn't exist.
    """
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                stored_username = line.strip().split(":")[0]
                if username == stored_username:
                    return True
        return False
    except FileNotFoundError:
        return False


def is_username_available(username: str) -> bool:
    """
    Check if username is available for registration.
    
    Args:
        username (str): The username to validate
        
    Returns:
        bool: True if username is available, False otherwise
        
    Note:
        Validates that the username is not empty and not already taken.
        Provides user feedback for validation failures.
    """
    if not username:
        print("Username cannot be empty")
        return False
    if check_username(username):
        print("Username already exists")
        return False
    return True


def save_user(username: str, password: str) -> bool:
    """
    Save user credentials to the persistent storage file.
    
    Args:
        username (str): The username to save
        password (str): The hashed password to save
        
    Returns:
        bool: True if user was saved successfully, False otherwise
        
    Note:
        Appends the user credentials to the users.txt file in the format
        username:hashed_password. Handles file I/O errors gracefully.
    """
    try:
        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(f"{username}:{password}\n")
        return True
    except Exception as e:
        print(f"Error saving user: {e}")
        return False


def sign_up() -> Tuple[bool, Optional[str]]:
    """
    Register a new user and return registration status.
    
    This function handles the complete user registration process including
    username validation, password hashing, and credential storage.
    
    Returns:
        Tuple[bool, Optional[str]]: A tuple containing:
            - success (bool): True if registration successful, False otherwise
            - username (Optional[str]): Username if successful, None otherwise
            
    Note:
        - Uses get_valid_input for robust input handling
        - Validates username availability before proceeding
        - Hashes passwords using SHA256 for security
        - Provides clear feedback for success/failure scenarios
    """
    # Get valid username with availability validation
    username = get_valid_input(
        "Enter your username: ",
        "Username cannot be empty",
        is_username_available
    )
    
    # Get valid password from user input
    password = get_valid_input(
        "Enter your password: ",
        "Password cannot be empty"
    )
    
    # Hash password for secure storage
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Save user credentials to persistent storage
    if save_user(username, hashed_password):
        print("Registration successful!")
        return True, username
    else:
        print("Registration failed. Please try again.")
        return False, None


# Example usage and testing (when run as main module)
if __name__ == "__main__":
    print("User Management System - Registration Module")
    print("=" * 40)
    
    # Test registration functionality
    success, username = sign_up()
    if success:
        print(f"User '{username}' registered successfully!")
    else:
        print("Registration failed. Please try again.")
