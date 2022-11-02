#!/usr/bin/python3
"""rectangle."""
from models.base import Base


class Rectangle(Base):
    """

    This is a rectangle class.

    ...

    Attributes

    ----------

    __width:
        this is the width of the rectangle

    __height:
        this is the height of the rectangle
    __x:
       x
    __y:
       y

    Methods

    -------

    __init__:
          class constructor

    """
    @property
    def width(self):
        """
        Parameters

        ----------

        None

        """
        return self.__width

    @width.setter
    def width(self, value):
        """

        Parameters

        ----------

        None

        """
        self.__width = value

    @property
    def height(self):
        """
        Parameters

        ----------

        None

        """
        return self.__height

    @height.setter
    def height(self, value):
        """

        Parameters

        ----------

        None

        """
        self.__width = value

    @property
    def x(self):
        """
        Parameters

        ----------

        None

        """
        return self.__x

    @width.setter
    def x(self, value):
        """

        Parameters

        ----------

        None

        """
        self.__x = value

    @property
    def y(self):
        """
        Parameters

        ----------

        None

        """
        return self.__y

    @width.setter
    def y(self, value):
        """

        Parameters

        ----------

        None

        """
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Parameters.
        ----------

        width:
            width
        height:
            height
        x:
            x
        y:
           y
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y

        if id is not None:
            self.id = id
        else:
            self.id = Base.id
