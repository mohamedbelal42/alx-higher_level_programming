#!/usr/bin/python3
"""defines class Student."""

class Student:
    """representation of a student."""
    def __init__(self, first_name, last_name, age):
        """initializes the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retuens a dictionary representation of a student instance."""
        return self.__dict__
