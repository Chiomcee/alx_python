#!/usr/bin/python3
"""
    A Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of size"""
        self.width = value
        self.height = value
