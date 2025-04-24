class Graph:
    def __init__(self, vertex_count, vertex_names):
        self.vertex_count = vertex_count
        self.edge_count = 0
        self.vertex_names = vertex_names
        self.index_to_name = {}
        self.name_to_index = {}
        for i in range(len(vertex_names)):
            self.index_to_name[i] = vertex_names[i]
            self.name_to_index[vertex_names[i]] = i

    def add_edge(self, from_vertex, to_vertex):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError


class AdjacencyList(Graph):
    def __init__(self, vertex_count, vertex_names):
        super().__init__(vertex_count, vertex_names)
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex != to_vertex and to_vertex not in self.adjacency_list[from_vertex] and from_vertex not in self.adjacency_list[to_vertex]:
            self.adjacency_list[from_vertex].insert(0, to_vertex)
            self.adjacency_list[to_vertex].insert(0, from_vertex)
            self.edge_count += 1

    def display(self):
        print(f"{self.vertex_count} vertices, {self.edge_count} edges")
        for i in range(self.vertex_count):
            adjacent_vertices = self.adjacency_list[i]
            if adjacent_vertices:
                neighbors_str = " ".join(self.index_to_name[neighbor] for neighbor in adjacent_vertices)
                print(f"{self.index_to_name[i]}: {neighbors_str}")


class AdjacencyMatrix(Graph):
    def __init__(self, vertex_count, vertex_names):
        super().__init__(vertex_count, vertex_names)
        self.matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex != to_vertex and self.matrix[from_vertex][to_vertex] == 0:
            self.matrix[from_vertex][to_vertex] = 1
            self.matrix[to_vertex][from_vertex] = 1
            self.edge_count += 1

    def display(self):
        print(f"{self.vertex_count} vertices, {self.edge_count} edges")
        for row in self.matrix:
            print(" ".join(str(cell) for cell in row))


def main():
    graph_type = input().strip()
    vertex_count = int(input().strip())
    edge_input_count = int(input().strip())
    vertex_names_line = input().strip()

    if vertex_count == 0:
        print("0 vertices, 0 edges")
        print("No edges")
        return

    vertex_names = [name.strip() for name in vertex_names_line.split(",")]

    if graph_type == "List":
        graph = AdjacencyList(vertex_count, vertex_names)
    else:
        graph = AdjacencyMatrix(vertex_count, vertex_names)

    for _ in range(edge_input_count):
        from_vertex, to_vertex = map(int, input().strip().split())
        if 0 <= from_vertex < vertex_count and 0 <= to_vertex < vertex_count:
            graph.add_edge(from_vertex, to_vertex)
        else:
            print(f"Invalid edge ({from_vertex}, {to_vertex}). Skipping.")

    if graph.edge_count == 0:
        print("No edges")
    else:
        graph.display()


if __name__ == "__main__":
    main()
