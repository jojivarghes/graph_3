from graph import Node, AdjSetGraph


class TestAdjSetGraph:
    def test_add_node(self, capsys):
        g = AdjSetGraph(num_nodes=2)
        g.add_node(0, 1)
        g.show()
        captured = capsys.readouterr()
        assert captured.out == '0 -> 1\n'

    def test_get_adj_nodes(self, adj_set_graph):
        g = adj_set_graph
        assert g.get_adj_nodes(0) == [Node(node_id=1), Node(node_id=2)]

    def test_show(self, capsys, adj_set_graph):
        adj_set_graph.show()
        captured = capsys.readouterr()
        assert captured.out == '0 -> 1\n0 -> 2\n1 -> 4\n2 -> 3\n'
