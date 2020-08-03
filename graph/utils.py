import graph
from queue import Queue


def get_nodes_breadth_first(gph: graph.AdjSetGraph, vertex):
    q = Queue()
    node_list = []
    root = gph.nodes[vertex]
    q.put(root)
    while not q.empty():
        node = q.get()
        node_list.append(node.node_id)
        for i in gph.get_adj_nodes(node.node_id):
            q.put(i)
    return node_list


def get_nodes_depth_first(gph: graph.AdjSetGraph, vertex):
    node_list = []
    root = gph.nodes[vertex]

    def get_adj_nodes(node):
        node_list.append(node.node_id)
        for i in gph.get_adj_nodes(node.node_id):
            get_adj_nodes(i)

    get_adj_nodes(root)
    return node_list
