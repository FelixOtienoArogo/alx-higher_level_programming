#!/usr/bin/python3
"""read_file."""


def read_lines(filename=""):
    """
    Parameters.

    ----------

    size: int

       The size of the square

    """
    with open(filename, "r", encoding="UTF-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for index in range(nb_lines):
            print(f.readline(), end="")
