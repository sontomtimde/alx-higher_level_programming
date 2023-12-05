#!/usr/bin/python3
"""Define a function to read and return the contents of a UTF-8 text file."""


def read_file(filename=""):
    """
    Read the contents of a UTF-8 text file and return as a string.

    Args:
    filename (str): The path to the file. Default is an empty string.

    Returns:
    str: The content of the file as a string.
    """
    try:
        with open(filename, encoding="utf-8") as f:
            file_content = f.read()
            return file_content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error reading file: {e}"
