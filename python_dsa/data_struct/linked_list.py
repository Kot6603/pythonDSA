from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    def __init__(self, data: T, next: LinkedListNode[T] | None = None):
        self.data: T = data
        self.next: LinkedListNode[T] | None = next


class LinkedList(Generic[T]):
    def __init__(self, head: list[T] | LinkedListNode[T] | None = None):
        self.head: LinkedListNode[T] | None
        self._length: int
        if head is None:
            self.head = None
            self._length = 0
        elif type(head) is LinkedListNode:
            self.head = head
            current = head
            size: int = 0
            while current is not None:
                size += 1
                current = current.next
            self._length = size
        else:
            assert type(head) is list
            self.head = LinkedListNode(head[0])
            self._length = 1
            for i in range(1, len(head)):
                self.append(head[i])

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

    def remove(self, item: T | None = None) -> bool:
        """Removes the item from the list.

        no arguments  -> Remove first item
        returns true or false based on found or not
        """
        if self.head is None:
            return False

        if item is None:
            self.head = self.head.next
            self._length -= 1
            return True

        current = self.head
        prev = self.head
        while current is not None:
            if current.data == item:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self._length -= 1
                return True

            prev = current
            current = current.next

        return False

    def get_node(self, index: int = 0) -> LinkedListNode[T] | None:
        if index < 0 or index >= self._length:
            raise IndexError("index out of range")

        curr_idx = 0
        current = self.head
        while current is not None:
            if curr_idx == index:
                return current
            current = current.next
            curr_idx += 1

        return None

    def __str__(self) -> str:
        if self.is_empty():
            return "Linked List[0]: (empty)"

        array: list[str] = []
        current = self.head
        while current is not None:
            array.append(str(current.data))
            current = current.next

        return f'Linked List[{self._length}]: {" -> ".join(array)}'


# insert
# size
