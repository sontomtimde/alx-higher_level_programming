#!/usr/bin/python3
class Rectangle:
    """A class to represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_dimension(value, "height")
        self.__height = value

    def _validate_dimension(self, value, dimension_name):
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")
