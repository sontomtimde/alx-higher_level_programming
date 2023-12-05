#!/usr/bin/python3
"""Define a function to retrieve attributes and methods of an object."""


def lookup(obj):
    """
    Return a list of attributes and methods of the given object.

    Args:
    obj (object): The object to inspect.

    Returns:
    list: A list containing the names of attributes and methods.
    """
    return dir(obj)
