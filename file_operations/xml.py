"""xml.py - This module provides functions to read/write `xml` files."""

from xml.parsers.expat import ExpatError
import xmltodict


# File -> Python Object
# -----------------------------------------------------------------------------


def xml2dict(file_path: str, encoding: str = "utf8") -> dict:
    """Read XML and return dict.

    Args:
        file_path (str): file path of xml file
        encoding (str, optional): encoding. Defaults to "utf8".

    Returns:
        dict: data
    """

    with open(file_path, "r", encoding=encoding) as f:
        content = f.read()
        try:
            return xmltodict.parse(content)
        except ExpatError:
            return {}
