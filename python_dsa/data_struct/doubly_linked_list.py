from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class DoublyLinkedListNode(Generic[T]):
    def __init__(
        self,
        data: T,
        next: DoublyLinkedListNode[T] | None = None,
        prev: DoublyLinkedListNode[T] | None = None,
    ):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(Generic[T]):
    def __init__(self, data: list[T] | DoublyLinkedListNode[T] | None = None):
        self._head: DoublyLinkedListNode[T] | None
        self._tail: DoublyLinkedListNode[T] | None
        self._length: int
        if data is None:
            self._head = None
            self._tail = None
            self._length = 0
        elif type(data) is DoublyLinkedListNode:
            self._head = data
            current = data
            size = 1
            while current.next is not None:
                size += 1
                current = current.next
            self._tail = current
            self._length = size
        else:
            assert type(data) is list, "must be a list if not node or None"
            new_node = DoublyLinkedListNode(data[0])
            self._head = new_node
            self._tail = new_node
            self._length = 1
            for i in range(1, len(data)):
                self.append(data[i])

    def is_empty(self) -> bool:
        return self._length == 0

    def size(self) -> int:
        return self._length

    def append(self, item: T) -> None:
        new_node = DoublyLinkedListNode(item, None, self._tail)
        if self.is_empty():
            self._head = new_node
        else:
            assert self._tail is not None, "tail None when list not empty"
            self._tail.next = new_node
        self._tail = new_node
        self._length += 1

    def insert(self, index: int, item: T) -> None:
        raise NotImplementedError("Not implemented yet")

    def index(self, item: T) -> int:
        raise NotImplementedError("Not implemented yet")

    def remove(self, item: T) -> bool:
        current = self._head
        while current is not None:
            if current.data == item:
                if current == self._head:
                    self._head = current.next
                    if current.next is not None:
                        current.next.prev = None
                else:
                    assert current.prev is not None, "corrupt node"
                    current.prev.next = current.next
                self._length -= 1
                return True
            current = current.next

        return False

    def get_node(self, index: int = 0) -> DoublyLinkedListNode[T] | None:
        if index < -self._length or index >= self._length:
            raise IndexError("index out of range")

        if index < 0:
            curr_idx = self._length - 1
            # idx = ridx - length
            # ridx = idx + length
            current = self._tail
            while current is not None:
                if curr_idx - self._length == index:
                    return current
                current = current.prev
                curr_idx -= 1
        else:
            curr_idx = 0
            current = self._head
            while current is not None:
                if curr_idx == index:
                    return current
                current = current.next
                curr_idx += 1

        return None

    def __str__(self) -> str:
        if self.is_empty():
            return "DoublyLinkedList[0]: (empty)"

        array: list[str] = []
        current = self._head
        while current is not None:
            array.append(str(current.data))
            current = current.next

        return f'DoublyLinkedList[{self._length}]: {" <-> ".join(array)}'
