#!/usr/bin/python3
"""Defines a subclass Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry attributes and methods"""
    def __init__(self, width, height):
        """Initializes a new Rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
