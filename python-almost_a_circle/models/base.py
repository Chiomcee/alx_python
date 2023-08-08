#!/usr/bin/python3
"""
    Base Module
"""


class Base:
    """Base class to be inherited by all othere classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initizes the instance of the Base class
            takes one optional argument, id. If  an id value
            is provided, it is assigned to the id attribute of
            the instance,

        otherwise:
            the counter is incremented, with it's current
            value assigned to the id attribute of the instanc.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
