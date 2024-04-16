"""pdf.py - This module provides functions to read/write `pdf` files."""

from file_operations._read_pdf import read_pdf


# File -> Python Object
# -----------------------------------------------------------------------------


def pdf2str(file_path: str) -> str:
    """Read text of pdf file.

    Args:
        file_path (str): file path of pdf file

    Returns:
        str: text
    """

    return read_pdf(file_path)
