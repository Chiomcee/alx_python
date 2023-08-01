#!/usr/bin/python3
"""Function that checks if an object is exactly an instance
    of a specified class"""

def is_same_class(obj, a_class):
    """Takes two arguments, compares the type using
    the type function with the specified class.

    Returns:
        if the obj type match the class- return True
        otherwisw - False.
    """
    return (type(obj) == a_class)
