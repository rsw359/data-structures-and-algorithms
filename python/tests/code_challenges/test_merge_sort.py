from code_challenges.merge_sort import merge_sort
import pytest


def test_merge_sort_exists():
    assert merge_sort


def test_short_list():
    test_list = [3, 6, 4, 8]
    actual = merge_sort(test_list)
    expected = [3, 4, 6, 8]
    assert actual == expected


def test_long_sort():
    test_list = [4, 6, 13, 44, 2, 34, 365, 45, 34, 5, 23, 4, 23, 2]
    actual = merge_sort(test_list)
    expected = [2, 2, 4, 4, 5, 6, 13, 23, 23, 34, 34, 44, 45, 365]
    assert actual == expected


def test_negative_nums():
    test_list = [-2, 5, 6, -6, 0, 4]
    actual = merge_sort(test_list)
    expected = [-6, -2, 0, 4, 5, 6]
    assert actual == expected


def test_float():
    test_list = [.34, .63, .36, .82]
    actual = merge_sort(test_list)
    expected = [.34, .36, .63, .82]
    assert actual == expected


def test_odd_length():
    test_list = [5, 5, 14, 55, 4]
    actual = merge_sort(test_list)
    expected = [4, 5, 5, 14, 55]
    assert actual == expected


