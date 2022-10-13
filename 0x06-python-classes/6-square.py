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

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters.

        ----------

        size: int

            The size of the square
        position: int

            The position

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Paramaneters.

        ------------

        None

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Parameters.

        ----------

        None

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """

        Paramaneters.

        ------------

        None

        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        Properties.

        ----------
        None

        """
        return self.__position

    @position.setter
    def position(self, value):
        """

        Properties.

        ----------
        value
            The value to set

        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Parameters.

        ----------

        None

        """
        if (self.__size == 0):
            print("")
        else:
            for line in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
