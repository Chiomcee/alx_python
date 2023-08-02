#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """Creates an empty class"""
    def __class_getitem__(cls, params):
        return cls

    def __str__(self):
        return str(self.__dict__)

    def __dir__(self):
        class_dir = dir(type(self))
        class_dir.remove("__init_subclass__")
        return class_dir

    def __sizeof__(self):
        return object.__sizeof__(self)

