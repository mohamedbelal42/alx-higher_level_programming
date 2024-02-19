#!/usr/bin/python3
"""module for Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """a subclass representing a square."""
    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method for area of a square."""
        return self.__size ** 2
