from collections import defaultdict
from collections import deque
class Graph_bfs:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def bfs(self, start, goals):
        visited = set()
        queue =deque([(start, [] )])
        while queue:
            node, path = queue.popleft()
            print(path)
            if node not in visited:
                visited.add(node)
            if node in goals:
                return path + [node], node
            for neighbor in self.graph.get(node,[]):
                if neighbor not in visited:
                    queue.append((neighbor,path + [node]))


        return [], None

    def print_path(path, goal):
        print('->'.join(path + [goal]))



g = Graph_bfs(directed=False)

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


print(g.bfs(start, goal))


