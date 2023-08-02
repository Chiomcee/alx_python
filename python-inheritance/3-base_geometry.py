#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """Creates an empty class"""

    def __dir__(cls):
        # get list of all attributes for this classand exclude_init_subclass
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']
