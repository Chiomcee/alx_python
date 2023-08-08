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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # ================  HEIGHT  =======================
    @property
    def height(self):
        """Gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # ====================== X CORD =======================
    @property
    def x(self):
        """Gets the x  value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # ====================== Y CORD =======================
    @property
    def y(self):
        """Gets the y  value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle with #"""
        for i in range(self.__height):
            print('#' *self.__width)
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def display(self):
        """Update the display(self) using x cordinate"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """Update ro assign arguments to each attribute"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes.

        Args:
            *args: The positional arguments can be used to update id,
                   width, height, x, and y in that order.
            **kwargs: The keyword arguments can be used to update any
                   attribute by specifying the attribute name.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for index, arg in enumerate(args):
                if index < len(attrs):
                    setattr(self, attrs[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
