#!/usr/bin/python3
"""base."""


class Base:
    """
    This is the base class.

    ....

    Attributes
    ----------
    __nb-objects
        this is the number of objects

    Methods
    -------
    __init__
        a class constructor

    """

    __nb_objects = 0

    def __init__(self,  id=None):
        """
        Parameters.

        ----------

        None

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
