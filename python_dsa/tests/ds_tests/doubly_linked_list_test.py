from pytest import fixture, mark

from python_dsa.data_struct.doubly_linked_list import (
    DoublyLinkedList,
    DoublyLinkedListNode,
)


@fixture
def empty_int_dll() -> DoublyLinkedList[int]:
    return DoublyLinkedList[int]()


@fixture
def int3_dll() -> DoublyLinkedList[int]:
    return DoublyLinkedList[int]([1, 2, 3])


class TestIntDoublyLinkedList:
    def test_basic_init(self):
        dll = DoublyLinkedList[int]()
        assert dll.is_empty()
        assert dll.size() == 0
        assert str(dll) == "DoublyLinkedList[0]: (empty)"

    def test_list_init(self):
        dll = DoublyLinkedList[int]([1, 2, 3])
        assert not dll.is_empty()
        assert dll.size() == 3
        assert str(dll) == "DoublyLinkedList[3]: 1 <-> 2 <-> 3"

    def test_node_init(self):
        node1 = DoublyLinkedListNode[int](1)
        node2 = DoublyLinkedListNode[int](2)
        node3 = DoublyLinkedListNode[int](3)
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2

        dll = DoublyLinkedList[int](node1)
        assert not dll.is_empty()
        assert dll.size() == 3
        assert str(dll) == "DoublyLinkedList[3]: 1 <-> 2 <-> 3"

    def test_append_empty(self, empty_int_dll):
        empty_int_dll.append(1)
        assert empty_int_dll.size() == 1
        assert str(empty_int_dll) == "DoublyLinkedList[1]: 1"

    def test_append_non_empty(self, int3_dll):
        int3_dll.append(4)
        assert int3_dll.size() == 4
        assert str(int3_dll) == "DoublyLinkedList[4]: 1 <-> 2 <-> 3 <-> 4"
