"""dir.py - This module provides functions to read information and to make 
operations in directories."""

import os
import shutil


# Directory -> Python Object
# -----------------------------------------------------------------------------


def dir2dict(folder_path: str) -> dict:
    """Get dict of all files in folder

    Args:
        folder_path (str): folder path

    Returns:
        dict: dict of files (dict[file_name] = file_path)
    """

    file_paths = dict()
    for file in os.listdir(folder_path):
        file_paths[file] = os.path.join(folder_path, file)
    return file_paths


def dir2list(
    folder_path: str, file_extension: str = None, only_file_name: bool = False
) -> list:
    """_summary_

    Args:
        folder_path (str): folder path
        file_extension (str, optional): limit search with files ending in, if None
        return list of all files in folder. Defaults to None.

    Returns:
        list: list of file paths
    """

    file_paths = []
    for file in os.listdir(folder_path):
        if file_extension is not None:
            if file.endswith(file_extension):
                if only_file_name:
                    file_paths.append(file)
                else:
                    file_paths.append(os.path.join(folder_path, file))
        else:
            if only_file_name:
                file_paths.append(file)
            else:
                file_paths.append(os.path.join(folder_path, file))

    return file_paths


# Other file system utilities
# -----------------------------------------------------------------------------


def file_check(file_path: str) -> bool:
    """Checks if file exists.

    Args:
        file_path (str): file path

    Returns:
        bool: True if file exists
    """

    return os.path.isfile(file_path)


def folder_check(folder_path: str) -> bool:
    """Checks if folder exists.

    Args:
        folder_path (str): folder path

    Returns:
        bool: True if folder exists
    """
    return os.path.isdir(folder_path)


def delete_file(file_path: str) -> None:
    """Delete file.

    Args:
        file_path (str): file path of file to be deleted
    """
    os.remove(file_path)


def clear_folder(folder_path: str) -> None:
    """Delete all files in folder.

    Args:
        folder_path (str): folder path
    """

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
