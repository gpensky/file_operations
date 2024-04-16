"""office.py - This module provides functions to read/write microsoft office files."""

import pandas
import textract


# Python Object -> File
# -----------------------------------------------------------------------------


def list2excel(file_path: str, data: list[dict], encoding: str = "utf8") -> None:
    """Saves list of dict to excel file.

    Args:
        file_path (str): file path of xlsx file
        data (list): list of dict to be saved
        encoding (str, optional): encoding. Defaults to "utf8".
    """
    del encoding
    df = pandas.DataFrame.from_dict(data)
    df.to_excel(file_path)


# File -> Python Object
# -----------------------------------------------------------------------------


def doc2str(file_path: str, encoding: str = "utf8") -> str:
    """Read text of doc file.

    Args:
        file_path (str): file path of doc file
        encoding (str, optional): encoding. Defaults to "utf8".

    Returns:
        str: text
    """

    text = textract.process(file_path, encoding=encoding)
    text = text.decode(encoding)
    return text
