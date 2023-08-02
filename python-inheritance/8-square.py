#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        """Initializes a new Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
