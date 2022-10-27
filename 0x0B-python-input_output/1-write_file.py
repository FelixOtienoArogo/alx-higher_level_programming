#!/usr/bin/python3
"""write_file."""


def write_file(filename="", text=""):
    """
    Parameters.

    ----------

    size: int

       The size of the square

    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
