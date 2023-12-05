#!/usr/bin/python3
"""Defining class Student."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student object.

        Args:
        attrs (list): A list of attributes to include in the dictionary.
                      If None, returns all attributes.

        Returns:
        dict: A dictionary representation of the Student object.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """
        Replace attributes of the Student object from a JSON-like dictionary.

        Args:
        json_data (dict): A JSON-like dictionary containing attribute-value pairs.
        """
        if isinstance(json_data, dict):
            for k, v in json_data.items():
                setattr(self, k, v)
        else:
            raise ValueError("Invalid JSON-like dictionary input.")

# Example usage:
if __name__ == "__main__":
    # Creating a Student object
    student = Student("John", "Doe", 25)
    
    # Getting JSON representation
    student_json = student.to_json()
    print(student_json)
    
    # Reloading attributes from JSON-like dictionary
    new_data = {"first_name": "Alice", "last_name": "Smith", "age": 30}
    student.reload_from_json(new_data)
    updated_json = student.to_json()
    print(updated_json)
