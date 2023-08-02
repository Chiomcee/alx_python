#!/usr/bin/python3
"""Defines a subclass Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry attributes and methods"""

    def __dir__(cls):
        # get list of all attributes for this classand exclude_init_subclass
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']

    def __init__(self, width, height):
        """Initializes a new Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
