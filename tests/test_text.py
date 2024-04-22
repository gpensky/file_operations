"""Test text"""

import os
import pytest

from file_operations.text import str2txt, txt2str, html2md, md2html


@pytest.fixture(name="test_file_paths")
def fixture_test_file_paths() -> dict:
    """Get test file paths

    Returns:
        dict: test file paths
    """
    return {
        "01": os.path.join("tests", "test_files", "text_test_file_01.txt"),
        "02": os.path.join("tests", "test_files", "text_test_file_02.txt"),
    }


@pytest.fixture(name="expected_result")
def fixture_expected_result() -> list:
    """Set expected result

    Returns:
        list: expected result
    """

    return "text test file\nwith multiple lines"


def test_str2txt(test_file_paths: dict, expected_result: str):
    """Test text.str2txt standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    str2txt(test_file_paths["02"], expected_result)
    result = ""
    with open(test_file_paths["02"], "r", encoding="utf8") as file:
        result = file.read()
    os.remove(test_file_paths["02"])
    assert result == expected_result


def test_txt2str(test_file_paths: dict, expected_result: str):
    """Test text.txt2str standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result (str): expected result
    """

    result = txt2str(test_file_paths["01"])
    assert result == expected_result

def test_html2md():
    html_content = "<h1>Hello, World!</h1>"
    expected_md = "# Hello, World!"
    assert html2md(html_content) == expected_md

def test_md2html():
    md_content = "# Hello, World!"
    expected_html = "<h1>Hello, World!</h1>"
    assert md2html(md_content) == expected_html