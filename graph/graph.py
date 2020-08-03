import abc


class Graph(abc.ABC):
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes

    @abc.abstractmethod
    def add_node(self, v1, v2):
        pass

    @abc.abstractmethod
    def get_adj_nodes(self, v1):
        pass

    @abc.abstractmethod
    def show(self):
        pass


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.adj_nodes = []

    def add_node(self, v2):
        self.adj_nodes.append(Node(node_id=v2))

    def get_adj_nodes(self):
        return self.adj_nodes

    def show(self):
        for i in self.adj_nodes:
            print(f'{self.node_id} -> {i.node_id}')

    def __eq__(self, other):
        return self.node_id == other.node_id and self.adj_nodes == other.adj_nodes

    def __repr__(self):
        return f'{self.__class__.__name__}(node_id={self.node_id})'


class AdjSetGraph(Graph):
    def __init__(self, num_nodes):
        super().__init__(num_nodes=num_nodes)
        self.nodes = []
        for i in range(num_nodes):
            self.nodes.append(Node(node_id=i))

    def add_node(self, v1, v2):
        self.nodes[v1].add_node(v2)

    def get_adj_nodes(self, v1):
        return self.nodes[v1].get_adj_nodes()

    def show(self):
        for i in self.nodes:
            i.show()


if __name__ == '__main__':
    g = AdjSetGraph(num_nodes=4)
    g.add_node(0, 1)
    g.add_node(0, 2)
    g.add_node(2, 3)
    g.show()
