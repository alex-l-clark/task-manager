import hashlib
from utils import get_valid_input

def find_user_credentials(username):
    """Find stored credentials for a given username"""
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username:
                    return stored_password
        return None
    except FileNotFoundError:
        return None

def verify_password(input_password, stored_password):
    """Verify if input password matches stored password"""
    hashed_input = hashlib.sha256(input_password.encode()).hexdigest()
    return hashed_input == stored_password

def login():
    """Core login function - returns (success, message)"""
    # Get valid username
    username = get_valid_input(
        "Enter your username: ",
        "Username cannot be empty"
    )
    
    # Check if username exists in system
    stored_password = find_user_credentials(username)
    if not stored_password:
        return False, "Invalid username"
    
    # Get and verify password
    password = get_valid_input(
        "Enter your password: ",
        "Password cannot be empty"
    )
    
    if verify_password(password, stored_password):
        return True, "Login successful"
    else:
        return False, "Invalid password"

def login_with_retry():
    """Login function with retry logic for CLI interface"""
    while True:
        success, message = login()
        print(message)
        
        if success:
            return True
        
        # Ask if user wants to retry
        retry = input("Try again? (y/n): ").strip().lower()
        if retry not in ['y', 'yes']:
            print("Login cancelled")
            return False