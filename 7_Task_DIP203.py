class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def neighbors(self, u):
        return self.graph.get(u, [])

    def print_graph(self):
        for vertex in self.graph: print(f"{vertex}: {self.graph[vertex]}")

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
g.print_graph()

neighbors = g.neighbors('B')
print()
print(neighbors) # By B. Nazarzoda 241ADB013