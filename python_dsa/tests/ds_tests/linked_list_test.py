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

    def test_pop_empty(self):
        pass

    def test_pop_non_empty(self):
        pass

    def test_remove_empty(self):
        pass

    def test_remove_non_empty(self):
        pass

    def test_remove_out_of_range(self):
        pass

    def test_get_element_empty(self):
        pass

    def test_get_element_non_empty(self):
        pass

    def test_get_element_out_of_range(self):
        pass
