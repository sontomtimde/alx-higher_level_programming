#!/usr/bin/python3
"""Define a function to convert a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """
    Return a Python object representation of a JSON string.

    Args:
    my_str (str): The JSON string to convert to a Python object.

    Returns:
    object: The Python object converted from the JSON string.
    """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None  # or handle the error as required
