from queue import Queue
import string
from collections import defaultdict
import sys


inputs = [x.strip() for x in open("input.txt").readlines()]
graph = defaultdict(list)
points = {}
start, starts, end = None, [], None
for x in range(len(inputs)):
    for y in range(len(inputs[x])):
        point = complex(x, y)
        value = 0
        if inputs[x][y] == "S":
            start = point
            value = 0
            starts.append(point)
        elif inputs[x][y] == "a":
            value = 0
            starts.append(point)
        elif inputs[x][y] == "E":
            end = point
            value = 25
        else:
            value = string.ascii_lowercase.index(inputs[x][y])
        points[point] = value

for point in points:
    for neighbor in [1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j]:
        if (point + neighbor) in points:
            graph[point].append(point+neighbor)


def dijkstra(graph, source):
    Q = list(graph.keys())
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)

        for v in graph[u]:
            alt = dist[u] + 1
            if alt < dist[v] and points[u] - points[v] <= 1:
                dist[v] = alt
    return dist


paths = dijkstra(graph, end)
print(paths[start])  # Part 1
print(min(paths[s] for s in starts))  # Part 2
