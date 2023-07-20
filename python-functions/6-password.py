#!/usr/bin/python3

def validate_password(password):
    # Check for password length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not has_uppercase or not has_lowercase or not has_digit:
        return False

    # Check for spaces in the password
    if ' ' in password:
        return False

    return True
