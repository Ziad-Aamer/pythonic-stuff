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


def run_dijkstra_v1(graph, start_node, end_node):
    nodes_list = {}
    for key in graph.keys():
        nodes_list[key] = {'cost': 99999, 'parent': '', 'visited': False}
    nodes_list[start_node]['cost'] = 0
    ch_node = start_node

    #TODO: make sure we check all nodes, and that this condition is correct
    while ch_node != -1:

        # Update neighbours
        for node in graph[ch_node]:
            cost = nodes_list[ch_node]['cost'] + graph[ch_node][node]
            if cost < nodes_list[node]['cost']:
                nodes_list[node]['cost'] = cost
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

    print("Min cost: ", nodes_list[end_node]['cost'])
    # Get the path
    node = end_node
    path = [end_node]
    while node != start_node:
        node = nodes_list[node]['parent']
        path.append(node)

    path.reverse()
    return path


def get_path(start, end, parent):
    # Get the path
    node = end
    path = [end]
    while node != start:
        node = parent[node]
        path.append(node)

    path.reverse()
    return path


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if lowest_cost > cost and node not in processed:
            lowest_cost = cost
            lowest_node = node

    return lowest_node


def run_dijkstra_v2(graph, start, end):

    # 1- initialize
    costs = {}
    parents = {}
    processed = []

    for node in graph.keys():
        if node in graph[start]:
            costs[node] = graph[start][node]
            parents[node] = start
        else:
            costs[node] = float("inf")
            parents[node] = None

    # 2- start algo
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        for n_node in graph[node]:
            cost = costs[node] + graph[node][n_node]
            if cost < costs[n_node]:
                costs[n_node] = cost
                parents[n_node] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    print("Min cost: ", costs[end])
    return get_path(start, end, parents)

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

    path = run_dijkstra_v1(graph, "start", "fin")
    print("Path: ", path)

    path = run_dijkstra_v2(graph, "start", "fin")
    print("Path: ", path)

"""
Dividing the algorithm into functions will:
    1- Make it more readable
    2- avoid mistakes
    3- give you overview
    4- abstract, so it is easier to remember
"""

