#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not isinstance(a_dictionary, dict):
        raise TypeError("Input must be a dictionary.")
    return {k: v * 2 if isinstance(v, (int, float)) else v for k, v in a_dictionary.items()}
