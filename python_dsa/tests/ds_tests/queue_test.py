from pytest import fixture

from python_dsa.data_struct.queue import Queue


@fixture
def empty_queue() -> Queue[int]:
    return Queue[int]()


@fixture
def three_element_queue() -> Queue[int]:
    return Queue[int]([1, 2, 3])


class TestIntQueue:
    def test_basic_init(self):
        q = Queue[int]()
        assert q.is_empty()
        assert q.size() == 0
        assert str(q) == "Queue[0]: <-  <-"

    def test_list_init(self):
        q = Queue[int]([1, 2, 3])
        assert not q.is_empty()
        assert q.size() == 3
        assert str(q) == "Queue[3]: <- 1, 2, 3 <-"

    def test_push_empty(self, empty_queue):
        empty_queue.push(1)
        assert not empty_queue.is_empty()
        assert empty_queue.size() == 1
        assert str(empty_queue) == "Queue[1]: <- 1 <-"

    def test_push_non_empty(self, three_element_queue):
        three_element_queue.push(4)
        assert not three_element_queue.is_empty()
        assert three_element_queue.size() == 4
        assert str(three_element_queue) == "Queue[4]: <- 1, 2, 3, 4 <-"

    def test_pop_empty(self, empty_queue):
        assert empty_queue.pop() is None
        assert empty_queue.is_empty()
        assert empty_queue.size() == 0
        assert str(empty_queue) == "Queue[0]: <-  <-"

    def test_pop_non_empty(self, three_element_queue):
        assert three_element_queue.pop() == 1
        assert not three_element_queue.is_empty()
        assert three_element_queue.size() == 2
        assert str(three_element_queue) == "Queue[2]: <- 2, 3 <-"

    def test_peek_empty(self, empty_queue):
        assert empty_queue.peek() is None
        assert empty_queue.is_empty()
        assert empty_queue.size() == 0
        assert str(empty_queue) == "Queue[0]: <-  <-"

    def test_peek_non_empty(self, three_element_queue):
        assert three_element_queue.peek() == 1
        assert not three_element_queue.is_empty()
        assert three_element_queue.size() == 3
        assert str(three_element_queue) == "Queue[3]: <- 1, 2, 3 <-"

    def test_clear_empty(self, empty_queue):
        empty_queue.clear()
        assert empty_queue.is_empty()
        assert empty_queue.size() == 0
        assert str(empty_queue) == "Queue[0]: <-  <-"

    def test_clear_non_empty(self, three_element_queue):
        three_element_queue.clear()
        assert three_element_queue.is_empty()
        assert three_element_queue.size() == 0
        assert str(three_element_queue) == "Queue[0]: <-  <-"
