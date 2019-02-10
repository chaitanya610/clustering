class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def isCyclic(self, parent, u, v):
        x = self.find(parent, u)
        y = self.find(parent, v)
        parent[y] = x
        return x == y

    def kruskalMST(self):
        result = []
        self.graph = sorted(self.graph, key=lambda x: x[2])
        parent = list(range(self.V + 1))
        i = 0
        edges = 0
        while edges < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            if not self.isCyclic(parent, u, v):
                edges += 1
                result.append([u, v])
        return result, self.V - 1 - edges


def MST(g_nodes, g_edges):
    g = Graph(g_nodes)
    g.graph = g_edges
    return g.kruskalMST()
