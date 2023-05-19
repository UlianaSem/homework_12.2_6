import pytest
from utils import arrs


@pytest.fixture
def list_for_tests():
    return [1, 2, 3]


def test_get(list_for_tests):
    assert arrs.get(list_for_tests, 1, "test") == 2
    assert arrs.get(list_for_tests, -3, 'test') == 'test'
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice(list_for_tests):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(list_for_tests, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([0, 1], -4) == [0, 1]
    assert arrs.my_slice(list_for_tests, -2, 2) == [2]