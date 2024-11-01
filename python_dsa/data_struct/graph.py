class GraphEdge:
    def __init__(self, from_node: int, to_node: int, weight: float = 1):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight


class AdjacencyList:
    def __init__(self, num_nodes: int, edges: list[GraphEdge], directed: bool = True):
        self._directed: bool = directed
        self._list: list[list[tuple[int, float]]] = []
        for _ in range(num_nodes):
            self._list.append([])
        for edge in edges:
            self._list[edge.from_node].append((edge.to_node, edge.weight))
            if (
                not self._directed
                and (edge.from_node, edge.weight) not in self._list[edge.to_node]
            ):
                self._list[edge.to_node].append((edge.from_node, edge.weight))

    def get_number_of_nodes(self) -> int:
        return len(self._list)

    def get_number_of_edges(self) -> int:
        total: int = 0
        for node in self._list:
            for _ in node:
                total += len(node)

        return total

    def add_edge(self, edge: GraphEdge) -> None:
        raise NotImplementedError

    def get_neighbors(self, node: int) -> list[int]:
        raise NotImplementedError

    def get_indegree(self, node: int) -> int:
        raise NotImplementedError

    def remove_edge(self, from_node: int, to_node: int) -> None:
        raise NotImplementedError

    def remove_node(self, node: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        output: str = ""
        for node in range(len(self._list)):
            output += f"{node}: {self._list[node]}\n"

        return output.strip()
