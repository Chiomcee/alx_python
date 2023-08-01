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

    @property
    def size(self):
        """set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
