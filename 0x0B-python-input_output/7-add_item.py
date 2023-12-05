#!/usr/bin/python3
"""Adding arguments to the Python list."""
import sys
from pathlib import Path

# Importing the functions directly for clarity
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_to_list():
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    try:
        save_to_json_file(items, "add_item.json")
        print("Items added successfully.")
    except Exception as e:
        print(f"Error adding items: {e}")

if __name__ == "__main__":
    add_items_to_list()
