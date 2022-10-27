#!/usr/bin/python3
"""class_to_json."""


class Student:
    """
    class.

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

    def __init__(self, first_name, last_name, age):
        """
        Properties.

        __________

        None

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Properties.

        __________

        None

        """
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary
