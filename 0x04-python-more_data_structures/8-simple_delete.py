#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not isinstance(a_dictionary, dict):
        print("Error: Input must be a dictionary.")
        return
    if key in a_dictionary:
        a_dictionary.pop(key)
        print(f"Key '{key}' deleted.")
    else:
        print(f"Key '{key}' not found in the dictionary.")
    return a_dictionary
