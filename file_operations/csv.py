"""csv.py - This module provides functions to read/write `csv` files."""

import csv

# File -> Python Object
# -----------------------------------------------------------------------------


def csv2list(file_path: str, encoding: str = "utf-8-sig", delimiter=";") -> list[dict]:
    """Reads CSV and returns list of dicts.

    Args:
        file_path (str): file path of csv file
        encoding (str, optional): encoding. Defaults to "utf-8-sig".

    Returns:
        list[dict]: data read from file
    """

    with open(file_path, "r", encoding=encoding) as f:
        table = csv.DictReader(f, delimiter=delimiter)
        return list(table)
