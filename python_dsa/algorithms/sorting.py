"""
Sorting Algorithms :D
- should this mutate state? - prob not

These will return you new arrays :D
"""


def bubble_sort(original: list[int]) -> list[int]:
    """Bubble Sort

    Basic idea:
    - iterate over
    - swap if curr is greater than prev
    """
    array = original.copy()
    n = len(array)
    for _ in range(n - 1):
        for i in range(1, n):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]

    return array
