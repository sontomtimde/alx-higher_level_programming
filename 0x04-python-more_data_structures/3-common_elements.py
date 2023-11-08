#!/usr/bin/python3

def common_elements(set_1, set_2):
    try:
        # Check if the inputs are sets, then return their intersection
        if isinstance(set_1, set) and isinstance(set_2, set):
            return set_1 & set_2
        else:
            raise TypeError("Both inputs should be sets.")
    except TypeError as e:
        # Handle type errors and print an error message
        print(f"Error: {e}")
        return None
