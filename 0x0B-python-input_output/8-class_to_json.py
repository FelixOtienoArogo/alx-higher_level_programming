#!/usr/bin/python3
"""class_to_json."""


def class_to_json(obj):
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
    return vars(obj)
