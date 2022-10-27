#!/usr/bin/python3
"""read_file."""


def append_write(filename="", text=""):
    """
    Parameters.

    ----------

    size: int

       The size of the square

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
