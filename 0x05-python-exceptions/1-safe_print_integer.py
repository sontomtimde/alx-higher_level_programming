#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print(f"{int(value)}")
        return True
    except (ValueError, TypeError) as e:
        print(f"Error: {e}. Couldn't print {value} as an integer.")
        return False
