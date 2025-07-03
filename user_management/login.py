"""
User Management System - Login Module

This module provides functionality for user authentication and login verification.
It includes functions for finding user credentials, password verification, and
the main login process.

Author: Alex Clark
Date: July 2nd, 2025
Version: 1.0.0
"""

import hashlib
import sys
import os
from typing import Optional, Tuple

# Add parent directory to path for utils import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_valid_input


def find_user_credentials(username: str) -> Optional[str]:
    """
    Find stored credentials for a given username.
    
    Args:
        username (str): The username to search for
        
    Returns:
        Optional[str]: The hashed password if found, None otherwise
        
    Note:
        Searches the users.txt file for the specified username and returns
        the corresponding hashed password.
    """
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username:
                    return stored_password
        return None
    except FileNotFoundError:
        return None


def verify_password(input_password: str, stored_password: str) -> bool:
    """
    Verify if input password matches stored password.
    
    Args:
        input_password (str): The password entered by the user
        stored_password (str): The hashed password stored in the system
        
    Returns:
        bool: True if passwords match, False otherwise
        
    Note:
        Compares the SHA256 hash of the input password with the stored hash.
    """
    hashed_input = hashlib.sha256(input_password.encode()).hexdigest()
    return hashed_input == stored_password


def login() -> Tuple[bool, str, Optional[str]]:
    """
    Core login function - authenticates user and returns login status.
    
    This function prompts the user for credentials, validates them against
    stored user data, and returns the authentication result.
    
    Returns:
        Tuple[bool, str, Optional[str]]: A tuple containing:
            - success (bool): True if login successful, False otherwise
            - message (str): Status message for the user
            - username (Optional[str]): Username if successful, None otherwise
            
    Note:
        - Uses get_valid_input for robust input handling
        - Provides clear feedback for different failure scenarios
        - Returns username for session management
    """
    # Get valid username from user input
    username = get_valid_input(
        "Enter your username: ",
        "Username cannot be empty"
    )
    
    # Check if username exists in the system
    stored_password = find_user_credentials(username)
    if not stored_password:
        return False, "Invalid username", None
    
    # Get and verify password from user input
    password = get_valid_input(
        "Enter your password: ",
        "Password cannot be empty"
    )
    
    # Verify the provided password against stored hash
    if verify_password(password, stored_password):
        return True, "Login successful", username
    else:
        return False, "Invalid password", None


# Example usage and testing (when run as main module)
if __name__ == "__main__":
    print("User Management System - Login Module")
    print("=" * 40)
    
    # Test login functionality
    success, message, username = login()
    print(f"Login result: {message}")
    if success:
        print(f"Welcome, {username}!")
    else:
        print("Login failed. Please try again.")