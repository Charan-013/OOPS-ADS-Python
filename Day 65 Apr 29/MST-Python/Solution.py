class DisjointSet:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        for i in range(size + 1):
            self.parent.append(i)
            self.rank.append(0)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True


def minimum_spanning_tree(node_count, edge_list):
    edge_list.sort(key=lambda x: x[2])
    disjoint_set = DisjointSet(node_count)
    mst_edges = []
    total_cost = 0
    edge_count = 0

    for edge in edge_list:
        u = edge[0]
        v = edge[1]
        weight = edge[2]

        if disjoint_set.union(u, v):
            mst_edges.append([u, v, weight])
            total_cost += weight
            edge_count += 1

        if edge_count == node_count - 1:
            break

    return total_cost, mst_edges


if __name__ == "__main__":
    nodes, edges = map(int, input().split())
    graph_edges = []
    for _ in range(edges):
        u, v, w = map(int, input().split())
        graph_edges.append([u, v, w])

    total_cost, mst = minimum_spanning_tree(nodes, graph_edges)
    print(total_cost)
    for edge in mst:
        print(edge[0], edge[1], edge[2])
