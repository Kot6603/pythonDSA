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


def insertion_sort(original: list[int]) -> list[int]:
    """Insertion Sort

    Basic idea:
    - iterate over
    - sorted | unsorted
    - if before is bigger, swap
    """
    array = original.copy()
    n = len(array)

    for i in range(1, n):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1

    return array


def selection_sort(original: list[int]) -> list[int]:
    """Selection Sort

    Basic idea:
    - choose the maximum element if umsorted list
    - swap it with the last element of the unsorted list

    - unsorted | sorted
    """
    array = original.copy()
    n = len(array)

    for i in range(n - 1, -1, -1):
        largest = array[0]
        index = 0
        for j in range(1, i + 1):
            if array[j] > largest:
                largest = array[j]
                index = j
        array[index], array[i] = array[i], array[index]

    return array
