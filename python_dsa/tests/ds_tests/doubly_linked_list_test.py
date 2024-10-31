from pytest import fixture, mark, raises

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


@fixture
def int5_dll() -> DoublyLinkedList[int]:
    return DoublyLinkedList[int]([1, 2, 3, 4, 5])


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

    def test_remove_empty(self, empty_int_dll):
        result = empty_int_dll.remove(0)
        assert not result
        assert empty_int_dll.size() == 0
        assert str(empty_int_dll) == "DoublyLinkedList[0]: (empty)"

    def test_remove_found0(self, int5_dll):
        result = int5_dll.remove(1)
        assert result
        assert int5_dll.size() == 4
        assert str(int5_dll) == "DoublyLinkedList[4]: 2 <-> 3 <-> 4 <-> 5"

    def test_remove_found1(self, int5_dll):
        result = int5_dll.remove(2)
        assert result
        assert int5_dll.size() == 4
        assert str(int5_dll) == "DoublyLinkedList[4]: 1 <-> 3 <-> 4 <-> 5"

    def test_remove_found2(self, int5_dll):
        result = int5_dll.remove(3)
        assert result
        assert int5_dll.size() == 4
        assert str(int5_dll) == "DoublyLinkedList[4]: 1 <-> 2 <-> 4 <-> 5"

    def test_remove_found3(self, int5_dll):
        result = int5_dll.remove(4)
        assert result
        assert int5_dll.size() == 4
        assert str(int5_dll) == "DoublyLinkedList[4]: 1 <-> 2 <-> 3 <-> 5"

    def test_remove_found4(self, int5_dll):
        result = int5_dll.remove(5)
        assert result
        assert int5_dll.size() == 4
        assert str(int5_dll) == "DoublyLinkedList[4]: 1 <-> 2 <-> 3 <-> 4"

    def test_remove_not_found(self, int3_dll):
        result = int3_dll.remove(4)
        assert not result
        assert int3_dll.size() == 3
        assert str(int3_dll) == "DoublyLinkedList[3]: 1 <-> 2 <-> 3"

    def test_get_element_empty(self, empty_int_dll):
        with raises(IndexError) as idxError:
            _ = empty_int_dll.get_node(4)
        assert str(idxError.value) == "index out of range"

    def test_get_element_no_args(self, int3_dll):
        node = int3_dll.get_node()
        assert node.data == 1
        assert int3_dll.size() == 3
        assert str(int3_dll) == "DoublyLinkedList[3]: 1 <-> 2 <-> 3"

    def test_get_element_non_empty_pos(self, int5_dll):
        node = int5_dll.get_node(1)
        assert node.data == 2
        assert int5_dll.size() == 5
        assert str(int5_dll) == "DoublyLinkedList[5]: 1 <-> 2 <-> 3 <-> 4 <-> 5"

    def test_get_element_non_empty_neg1(self, int5_dll):
        node = int5_dll.get_node(-1)
        assert node.data == 5
        assert int5_dll.size() == 5
        assert str(int5_dll) == "DoublyLinkedList[5]: 1 <-> 2 <-> 3 <-> 4 <-> 5"

    def test_get_element_non_empty_neg2(self, int5_dll):
        node = int5_dll.get_node(-5)
        assert node.data == 1
        assert int5_dll.size() == 5
        assert str(int5_dll) == "DoublyLinkedList[5]: 1 <-> 2 <-> 3 <-> 4 <-> 5"

    def test_get_element_out_of_range_pos(self, int3_dll):
        with raises(IndexError) as idxError:
            _ = int3_dll.get_node(4)
        assert str(idxError.value) == "index out of range"

    def test_get_element_out_of_range_neg(self, int3_dll):
        with raises(IndexError) as idxError:
            _ = int3_dll.get_node(-4)
        assert str(idxError.value) == "index out of range"
