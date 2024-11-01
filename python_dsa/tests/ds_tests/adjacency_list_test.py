from pytest import fixture, mark, raises

from python_dsa.data_struct.graph import AdjacencyList, GraphEdge


@fixture
def empty_dal() -> AdjacencyList:
    return AdjacencyList(0, [])


@fixture
def one_node() -> AdjacencyList:
    return AdjacencyList(1, [])


@fixture
def simple_dal() -> AdjacencyList:
    edges: list[GraphEdge] = []
    edges.append(GraphEdge(0, 1))
    edges.append(GraphEdge(1, 2))
    return AdjacencyList(3, edges)


@fixture
def complex_dal() -> AdjacencyList:
    return AdjacencyList(1, [])


class TestAdjacencyLists:
    def test_empty_init(self):
        dal = AdjacencyList(0, [])
        assert dal.get_number_of_nodes() == 0
        assert dal.get_number_of_edges() == 0
        assert str(dal) == ""

    def test_one_node_init(self):
        dal = AdjacencyList(1, [])
        assert dal.get_number_of_nodes() == 1
        assert dal.get_number_of_edges() == 0
        assert str(dal) == "0: []"

    def test_graph_init(self):
        edges: list[GraphEdge] = []
        edges.append(GraphEdge(0, 1))
        edges.append(GraphEdge(1, 2))
        dal = AdjacencyList(3, edges)
        assert dal.get_number_of_nodes() == 3
        assert dal.get_number_of_edges() == 2
        assert str(dal) == "0: [(1, 1)]\n1: [(2, 1)]\n2: []"
