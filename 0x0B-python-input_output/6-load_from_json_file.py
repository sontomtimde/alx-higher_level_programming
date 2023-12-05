#!/usr/bin/python3
"""Define a function to read a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Read a Python object from a JSON file.

    Args:
    filename (str): The path to the JSON file to be read.

    Returns:
    object: The Python object created from the JSON file.
    """
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {filename}: {e}")
        return None
    except Exception as e:
        print(f"Error reading from JSON file {filename}: {e}")
        return None
