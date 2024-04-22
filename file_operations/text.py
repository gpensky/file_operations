"""text.py - This module provides functions to read/write text files."""

import pandoc

# Python Object -> File
# -----------------------------------------------------------------------------


def str2txt(file_path: str, data: str, encoding: str = "utf8") -> None:
    """Saves str to txt file

    Args:
        file_path (str): file path of txt file
        data (str): str to be encoding
        encoding (str, optional): _description_. Defaults to "utf8".
    """

    with open(file_path, "w", encoding=encoding) as file:
        file.write(data)


# File -> Python Object
# -----------------------------------------------------------------------------


def txt2str(file_path: str, encoding: str = "utf8") -> str:
    """Read text of txt file.

    Args:
        file_path (str): file path of txt file
        encoding (str, optional): encoding. Defaults to "utf8".

    Returns:
        str: text
    """

    with open(file_path, "r", encoding=encoding) as file:
        return file.read()


# String -> String
# -----------------------------------------------------------------------------


def html2md(data: str) -> str:
    """Converts html to markdown

    Args:
        data (str): html string

    Returns:
        str: markdown string
    """

    return pandoc.write(pandoc.read(data, format="html"), format="markdown")


def md2html(data: str) -> str:
    """Converts markdown to html

    Args:
        data (str): markdown string

    Returns:
        str: html string
    """

    return pandoc.write(pandoc.read(data, format="markdown"), format="html")
