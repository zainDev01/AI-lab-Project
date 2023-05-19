class Graph_idfs:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]

    @staticmethod
    def print_path(traced_path, goal):
        if traced_path:
            for node in traced_path:
                print(node, end=' ')
            print(goal)

    def iterative_deepening(self, start, goals, max_depth = 3):
        for depth in range(max_depth + 1):
            result, goal_node = self.depth_limited_search(start, goals, depth)
            if goal_node is not None:
                return result, goal_node

        return None, None

    def depth_limited_search(self, start, goals, max_depth):
        visited = set()
        stack = [(start, [], 0)]

        while stack:
            current_node, traced_path, current_depth = stack.pop()

            if current_node in goals:
                return traced_path, current_node

            visited.add(current_node)

            if current_depth < max_depth:
                if current_node in self.graph:
                    neighbors = self.graph[current_node]
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.append((neighbor, traced_path + [current_node], current_depth + 1))

        return None, None

    def bidirectional_search(self, start, goal):
        forward_visited = set()
        backward_visited = set()
        forward_stack = [(start, [], 0)]
        backward_stack = [(goal, [], 0)]

        while forward_stack and backward_stack:
            forward_current_node, forward_traced_path, forward_current_depth = forward_stack.pop()
            backward_current_node, backward_traced_path, backward_current_depth = backward_stack.pop()

            if forward_current_node in backward_visited:
                return forward_traced_path + [forward_current_node] + backward_traced_path[::-1]

            if backward_current_node in forward_visited:
                return backward_traced_path[::-1] + [backward_current_node] + forward_traced_path

            forward_visited.add(forward_current_node)
            backward_visited.add(backward_current_node)

            if forward_current_node in self.graph:
                forward_neighbors = self.graph[forward_current_node]
                for forward_neighbor in forward_neighbors:
                    if forward_neighbor not in forward_visited:
                        forward_stack.append(
                            (forward_neighbor, forward_traced_path + [forward_current_node], forward_current_depth + 1)
                        )

            if backward_current_node in self.graph:
                backward_neighbors = self.graph[backward_current_node]
                for backward_neighbor in backward_neighbors:
                    if backward_neighbor not in backward_visited:
                        backward_stack.append(
                            (backward_neighbor, backward_traced_path + [backward_current_node],
                             backward_current_depth + 1)
                        )

        return None
g = Graph_idfs(directed=False)

g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('b', 'd')
g.add_edge('b', 'e')
g.add_edge('c', 'f')
g.add_edge('c', 'g')


start = 'a'
goal = 'f'
print(g.iterative_deepening(start , goal))
print(g.depth_limited_search(start , goal,3))
print(g.bidirectional_search(start , goal))

# path = print(g.iterative_deepening(start , goal))
# g.print_path(path , goal)