#!/usr/bin/python3
"""Representing the class Square"""


class Square:
    """Defines a class square."""

    def __init__(self, size=0):
        """Initializing a new object square.

        Args:
            size(int):must be an integer,
            represents size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
