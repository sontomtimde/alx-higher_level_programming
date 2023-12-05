#!/usr/bin/python3
"""Defining the Student class with a customized JSON representation."""


class Student:
    """Representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(age, int):
            raise ValueError("Invalid input data types.")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a customized dictionary representation."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

# Example usage:
if __name__ == "__main__":
    student = Student("John", "Doe", 25)
    student_json = student.to_json()
    print(student_json)
