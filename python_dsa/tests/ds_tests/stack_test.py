from python_dsa.data_struct.stack import Stack


class TestIntStack:
    def test_basic_init(self):
        s = Stack[int]()
        assert str(s) == "[ <-"
        assert s.size() == 0
        assert s.is_empty()

    def test_list_init(self):
        s = Stack[int]([1, 2, 3])
        assert str(s) == "[1, 2, 3 <-"
        assert s.size() == 3
        assert not s.is_empty()

    def test_push_empty(self):
        s = Stack[int]()
        s.push(1)
        assert str(s) == "[1 <-"
        assert s.size() == 1
        assert not s.is_empty()

    def test_push_non_empty(self):
        s = Stack[int]([1, 2, 3])
        s.push(4)
        assert str(s) == "[1, 2, 3, 4 <-"
        assert s.size() == 4
        assert not s.is_empty()

    def test_pop_empty(self):
        s = Stack[int]()
        assert s.pop() is None
        assert str(s) == "[ <-"
        assert s.size() == 0
        assert s.is_empty()

    def test_pop_non_empty(self):
        s = Stack[int]([1, 2, 3])
        assert s.pop() == 3
        assert str(s) == "[1, 2 <-"
        assert s.size() == 2
        assert not s.is_empty()

    def test_peek_empty(self):
        s = Stack[int]()
        assert s.peek() is None
        assert str(s) == "[ <-"
        assert s.size() == 0
        assert s.is_empty()

    def test_peek_non_empty(self):
        s = Stack[int]([1, 2, 3])
        assert s.peek() == 3
        assert str(s) == "[1, 2, 3 <-"
        assert s.size() == 3
        assert not s.is_empty()

    def test_clear_empty(self):
        s = Stack[int]()
        s.clear()
        assert str(s) == "[ <-"
        assert s.size() == 0
        assert s.is_empty()

    def test_clear_non_empty(self):
        s = Stack[int]([1, 2, 3])
        s.clear()
        assert str(s) == "[ <-"
        assert s.size() == 0
        assert s.is_empty()
