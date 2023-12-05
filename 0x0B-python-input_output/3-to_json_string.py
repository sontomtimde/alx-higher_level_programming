#!/usr/bin/python3
"""Define a function to convert a Python object to a JSON string."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object.

    Args:
    my_obj: The Python object to convert to JSON.

    Returns:
    str: The JSON string representation of the object.
    """
    try:
        return json.dumps(my_obj)
    except Exception as e:
        print(f"Error converting to JSON: {e}")
        return None  # or handle the error according to your needs
