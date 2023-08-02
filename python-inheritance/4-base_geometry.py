#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Represents a base geometry class """

    def __dir__(cls):
        # get list of all attributes for this classand exclude_init_subclass
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']


    def area(self):
        """Area not yet implemented"""
        raise Exception("area() is not implemented")
