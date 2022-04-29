import pytest

from pythonisms import CustomCollection

def test_for_in_loop():

    custom_col = CustomCollection(10)
    actual = []
    for i in custom_col:
        actual.append(i)

    expected = [0,1,2,3,4,5,6,7,8,9]
    assert actual == expected


def test_list_comprehension():

    custom_col = CustomCollection(10)
    actual = [x for x in custom_col]
    expected = [0,1,2,3,4,5,6,7,8,9]
    assert actual == expected

def test_convert_to_list():
    custom_col = CustomCollection(10)
    actual = list(custom_col)
    expected = [0,1,2,3,4,5,6,7,8,9]
    assert actual == expected

def test_calculate_time_elapsed_with_decorator():
    custom_col = CustomCollection(10)
    time_to_one_thousand = custom_col.count_to_one_thousand()
    time_to_one_million = custom_col.count_to_one_million()
    assert time_to_one_million > time_to_one_thousand

def test_dunder_equals():
    custom_col1 = CustomCollection(10)
    custom_col2 = CustomCollection(10)
    assert custom_col1 == custom_col2

def test_dunder_bool():
    custom_col1 = CustomCollection(100)
    custom_col2 = CustomCollection(-1)

    #Test truthiness
    assert custom_col1
    assert not custom_col2


