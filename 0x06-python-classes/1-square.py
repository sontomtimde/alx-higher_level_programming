#!/usr/bin/python3
"""Define the square and the size"""


class Square:
    """Solving the square"""

    def __init__(self, size=0):
        """Initialize the new square"""
        self.__size = size

    def get_size(self):
        """Get the size of the square"""
        return self.__size

    def set_size(self, new_size):
        """Set the size of the square"""
        if isinstance(new_size, (int, float)) and new_size >= 0:
            self.__size = new_size
        else:
            raise ValueError("Size must be a non-negative number")

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
