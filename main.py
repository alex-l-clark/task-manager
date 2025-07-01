"""
Main entry point for the Task Manager application.

This file demonstrates how to use the reorganized user_management package.
"""

from user_management import login, sign_up

def main():
    print("=== Task Manager ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        success, message = login()
        print(message)
        if success:
            print("Welcome to Task Manager!")
            # TODO: Add task management menu here
        else:
            print("Login failed.")
    
    elif choice == "2":
        sign_up()
    
    elif choice == "3":
        print("Goodbye!")
    
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

