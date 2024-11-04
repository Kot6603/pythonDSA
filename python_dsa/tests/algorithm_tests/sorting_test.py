from pytest import fixture, mark

from python_dsa.algorithms.sorting import bubble_sort, insertion_sort


@fixture
def empty_list() -> list[int]:
    return []


@fixture
def one_item() -> list[int]:
    return [1]


@fixture
def sorted_list() -> list[int]:
    return [1, 2, 3, 4, 5]


@fixture
def unsorted_list() -> list[int]:
    return [2, 5, 1, 3, 4]


class TestBubbleSort:
    def test_empty(self, empty_list):
        result = bubble_sort(empty_list)
        assert result == []

    def test_one(self, one_item):
        result = bubble_sort(one_item)
        assert result == [1]

    def test_sorted(self, sorted_list):
        result = bubble_sort(sorted_list)
        assert sorted_list == [1, 2, 3, 4, 5]
        assert result == [1, 2, 3, 4, 5]

    def test_unsorted(self, unsorted_list):
        result = bubble_sort(unsorted_list)
        assert unsorted_list == [2, 5, 1, 3, 4]
        assert result == [1, 2, 3, 4, 5]


class TestInsertionSort:
    def test_empty(self, empty_list):
        result = insertion_sort(empty_list)
        assert result == []

    def test_one(self, one_item):
        result = insertion_sort(one_item)
        assert result == [1]

    def test_sorted(self, sorted_list):
        result = insertion_sort(sorted_list)
        assert result == [1, 2, 3, 4, 5]

    def test_unsorted(self, unsorted_list):
        result = insertion_sort(unsorted_list)
        assert result == [1, 2, 3, 4, 5]
