class AdjacencyListGraph:
    def __init__(self, total_vertices, labels):
        self.total_vertices = total_vertices
        self.labels = labels
        self.graph = [[] for _ in range(total_vertices)]
        self.total_edges = 0

    def insert_edge(self, start, end):
        if start != end:
            if end not in self.graph[start]:
                self.graph[start].insert(0, end)
                self.graph[end].insert(0, start)
                self.total_edges += 1

    def show(self):
        if self.total_edges == 0:
            print("No edges")
            return
        print(f"{self.total_vertices} vertices, {self.total_edges} edges")
        for i in range(self.total_vertices):
            neighbors = self.graph[i]
            if neighbors:
                neighbor_labels = " ".join(self.labels[neighbor] for neighbor in neighbors)
                print(f"{self.labels[i]}: {neighbor_labels}")


class AdjacencyMatrixGraph:
    def __init__(self, total_vertices, labels):
        self.total_vertices = total_vertices
        self.labels = labels
        self.matrix = [[0] * total_vertices for _ in range(total_vertices)]
        self.total_edges = 0

    def insert_edge(self, start, end):
        if start != end:
            if self.matrix[start][end] == 0:
                self.matrix[start][end] = 1
                self.matrix[end][start] = 1
                self.total_edges += 1

    def show(self):
        print(f"{self.total_vertices} vertices, {self.total_edges} edges")
        for row in self.matrix:
            print(" ".join(str(cell) for cell in row))


def main():
    graph_type = input().strip()
    vertex_count = int(input())
    edge_count = int(input())
    labels = input().strip().split(",")
    
    if labels == ['']:
        print("0 vertices, 0 edges")
        print("No edges")
        return

    edges = []
    for _ in range(edge_count):
        edges.append(list(map(int, input().strip().split())))

    if graph_type == "List":
        graph = AdjacencyListGraph(vertex_count, labels)
    elif graph_type == "Matrix":
        graph = AdjacencyMatrixGraph(vertex_count, labels)

    for edge in edges:
        graph.insert_edge(edge[0], edge[1])

    if graph.total_edges == 0:
        print("No edges")
    else:
        graph.show()


main()
