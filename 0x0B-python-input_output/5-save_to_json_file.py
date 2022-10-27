#!/usr/bin/python3
"""to_json_string.py"""

import json


def save_to_json_file(my_obj, filename):
    """
    Parameters.

    ----------

    size: int

       The size of the square

    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
