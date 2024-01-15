import pytest
import bisect


def test_ok_1():
    my_list = [2, 3, 1]
    sorted(my_list)
    bisect.bisect_right(my_list, 1)


def test_violation_1():
    my_list = [2, 3, 1]
    sorted(my_list)
    bisect.bisect_right(my_list, 1)
    bisect.bisect_right(my_list, 1)
