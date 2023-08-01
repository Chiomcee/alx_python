#!/usr/bin/python3
"""Function tht checks if an object is an instance of,
    or if is an instance of a class that inherited from,
    the specified class.
"""

def is_kind_of_class(obj, a_class):
    """takes two arguments. uses the instance func to check
        if the obj is an instance of the specified class or 
        any of its subclasses.

        returns:
            if it is  - returns True
            otherwise - False
    """
    return isinstance(obj, a_class)


