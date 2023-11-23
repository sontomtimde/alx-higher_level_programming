#!/usr/bin/python3
"""Define the square as per 2-square.py"""


class Square:
    """Defining the square by size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
