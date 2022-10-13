#!/usr/bin/python3
"""Fourth square."""


class Square:
    """
    This is a square class.

    ...

    Attributes
    ----------
    __size:
        this is the size of the square

    Methods
    -------
    None

    """

    def __init__(self, size=0):
        """
        Parameters.

        ----------

        size: int

            The size of the square

        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Paramaneters.

        ------------
        None

        """
        return self.__size * self.__size
