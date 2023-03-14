"""
Usage:
    *find the shortest path for weighted edges (the smallest total weight)

Steps:
    1-Find the cheapest node.
    2-Update the path to neighbors with a cheaper cost (if possible)
    3-Repeat until you've done this for every node in the graph.
    4-Calculate the final path.

Notes:
    *Dijkstra’s algorithm only works with directed acyclic graphs, called DAGs for short.
    *You can't Dijkstra's algorithm with negative-weight edges.
    *Bellman-Ford algorithm finds the shortest-path in a graph that has negative-weight edges.
"""


def run_dijkstra(graph, start_node, end_node):
    nodes_list = {}
    for key in graph.keys():
        nodes_list[key] = {'cost': 99999, 'parent': '', 'visited': False}
    nodes_list[start_node]['cost'] = 0
    ch_node = start_node

    #TODO: make sure we check all nodes, and that this condition is correct
    while ch_node != -1:
        # Update neighbours
        for node in graph[ch_node]:
            nodes_list[node]['cost'] = graph[ch_node][node]
            nodes_list[node]['parent'] = ch_node
        nodes_list[ch_node]['visited'] = True

        # Find cheapest node.
        ch_node = -1
        cheapest = 99999
        for key in nodes_list.keys():
            node = nodes_list[key]
            if not node['visited'] and node['cost'] <= cheapest:
                ch_node = key
                cheapest = node['cost']

    # Get the path
    node = end_node
    path = [end_node]
    while node != start_node:
        node = nodes_list[node]['parent']
        path.append(node)

    path.reverse()
    return path

def test_dijkstra():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}

    path = run_dijkstra(graph, "start", "fin")

    print("Path: ", path)