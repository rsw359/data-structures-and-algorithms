from code_challenges.merge_sort import merge_sort
import pytest


def test_merge_sort_exists():
    assert merge_sort


def test_short_list():
    test_list = [5, 6, 4, 7]
    actual = merge_sort(test_list)
    expected = [4, 5, 6, 7]
    assert actual == expected


def test_long_sort():
    test_list = [4, 6, 13, 44, 2, 34, 265, 45, 34, 5, 234, 23, 4, 23, 2]
    actual = merge_sort(test_list)
    expected = [2, 2, 4, 4, 5, 6, 13, 23, 23, 34, 34, 44, 45, 234, 265]
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
    test_list = [5, 5, 12, 123, 4]
    actual = merge_sort(test_list)
    expected = [4, 5, 5, 12, 123]
    assert actual == expected


