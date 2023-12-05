#!/usr/bin/python3
"""Define a function to append text to a UTF-8 text file."""


def append_write(filename="", text=""):
    """
    Append text to a UTF-8 text file.

    Args:
    filename (str): The path to the file. Default is an empty string.
    text (str): The text to append to the file. Default is an empty string.

    Returns:
    bool: True if the text was successfully appended, False otherwise.
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text)
        return True
    except Exception as e:
        print(f"Error appending to file: {e}")
        return False
