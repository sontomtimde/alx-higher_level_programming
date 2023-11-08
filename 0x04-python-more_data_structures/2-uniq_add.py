#!/usr/bin/python3

def uniq_add(my_list=[]):
    try:
        # Use a set to get unique elements and then sum them
        unique_elements = set(my_list)
        return sum(unique_elements)
    except TypeError:
        # Handle non-numeric elements in the list
        print("Error: All elements in the list should be numeric.")
        return None
