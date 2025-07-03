"""
Main entry point for the Task Manager application.

This file demonstrates how to use the reorganized user_management and task_management packages.

Author: Alex Clark
Date: July 2nd, 2025
Version: 1.0.0
"""

from user_management import login, sign_up
from task_management import display_main_task_menu


def main():
    current_user = None  # Track the currently logged-in user
    
    while True:
        print("=== Task Manager ===")
        if current_user:
            print(f"Logged in as: {current_user}")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            success, message, username = login()
            print(message)
            if success:
                current_user = username
                print(f"Welcome to Task Manager, {current_user}!")
                display_main_task_menu(current_user)
            else:
                print("Login failed.")
        
        elif choice == "2":
            success, username = sign_up()
            if success:
                current_user = username
                print(f"Welcome {username}! You are now logged in.")
                display_main_task_menu(current_user)
            else:
                print("Registration failed. Please try again.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

