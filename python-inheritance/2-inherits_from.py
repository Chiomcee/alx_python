#!/usr/bin/python3
"""Function that checks if an obj is an instance of a class,
    that inherited from the specified class.
"""

def inherits_from(obj, a_class):
    """Takes two arguments. 

        Uses the type func to get the type of the object.
        Uses issubclass func to check if the type of the obj is
        a subclass of the specified a_class.

        Returns:
            if obj is a subclass of a_class return - True
            otherwise - False
    """

    return issubclass(type(obj), a_class)
