#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Represents a base geometry class """


    def area(self):
        """Area not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the argument value as integer"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
