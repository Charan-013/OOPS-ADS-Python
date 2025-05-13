class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, vertex):
        return self.w if vertex == self.v else self.v

    def __lt__(self, other):
        return self.weight < other.weight


class MinPQ:
    def __init__(self):
        self.data = []

    def insert(self, edge):
        self.data.append(edge)
        self.swim(len(self.data) - 1)

    def del_min(self):
        if not self.data:
            return None
        self.swap(0, len(self.data) - 1)
        min_edge = self.data.pop()
        self.sink(0)
        return min_edge

    def is_empty(self):
        return len(self.data) == 0

    def swim(self, k):
        while k > 0 and self.data[k] < self.data[(k - 1) // 2]:
            self.swap(k, (k - 1) // 2)
            k = (k - 1) // 2

    def sink(self, k):
        n = len(self.data)
        while 2 * k + 1 < n:
            j = 2 * k + 1
            if j + 1 < n and self.data[j + 1] < self.data[j]:
                j += 1
            if self.data[k] < self.data[j]:
                break
            self.swap(k, j)
            k = j

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]


class EdgeWeightedGraph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.adj[v].append(edge)
        self.adj[w].append(edge)


class LazyPrimMST:
    def __init__(self, graph):
        self.marked = [False] * graph.V
        self.total_weight = 0
        self.pq = MinPQ()

        for v in range(graph.V):
            if not self.marked[v]:
                self.prim(graph, v)

    def prim(self, graph, s):
        self.visit(graph, s)
        while not self.pq.is_empty():
            edge = self.pq.del_min()
            v = edge.either()
            w = edge.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.total_weight += edge.weight
            if not self.marked[v]:
                self.visit(graph, v)
            if not self.marked[w]:
                self.visit(graph, w)

    def visit(self, graph, v):
        self.marked[v] = True
        for edge in graph.adj[v]:
            if not self.marked[edge.other(v)]:
                self.pq.insert(edge)


def main():
    V = int(input())
    E = int(input())
    graph = EdgeWeightedGraph(V)

    for i in range(E):
        v, w, weight = input().split()
        graph.add_edge(Edge(int(v), int(w), float(weight)))

    mst = LazyPrimMST(graph)
    print(round(mst.total_weight, 2))


main()
