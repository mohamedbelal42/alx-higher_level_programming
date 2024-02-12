#!/usr/bin/python3
"""Defining an empty class Rectangle."""

class Rectangle:
    """Empty representation of a Rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes the rectangle."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """returns the premiter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representation of the rectangle."""
        string = ""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every deletion of a rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger of two rectangles.

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: if rect_1 or rect_2 are not instances of rectangle.
        Returns:
            the rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Instantiates a new square.

        Args:
            size: the size of the new square.

        """
        return cls(size, size)
