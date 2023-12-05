#!/usr/bin/python3
"""Define a function to convert a Python class instance to a JSON dictionary."""


def class_to_json(obj):
    """Convert a Python class instance to a JSON-compatible dictionary."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        # You might add more complex serialization logic for non-dictionary objects
        return str(obj)  # Or handle non-serializable objects differently

# Example usage:
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of MyClass
my_instance = MyClass("John", 30)

# Using class_to_json function
result = class_to_json(my_instance)
print(result)
