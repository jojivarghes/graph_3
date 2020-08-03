import pytest

from graph import AdjSetGraph


@pytest.fixture
def adj_set_graph():
    g = AdjSetGraph(num_nodes=5)
    g.add_node(0, 1)
    g.add_node(0, 2)
    g.add_node(2, 3)
    g.add_node(1, 4)
    return g
