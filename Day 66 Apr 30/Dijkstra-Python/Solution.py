class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __repr__(self):
        return f"{self.v}->{self.w} {self.weight:.2f}"


class EdgeWeightedDigraph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_edge(self, e):
        self.adj[e.v].append(e)

    def edges(self):
        for v in range(self.V):
            for e in self.adj[v]:
                yield e


class DijkstraSP:
    def __init__(self, G, s):
        self.G = G
        self.s = s
        self.distTo = [float("inf")] * G.V
        self.edgeTo = [None] * G.V
        self.distTo[s] = 0.0

        self.unvisited = set(range(G.V))

        while self.unvisited:
            v = self._min_distance_vertex()
            self.unvisited.remove(v)
            for e in self.G.adj[v]:
                self.relax(e)

    def _min_distance_vertex(self):
        min_dist = float("inf")
        min_vertex = -1
        for v in self.unvisited:
            if self.distTo[v] < min_dist:
                min_dist = self.distTo[v]
                min_vertex = v
        return min_vertex

    def relax(self, e):
        v = e.v
        w = e.w
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e

    def distTo(self, v):
        return self.distTo[v]

    def hasPathTo(self, v):
        return self.distTo[v] < float("inf")

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e:
            path.append(e)
            e = self.edgeTo[e.v]
        path.reverse()
        return path

    def check(self):
        for v in range(self.G.V):
            for e in self.G.adj[v]:
                assert (
                    self.distTo[e.w] <= self.distTo[e.v] + e.weight
                ), f"Edge relaxation error: {e}"


def read_graph():
    V = int(input())
    E = int(input())
    G = EdgeWeightedDigraph(V)

    for i in range(E):
        v, w, weight = input().split()
        v, w, weight = int(v), int(w), float(weight)
        G.add_edge(DirectedEdge(v, w, weight))

    return G


def main():
    G = read_graph()
    s = 0
    sp = DijkstraSP(G, s)

    for v in range(G.V):
        if sp.hasPathTo(v):
            path = sp.pathTo(v)
            print(f"0 to {v} ({sp.distTo[v]:.2f})", end="  ")
            for e in path:
                print(f"{e.v}->{e.w}  {e.weight:.2f}", end="   ")
            print()
        else:
            print(f"0 to {v} (no path)")


if __name__ == "__main__":
    main()
