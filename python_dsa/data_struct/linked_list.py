from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    def __init__(self, data: T, next: LinkedListNode[T] | None = None):
        self.data: T = data
        self.next: LinkedListNode[T] | None = next


class LinkedList(Generic[T]):
    def __init__(self, array: list[T] | None = None):
        self.head: LinkedListNode[T] | None
        self._length: int
        if array is None:
            self.head = None
            self._length = 0
        else:
            self.head = LinkedListNode(array[0])
            self._length = 1
            for i in range(1, len(array)):
                self.append(array[i])

    def is_empty(self) -> bool:
        return self._length == 0

    def size(self) -> int:
        return self._length

    def append(self, item: T) -> None:
        new_node: LinkedListNode[T] = LinkedListNode[T](item)

        if self.head is None:
            self.head = new_node
            self._length += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self._length += 1

    def __str__(self) -> str:
        if self.is_empty():
            return "Linked List[0]: (empty)"

        array: list[str] = []
        current = self.head
        while current is not None:
            array.append(str(current.data))
            current = current.next

        return f'Linked List[{self._length}]: {" -> ".join(array)}'


# pop
# remove
# insert
# size
