from collections import defaultdict

class Graph_dfs:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def dfs(self, start, goal):
        stack = [start]
        visited = set()
        parent = {}
        while stack:
            node = stack.pop()
            if node == goal:
                path = []
                while node != start:
                    path.append(node)
                    node = parent[node]
                path.append(start)
                path.reverse()
                return path , goal

            if node not in visited:
                visited.add(node)
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        parent[neighbor] = node

        return [],  None

    def print_path(path, goal):
        print('->'.join(path + [goal]))

g = Graph_dfs(directed=False)

# g.add_edge('S', 'A'),
# g.add_edge('S', 'G'),
# g.add_edge('A', 'B'),
# g.add_edge('A', 'C'),
# g.add_edge('B', 'D'),
# g.add_edge('C', 'D'),
# g.add_edge('C', 'G'),
# g.add_edge('D', 'G')


g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('b', 'd')
g.add_edge('b', 'e')
g.add_edge('c', 'f')
g.add_edge('c', 'g')


start = 'a'
goal = 'f'
print(g.dfs(start, goal))
