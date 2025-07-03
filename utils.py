"""
Task Manager System - Utilities Module

This module provides utility functions used across the task management system.
It includes input validation, data processing, and other helper functions.

Author: Alex Clark
Date: July 2nd, 2025
Version: 1.0.0
"""

from typing import Optional, Callable


def get_valid_input(prompt: str, error_message: str, validator: Optional[Callable[[str], bool]] = None) -> str:
    """
    Get valid input from user with custom validation.
    
    This function provides robust input handling with built-in empty input validation
    and optional custom validation functions.
    
    Args:
        prompt (str): The input prompt to display to the user
        error_message (str): Error message to show for empty input
        validator (Optional[Callable[[str], bool]]): Custom validation function that returns True/False
        
    Returns:
        str: Valid user input that passes all validation checks
        
    Note:
        - Continuously prompts until valid input is received
        - Strips whitespace from user input
        - Validates against empty input by default
        - Supports custom validation functions for specific requirements
        - Used throughout the system for consistent input handling
    """
    while True:
        # Get user input and remove leading/trailing whitespace
        value = input(prompt).strip()
        
        # Check for empty input
        if not value:
            print(error_message)
            continue
        
        # Apply custom validation if provided
        if validator and not validator(value):
            continue
        
        return value


# Example usage and testing (when run as main module)
if __name__ == "__main__":
    print("Task Manager System - Utilities Module")
    print("=" * 40)
    
    # Test basic input validation
    print("Testing basic input validation...")
    name = get_valid_input("Enter your name: ", "Name cannot be empty")
    print(f"Hello, {name}!")
    
    # Test custom validation
    print("\nTesting custom validation...")
    def is_positive_number(value: str) -> bool:
        try:
            num = int(value)
            if num <= 0:
                print("Please enter a positive number.")
                return False
            return True
        except ValueError:
            print("Please enter a valid number.")
            return False
    
    age = get_valid_input("Enter your age: ", "Age cannot be empty", is_positive_number)
    print(f"Your age is: {age}") 