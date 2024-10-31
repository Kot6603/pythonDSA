from pytest import fixture

from python_dsa.data_struct.linked_list import LinkedList


@fixture
def empty_int_linked_list() -> LinkedList[int]:
    return LinkedList[int]()


@fixture
def int3_linked_list() -> LinkedList[int]:
    return LinkedList[int]([1, 2, 3])


class TestIntLinkedList:
    def test_basic_init(self):
        ll = LinkedList[int]()
        assert ll.is_empty()
        assert ll.size() == 0
        assert ll.head is None
        assert str(ll) == "Linked List[0]: (empty)"

    def test_list_init(self):
        ll = LinkedList[int]([1, 2, 3])
        assert not ll.is_empty()
        assert ll.size() == 3
        assert ll.head is not None
        assert ll.head.data == 1
        assert str(ll) == "Linked List[3]: 1 -> 2 -> 3"

    def test_append_empty(self, empty_int_linked_list):
        empty_int_linked_list.append(1)
        assert empty_int_linked_list.size() == 1
        assert str(empty_int_linked_list) == "Linked List[1]: 1"

    def test_append_non_empty(self, int3_linked_list):
        int3_linked_list.append(4)
        assert int3_linked_list.size() == 4
        assert str(int3_linked_list) == "Linked List[4]: 1 -> 2 -> 3 -> 4"

    def test_remove_empty(self, empty_int_linked_list):
        result = empty_int_linked_list.remove()
        assert not result
        assert empty_int_linked_list.size() == 0
        assert str(empty_int_linked_list) == "Linked List[0]: (empty)"

    def test_remove_no_args(self, int3_linked_list):
        result = int3_linked_list.remove()
        assert result
        assert int3_linked_list.size() == 2
        assert str(int3_linked_list) == "Linked List[2]: 2 -> 3"

    def test_remove_found(self, int3_linked_list):
        result = int3_linked_list.remove(2)
        assert result
        assert int3_linked_list.size() == 2
        assert str(int3_linked_list) == "Linked List[2]: 1 -> 3"

    def test_remove_not_found(self, int3_linked_list):
        result = int3_linked_list.remove(4)
        assert not result
        assert int3_linked_list.size() == 3
        assert str(int3_linked_list) == "Linked List[3]: 1 -> 2 -> 3"

    def test_get_element_empty(self, empty_int_linked_list):
        with raises(IndexError) as idxError:
            _ = empty_int_linked_list.get_node(4)
        assert str(idxError.value) == "index out of range"

    def test_get_element_no_args(self, int3_linked_list):
        node = int3_linked_list.get_node()
        assert node.data == 1
        assert int3_linked_list.size() == 3
        assert str(int3_linked_list) == "Linked List[3]: 1 -> 2 -> 3"

    def test_get_element_non_empty(self, int3_linked_list):
        node = int3_linked_list.get_node(2)
        assert node.data == 3
        assert int3_linked_list.size() == 3
        assert str(int3_linked_list) == "Linked List[3]: 1 -> 2 -> 3"

    def test_get_element_out_of_range(self, int3_linked_list):
        with raises(IndexError) as idxError:
            _ = int3_linked_list.get_node(4)
        assert str(idxError.value) == "index out of range"
