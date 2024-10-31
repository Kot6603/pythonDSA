from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self, items: list[T] | None = None) -> None:
        if items is None:
            items = []
        self.items: list[T] = items

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T | None:
        if self.is_empty():
            return
        return self.items.pop(0)

    def peek(self) -> T | None:
        if self.is_empty():
            return
        return self.items[0]

    def size(self) -> int:
        return len(self.items)

    def clear(self) -> None:
        self.items = []

    def to_list(self) -> list[T]:
        return self.items

    def __str__(self) -> str:
        return f"Queue[{self.size()}]: <- {str(self.items)[1:-1]} <-"
