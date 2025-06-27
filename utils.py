def get_valid_input(prompt, error_message, validator=None):
    """Get valid input from user with custom validation
    
    Args:
        prompt (str): The input prompt to display
        error_message (str): Error message for empty input
        validator (function, optional): Custom validation function that returns True/False
    
    Returns:
        str: Valid user input
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print(error_message)
            continue
        if validator and not validator(value):
            continue
        return value 