"""json.py - This module provides functions to read/write `json` files."""

import json


# Python Object -> File
# -----------------------------------------------------------------------------


def dict2json(file_path: str, data: str, encoding: str = "utf8") -> None:
    """Saves dictionary to json file.

    Args:
        file_path (str): file path of json file
        data (str): dict to be saved
        encoding (str, optional): encoding. Defaults to "utf8".
    """

    with open(file_path, "w", encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def list2json(file_path: str, data: list[dict], encoding: str = "utf8") -> None:
    """Saves list of dict to json file.

    Args:
        file_path (str): file path of json file
        data (list): list of dict to be saved
        encoding (str, optional): encoding. Defaults to "utf8".
    """

    with open(file_path, "w", encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def list2jsonl(file_path: str, data: list[dict], encoding: str = "utf8") -> None:
    """Saves list of dict to json file.

    Args:
        file_path (str): file path of jsonl file
        data (list): list of dict to be saved
        encoding (str, optional): encoding. Defaults to "utf8".
    """

    with open(file_path, "w", encoding=encoding) as file:
        for entry in data:
            json.dump(entry, file, ensure_ascii=False)
            file.write("\n")


# File -> Python Object
# -----------------------------------------------------------------------------


def json2dict(file_path: str, encoding: str = "utf8") -> dict:
    """Reads json and return dict.

    Args:
        file_path (str): file path of json file
        encoding (str, optional): encoding. Defaults to "utf8".

    Returns:
        dict: data from json
    """

    with open(file_path, "r", encoding=encoding) as f:
        return json.load(f)


def json2list(file_path: str, encoding: str = "utf-8-sig") -> list[dict]:
    """Reads json and return list of dicts.

    Args:
        file_path (str): file path of json file
        encoding (str, optional): encoding. Defaults to "utf-8-sig".

    Returns:
        list[dict]: data read from file
    """

    with open(
        file_path,
        "r",
        encoding=encoding,
    ) as f:
        return json.loads(f.read())


def jsonl2list(file_path: str, encoding: str = "utf-8-sig") -> list[dict]:
    """Reads jsonl and return list of dicts.

    Args:
        file_path (str): file path of jsonl file
        encoding (str, optional): encoding. Defaults to "utf-8-sig".

    Returns:
        list[dict]: data read from file
    """
    data = []
    with open(file_path, "r", encoding=encoding) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def json2listtuple(file_path: str, encoding: str = "utf-8-sig") -> list[tuple]:
    """Reads json and return list of tuples.

    Args:
        file_path (str): file path of json file
        encoding (str, optional): encoding. Defaults to "utf-8-sig".

    Returns:
        list[tuple]: data read from file
    """
    data = []
    with open(
        file_path,
        "r",
        encoding=encoding,
    ) as f:
        data = json.loads(f.read())

    return [tuple(item) for item in data]
