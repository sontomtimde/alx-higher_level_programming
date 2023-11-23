#!/usr/bin/python3
""" The class square definition on 1-square.py"""


class Square:
    """Initialize the size"""
    def __init__(self, size=0):
        """Initialize the new square"""
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
