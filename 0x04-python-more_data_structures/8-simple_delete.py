#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not isinstance(a_dictionary, dict):
        print("Error: Input must be a dictionary.")
        return
    a_dictionary.pop(key, None)
    return a_dictionary
