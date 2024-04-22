"""zip.py - This module provides functions to read/write `zip` files."""

import shutil
import zipfile
import os


# File -> Directory
# -----------------------------------------------------------------------------


def zip2dir(file_path: str, output_folder_path: str) -> None:
    """Extract zip file contents to folder.

    Args:
        file_path (str): file path of zip file
        output_folder_path (str): output folder path
    """

    try:
        with zipfile.ZipFile(file_path, "r") as zip_file:
            for member in zip_file.namelist():
                filename = os.path.basename(member)

                # skip directories
                if not filename:
                    continue

                # copy file (taken from zipfile's extract)
                source = zip_file.open(member)
                target = open(os.path.join(output_folder_path, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
    except zipfile.BadZipFile:
        return None
