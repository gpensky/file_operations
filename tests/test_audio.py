"""Test audio"""

import os
from difflib import SequenceMatcher
import pytest

from file_operations.audio import audio2str


@pytest.fixture(name="test_file_paths")
def fixture_test_file_paths() -> dict:
    """Get test file paths.
    Data from: https://audio-samples.github.io/

    Returns:
        dict: test file paths
    """
    return {
        "01": os.path.join("tests", "test_files", "audio_test_file_01.mp3"),
        "02": os.path.join("tests", "test_files", "audio_test_file_02.mp3"),
        "03": os.path.join("tests", "test_files", "audio_test_file_03.mp3"),
        "04": os.path.join("tests", "test_files", "audio_test_file_04.mp3"),
        "05": os.path.join("tests", "test_files", "audio_test_file_05.mp3"),
    }


@pytest.fixture(name="expected_result")
def fixture_expected_result() -> str:
    """Set expected result

    Returns:
        str: expected result
    """

    return "My dear Fanny, you feel these things a great deal too much. I am most happy that you like the chain"


def test_audio2str_test_file_01(test_file_paths: dict, expected_result: str):
    """Test csv.csv2list standar config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    result = audio2str(test_file_paths["01"], model_name="tiny")
    similarity = SequenceMatcher(None, expected_result, result).ratio()
    assert similarity >= 0.9


def test_audio2str_test_file_02(test_file_paths: dict, expected_result: str):
    """Test csv.csv2list standar config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    result = audio2str(test_file_paths["02"], language="en", model_name="tiny")
    similarity = SequenceMatcher(None, expected_result, result).ratio()
    assert similarity >= 0.9


def test_audio2str_test_file_03(test_file_paths: dict, expected_result: str):
    """Test csv.csv2list standar config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    result = audio2str(test_file_paths["03"], model_name="tiny")
    similarity = SequenceMatcher(None, expected_result, result).ratio()
    assert similarity >= 0.9


def test_audio2str_test_file_04(test_file_paths: dict, expected_result: str):
    """Test csv.csv2list standar config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    result = audio2str(test_file_paths["04"], model_name="tiny")
    similarity = SequenceMatcher(None, expected_result, result).ratio()
    assert similarity >= 0.9


def test_audio2str_test_file_05(test_file_paths: dict, expected_result: str):
    """Test csv.csv2list standar config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    result = audio2str(test_file_paths["05"], model_name="tiny")
    similarity = SequenceMatcher(None, expected_result, result).ratio()
    assert similarity >= 0.9
