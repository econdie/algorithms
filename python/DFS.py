class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def DFS(self, node):
        self.visited.append(node)
        print('visited: ', node)

        for key, value in enumerate(self.graph[node]):
            if value == 1 and key not in self.visited:
                self.DFS(key)

graph = [[0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0]]
g = Graph(graph)
g.DFS(0)