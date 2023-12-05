#!/usr/bin/python3
"""Define a function to write a Python object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a JSON file.

    Args:
    my_obj: The Python object to be written to the JSON file.
    filename (str): The path to the JSON file to be created/overwritten.
    """
    try:
        with open(filename, "w") as f:
            json.dump(my_obj, f)
    except Exception as e:
        print(f"Error saving to JSON file: {e}")
        # Consider handling the error or raising an exception as appropriate
