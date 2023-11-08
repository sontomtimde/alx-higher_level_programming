#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key is None or value is None:
        print("Error: Key and value must not be None.")
        return
    a_dictionary[key] = value
    return a_dictionary
