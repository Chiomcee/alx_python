#!/usr/bin/python3
"""
    A Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                            Defaults to 0.
            id (optional): The identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ================  WIDTH  =======================
    @property
    def width(self):
        """Gets the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value"""
        self.__width = value

    # ================  HEIGHT  =======================
    @property
    def height(self):
        """Gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        self.__height = value

    # ====================== X CORD =======================
    @property
    def x(self):
        """Gets the x  value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value"""
        self.__x = value

    # ====================== Y CORD =======================
    @property
    def y(self):
        """Gets the y  value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value"""
        self.__y = value



