"""Test csv"""

import os
import pytest

from file_operations.csv import csv2list


@pytest.fixture(name="test_file_paths")
def fixture_test_file_paths() -> dict:
    """Get test file paths

    Returns:
        dict: test file paths
    """
    return {
        "01": os.path.join("tests", "test_files", "csv_test_file_01.csv"),
        "02": os.path.join("tests", "test_files", "csv_test_file_02.csv"),
    }


@pytest.fixture(name="expected_result")
def fixture_expected_result() -> list:
    """Set expected result

    Returns:
        list: expected result
    """

    return [
        {"Age": "30", "City": "New York", "Name": "João"},
        {"Age": "25", "City": "Los Angeles", "Name": "Emily"},
        {"Age": "35", "City": "Chicago", "Name": "David"},
    ]


def test_csv2list(test_file_paths: dict, expected_result: list):
    """Test csv.csv2list standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result (list): expected result
    """

    result = csv2list(test_file_paths["01"])
    assert result == expected_result

def test_csv2list_comma(test_file_paths: dict, expected_result: list):
    """Test csv.csv2list with comma separator

    Args:
        test_file_paths (dict): test file paths
        expected_result (list): expected result
    """

    result = csv2list(test_file_paths["02"], delimiter=",")
    assert result == expected_result
