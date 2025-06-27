import hashlib
from utils import get_valid_input

def check_username(username):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username = line.strip().split(":")[0]
                if username == stored_username:
                    return True
        return False
    except FileNotFoundError:
        return False

def is_username_available(username):
    """Check if username is available (not empty and not taken)"""
    if not username:
        print("Username cannot be empty")
        return False
    if check_username(username):
        print("Username already exists")
        return False
    return True

def save_user(username, password):
    """Save user credentials to file"""
    try:
        with open("users.txt", "a") as file:
            file.write(f"{username}:{password}\n")
        return True
    except Exception as e:
        print(f"Error saving user: {e}")
        return False

def sign_up():
    # Get valid username
    username = get_valid_input(
        "Enter your username: ",
        "Username cannot be empty",
        is_username_available
    )
    
    # Get valid password
    password = get_valid_input(
        "Enter your password: ",
        "Password cannot be empty"
    )
    
    # Hash password and save user
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if save_user(username, hashed_password):
        print("Registration successful!")
    else:
        print("Registration failed. Please try again.")

sign_up()