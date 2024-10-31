from pytest import fixture

from python_dsa.data_struct.stack import Stack


@fixture
def empty_int_stack() -> Stack[int]:
    return Stack[int]()


@fixture
def int3_stack() -> Stack[int]:
    return Stack[int]([1, 2, 3])


class TestIntStack:
    def test_basic_init(self):
        s = Stack[int]()
        assert s.is_empty()
        assert s.size() == 0
        assert str(s) == "Stack[0]: [ <-"

    def test_list_init(self):
        s = Stack[int]([1, 2, 3])
        assert not s.is_empty()
        assert s.size() == 3
        assert str(s) == "Stack[3]: [1, 2, 3 <-"

    def test_push_empty(self, empty_int_stack):
        empty_int_stack.push(1)
        assert empty_int_stack.size() == 1
        assert str(empty_int_stack) == "Stack[1]: [1 <-"

    def test_push_non_empty(self, int3_stack):
        int3_stack.push(4)
        assert int3_stack.size() == 4
        assert str(int3_stack) == "Stack[4]: [1, 2, 3, 4 <-"

    def test_pop_empty(self, empty_int_stack):
        assert empty_int_stack.pop() is None
        assert empty_int_stack.size() == 0
        assert str(empty_int_stack) == "Stack[0]: [ <-"

    def test_pop_non_empty(self, int3_stack):
        assert int3_stack.pop() == 3
        assert int3_stack.size() == 2
        assert str(int3_stack) == "Stack[2]: [1, 2 <-"

    def test_peek_empty(self, empty_int_stack):
        assert empty_int_stack.peek() is None
        assert empty_int_stack.size() == 0
        assert str(empty_int_stack) == "Stack[0]: [ <-"

    def test_peek_non_empty(self, int3_stack):
        assert int3_stack.peek() == 3
        assert int3_stack.size() == 3
        assert str(int3_stack) == "Stack[3]: [1, 2, 3 <-"

    def test_clear_empty(self, empty_int_stack):
        empty_int_stack.clear()
        assert empty_int_stack.size() == 0
        assert str(empty_int_stack) == "Stack[0]: [ <-"

    def test_clear_non_empty(self, int3_stack):
        int3_stack.clear()
        assert int3_stack.size() == 0
        assert str(int3_stack) == "Stack[0]: [ <-"
