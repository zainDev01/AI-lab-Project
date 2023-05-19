from collections import defaultdict
import heapq

class Graph_ucs:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def ucs(self, start, goal):
        visited = set()
        heap = [(0, start, [])]
        while heap:
            cost, node, path = heapq.heappop(heap)
            print(path)
            if node not in visited:
                visited.add(node)
            if node == goal:
                return path , goal
            for neighbor, weight in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [node]))

        return [], None

    def print_path(path, goal):
        print('->'.join(path + [goal]))

g = Graph_ucs(directed=False)

g.add_edge('S', 'F', 99)
g.add_edge('S', 'R', 80)
g.add_edge('R', 'P', 97)
g.add_edge('P', 'B', 101)
g.add_edge('F', 'B', 211)

heuristics = {'S': 253, 'F': 176, 'R': 193, 'P': 100, 'B': 0}

start = 'S'
goal = 'B'
print(g.ucs(start, goal))
