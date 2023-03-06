"""
BFS USAGE:
    *Checks if there's a path from A to B
    *Finds you the shortest path from A to B (unweighted edges)

"""
from collections import deque


def person_is_seller(name):
    return name == 'you'
    # return name[-1] == 'm'


# O(V+E) (V for number of vertices (number of persons added to the queue),
#       E for number of edges (connection of people))
def bfs(graph, root):
    search_queue = deque()
    search_queue += graph[root]
    searched = []
    num_of_searched = 0
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                print('serached %s', num_of_searched)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
        num_of_searched += 1
    return False


def test_bfs():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    found = bfs(graph, "you")
    print('found: ', found)