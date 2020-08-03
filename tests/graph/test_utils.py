from graph.utils import get_nodes_breadth_first, get_nodes_depth_first


def test_get_nodes_breadth_first(adj_set_graph):
    g = adj_set_graph
    assert get_nodes_breadth_first(g, 0) == [0, 1, 2, 4, 3]


def test_get_nodes_depth_first(adj_set_graph):
    g = adj_set_graph
    assert get_nodes_depth_first(g, 0) == [0, 1, 4, 2, 3]
