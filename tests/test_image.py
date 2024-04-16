"""Test image"""

import os
from difflib import SequenceMatcher
import pytest

from file_operations.image import image2str


@pytest.fixture(name="test_file_paths")
def fixture_test_file_paths() -> dict:
    """Get test file paths

    Returns:
        dict: test file paths
    """
    return {
        "01": os.path.join("tests", "test_files", "image_test_file_01.jpg"),
        "02": os.path.join("tests", "test_files", "image_test_file_02.jpg"),
        "03": os.path.join("tests", "test_files", "image_test_file_03.jpg"),
    }


@pytest.fixture(name="expected_result")
def fixture_expected_result() -> dict:
    """Set expected result

    Returns:
        dict: expected result
    """

    return {
        "01": "Test image 01\n",
        "02": "Test image 02\n",
        "03": "Test image 03\nnow with\nmultiple lines\n",
    }


def test_image2str_test_file_01(test_file_paths: dict, expected_result: list):
    """Test image.image2str standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result (list): expected result
    """

    result = image2str(test_file_paths["01"], lang="eng")
    similarity = SequenceMatcher(None, expected_result["01"], result).ratio()
    assert similarity >= 0.95


def test_image2str_test_file_02(test_file_paths: dict, expected_result: list):
    """Test image.image2str standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result (list): expected result
    """

    result = image2str(test_file_paths["02"], lang="eng")
    similarity = SequenceMatcher(None, expected_result["02"], result).ratio()
    assert similarity >= 0.95


def test_image2str_test_file_03(test_file_paths: dict, expected_result: list):
    """Test image.image2str standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result (list): expected result
    """

    result = image2str(test_file_paths["03"], lang="eng")
    similarity = SequenceMatcher(None, expected_result["03"], result).ratio()
    assert similarity >= 0.95
