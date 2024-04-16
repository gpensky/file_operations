"""Test dir"""

import os
import pytest

from file_operations.dir import (
    dir2dict,
    dir2list,
    file_check,
    folder_check,
    delete_file,
    clear_folder,
)


@pytest.fixture(name="create_test_folder")
def fixture_create_test_folder() -> dict:
    """Create test folder"""
    if not os.path.exists(os.path.join("tests", "test_files", "dir_test_folder_02")):
        os.mkdir(os.path.join("tests", "test_files", "dir_test_folder_02"))
        open(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_01.txt"
            ),
            "w",
            encoding="utf-8",
        ).close()
        open(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_02.txt"
            ),
            "w",
            encoding="utf-8",
        ).close()
        open(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_03.txt"
            ),
            "w",
            encoding="utf-8",
        ).close()


@pytest.fixture(name="test_folder_paths")
def fixture_test_folder_paths() -> dict:
    """Get test file paths

    Returns:
        dict: test file paths
    """
    return {
        "01": os.path.join("tests", "test_files", "dir_test_folder_01"),
        "02": os.path.join("tests", "test_files", "dir_test_folder_02"),
    }


@pytest.fixture(name="expected_result_dict_01")
def fixture_expected_result_dict_01() -> dict:
    """Set expected result

    Returns:
        dict: expected result
    """

    return {
        "dir_test_file_01.txt": str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_01", "dir_test_file_01.txt"
            )
        ),
        "dir_test_file_02.txt": str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_01", "dir_test_file_02.txt"
            )
        ),
        "dir_test_file_03.txt": str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_01", "dir_test_file_03.txt"
            )
        ),
    }


@pytest.fixture(name="expected_result_dict_02")
def fixture_expected_result_dict_02() -> dict:
    """Set expected result

    Returns:
        dict: expected result
    """

    return {
        "dir_test_file_01.txt": str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_01.txt"
            )
        ),
        "dir_test_file_02.txt": str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_02.txt"
            )
        ),
        "dir_test_file_03.txt": str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_03.txt"
            )
        ),
    }


@pytest.fixture(name="expected_result_list_01")
def fixture_expected_result_list_01() -> list:
    """Set expected result

    Returns:
        list: expected result
    """

    return [
        str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_01", "dir_test_file_01.txt"
            )
        ),
        str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_01", "dir_test_file_02.txt"
            )
        ),
        str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_01", "dir_test_file_03.txt"
            )
        ),
    ]


@pytest.fixture(name="expected_result_list_02")
def fixture_expected_result_list_02() -> list:
    """Set expected result

    Returns:
        list: expected result
    """

    return [
        str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_01.txt"
            )
        ),
        str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_02.txt"
            )
        ),
        str(
            os.path.join(
                "tests", "test_files", "dir_test_folder_02", "dir_test_file_03.txt"
            )
        ),
    ]


def test_dir2dict_test_folder_01(
    test_folder_paths: dict, expected_result_dict_01: dict
):
    """Test dir.dir2dict

    Args:
        test_folder_paths (dict): test folder paths
        expected_result_dict_01 (dict): expected result
    """

    result = dir2dict(test_folder_paths["01"])
    assert result == expected_result_dict_01


def test_dir2dict_test_folder_02(
    test_folder_paths: dict, expected_result_dict_02: dict, create_test_folder: None
):
    """Test dir.dir2dict

    Args:
        test_folder_paths (dict): test folder paths
        expected_result_dict_02 (dict): expected result
    """

    del create_test_folder
    result = dir2dict(test_folder_paths["02"])
    assert result == expected_result_dict_02


def test_dir2list_test_folder_01(
    test_folder_paths: dict, expected_result_list_01: list
):
    """Test dir.dir2list

    Args:
        test_folder_paths (dict): test folder paths
        expected_result_list_01 (list): expected result
    """

    expected_result_list_01.sort()
    result = dir2list(test_folder_paths["01"])
    result.sort()
    assert result == expected_result_list_01


def test_dir2list_test_folder_02(
    test_folder_paths: dict, expected_result_list_02: list, create_test_folder: None
):
    """Test dir.dir2list

    Args:
        test_folder_paths (dict): test folder paths
        expected_result_list_01 (list): expected result
    """

    del create_test_folder
    expected_result_list_02.sort()
    result = dir2list(test_folder_paths["02"])
    result.sort()
    assert result == expected_result_list_02


def test_file_check(test_folder_paths: dict):
    """Test dir.file_check

    Args:
        test_folder_paths (dict): test folder paths
    """

    result = file_check(os.path.join(test_folder_paths["01"], "dir_test_file_01.txt"))
    assert result is True


def test_folder_check(test_folder_paths: dict):
    """Test dir.folder_check

    Args:
        test_folder_paths (dict): test folder paths
    """

    result = folder_check(test_folder_paths["01"])
    assert result is True


def test_delete_file(test_folder_paths: dict):
    """Test dir.delete_file

    Args:
        test_folder_paths (dict): test folder paths
    """

    delete_file(os.path.join(test_folder_paths["02"], "dir_test_file_01.txt"))
    result = os.path.isfile(
        os.path.join(test_folder_paths["02"], "dir_test_file_01.txt")
    )
    assert result is False


def test_clear_folder(test_folder_paths: dict):
    """Test dir.clear_folder

    Args:
        test_folder_paths (dict): test folder paths
    """

    clear_folder(test_folder_paths["02"])
    result = (
        os.path.isfile(os.path.join(test_folder_paths["02"], "dir_test_file_01.txt"))
        or os.path.isfile(os.path.join(test_folder_paths["02"], "dir_test_file_02.txt"))
        or os.path.isfile(os.path.join(test_folder_paths["02"], "dir_test_file_03.txt"))
    )
    os.rmdir(test_folder_paths["02"])
    assert result is False
