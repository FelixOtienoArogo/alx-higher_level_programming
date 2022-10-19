#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """
    This is a rectangle class.

    ...

    Attributes
    ----------
    __width:
        this is the width of the rectangle
    __height:
        this is the height of the rectangle

    Methods
    -------
    None

    """

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """
        Parameters.

        __________

        None

        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Parameters.

        __________

        None

        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """
        Parameters.

        ----------

        size: int

            The size of the square

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Properties.

        __________

        None

        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Paramaneters.

        ------------

        None

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Parameters.

        ----------

        None

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Paramaneters.

        ------------

        None

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Parameters.

        ----------

        None

        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """

        Paramaneters.

        ------------

        None

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Parameters.

        _________

        None

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Parameters.

        __________

        None

        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """
        Parameters.

        __________

        None

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
