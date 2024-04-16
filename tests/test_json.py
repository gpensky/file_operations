"""Test json"""

import os
import json
import pytest

from file_operations.json import (
    dict2json,
    list2json,
    list2jsonl,
    json2dict,
    json2list,
    jsonl2list,
    json2listtuple,
)


@pytest.fixture(name="test_file_paths")
def fixture_test_file_paths() -> dict:
    """Get test file paths

    Returns:
        dict: test file paths
    """
    return {
        "01": os.path.join("tests", "test_files", "json_test_file_01.json"),
        "02": os.path.join("tests", "test_files", "json_test_file_02.json"),
        "03": os.path.join("tests", "test_files", "json_test_file_03.json"),
        "04": os.path.join("tests", "test_files", "json_test_file_04.jsonl"),
        "05": os.path.join("tests", "test_files", "json_test_file_05.json"),
        "06": os.path.join("tests", "test_files", "json_test_file_06.json"),
        "07": os.path.join("tests", "test_files", "json_test_file_07.jsonl"),
    }


@pytest.fixture(name="expected_result_dict")
def fixture_expected_result_dict() -> dict:
    """Set expected result

    Returns:
        dict: expected result
    """

    return {
        "books": [
            {
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "publication_year": 1951,
                "genres": ["Fiction", "Coming-of-age"],
                "rating": 4.1,
                "summary": "The story of Holden Caulfield, a young man who struggles with alienation and identity in the aftermath of being expelled from prep school.",
            },
            {
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "publication_year": 1960,
                "genres": ["Fiction", "Southern Gothic"],
                "rating": 4.4,
                "summary": "Set in the 1930s, it follows the journey of young Scout Finch, her brother Jem, and their father Atticus, a lawyer, as they navigate issues of race and morality in their Alabama town.",
            },
            {
                "title": "1984",
                "author": "George Orwell",
                "publication_year": 1949,
                "genres": ["Fiction", "Dystopian"],
                "rating": 4.6,
                "summary": "A dystopian novel set in a totalitarian regime where individualism and independent thinking are suppressed by the government led by 'Big Brother.'",
            },
        ]
    }


@pytest.fixture(name="expected_result_list")
def fixture_expected_result_list() -> list:
    """Set expected result

    Returns:
        list: expected result
    """

    return [
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "publication_year": 1951,
            "genres": ["Fiction", "Coming-of-age"],
            "rating": 4.1,
            "summary": "The story of Holden Caulfield, a young man who struggles with alienation and identity in the aftermath of being expelled from prep school.",
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "publication_year": 1960,
            "genres": ["Fiction", "Southern Gothic"],
            "rating": 4.4,
            "summary": "Set in the 1930s, it follows the journey of young Scout Finch, her brother Jem, and their father Atticus, a lawyer, as they navigate issues of race and morality in their Alabama town.",
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "publication_year": 1949,
            "genres": ["Fiction", "Dystopian"],
            "rating": 4.6,
            "summary": "A dystopian novel set in a totalitarian regime where individualism and independent thinking are suppressed by the government led by 'Big Brother.'",
        },
    ]


@pytest.fixture(name="expected_result_tuple")
def fixture_expected_result_tuple() -> list[tuple]:
    """Set expected result

    Returns:
        tuple: expected result
    """

    return [
        ("The Catcher in the Rye", "J.D. Salinger"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("1984", "George Orwell"),
    ]


def test_dict2json(test_file_paths: dict, expected_result_dict: dict):
    """Test json.dict2json standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_dict (dict): expected result
    """

    dict2json(test_file_paths["05"], expected_result_dict)

    result = {}
    with open(test_file_paths["05"], "r", encoding="utf8") as f:
        result = json.load(f)
    os.remove(test_file_paths["05"])
    assert result == expected_result_dict


def test_list2json(test_file_paths: dict, expected_result_list: list):
    """Test json.list2json standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_dict (dict): expected result
    """

    list2json(test_file_paths["06"], expected_result_list)

    result = []
    with open(test_file_paths["06"], "r", encoding="utf8") as f:
        result = json.load(f)
    os.remove(test_file_paths["06"])
    assert result == expected_result_list


def test_list2jsonl(test_file_paths: dict, expected_result_list: list):
    """Test json.list2jsonl standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_dict (dict): expected result
    """

    list2jsonl(test_file_paths["07"], expected_result_list)

    result = []
    with open(test_file_paths["07"], "r", encoding="utf8") as f:
        for line in f:
            result.append(json.loads(line))
    os.remove(test_file_paths["07"])
    assert result == expected_result_list


def test_json2dict(test_file_paths: dict, expected_result_dict: dict):
    """Test json.json2dict standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_dict (dict): expected result
    """

    result = json2dict(test_file_paths["01"])
    assert result == expected_result_dict


def test_json2list(test_file_paths: dict, expected_result_list: list):
    """Test json.json2list standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_list (list): expected result
    """

    result = json2list(test_file_paths["02"])
    assert result == expected_result_list


def test_jsonl2list(test_file_paths: dict, expected_result_list: list):
    """Test json.json2list standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_list (list): expected result
    """

    result = jsonl2list(test_file_paths["04"])
    assert result == expected_result_list


def test_json2listtuple(test_file_paths: dict, expected_result_tuple: list):
    """Test json.json2listtuple standard config

    Args:
        test_file_paths (dict): test file paths
        expected_result_tuple (list): expected result
    """

    result = json2listtuple(test_file_paths["03"])
    assert result == expected_result_tuple
