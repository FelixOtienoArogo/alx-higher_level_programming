#!/usr/bin/python3
"""to_json_string.py"""

import json


def load_from_json_file(filename):
    """
    Parameters.

    ----------

    size: int

       The size of the square

    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
