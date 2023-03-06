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
"""