#!/usr/bin/python3
"""read_file."""


def number_of_lines(filename=""):
    """
    Parameters.

    ----------

    size: int

       The size of the square

    """
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
