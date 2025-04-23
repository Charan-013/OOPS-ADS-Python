class AdjacencyList:
    def __init__(self, num_vertices, keys):
        self.num_vertices = num_vertices
        self.keys = keys
        self.adj = [[] for _ in range(num_vertices)]
        self.edge_count = 0

    def add_edge(self, v, w):
        if v == w:
            return
        if w not in self.adj[v]:
            self.adj[v].append(w)
            self.adj[w].append(v)
            self.edge_count += 1

    def display(self):
        print(f"{self.num_vertices} vertices, {self.edge_count} edges")
        for i in range(self.num_vertices):
            neighbors = []
            for j in range(self.num_vertices):
                if j in self.adj[i]:
                    neighbors.append(self.keys[j])
            neighbors.sort()  
            print(f"{self.keys[i]}: {' '.join(neighbors)}")




class AdjacencyMatrix:
    def __init__(self, num_vertices, keys):
        self.num_vertices = num_vertices
        self.keys = keys
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.edge_count = 0

    def add_edge(self, v, w):
        if v == w:
            return
        if self.matrix[v][w] == 0:
            self.matrix[v][w] = 1
            self.matrix[w][v] = 1
            self.edge_count += 1

    def display(self):
        print(f"{self.num_vertices} vertices, {self.edge_count} edges")
        for row in self.matrix:
            print(" ".join(str(val) for val in row))


def main():
    represents = input().strip()
    numVer = int(input())
    numEdg = int(input())
    keys = input().strip().split(",")
    if keys == ['']:
        print("0 vertices, 0 edges")
        print("No edges")
        return
    lst = []
    for i in range(numEdg):
        lst.append(list(map(int, input().strip().split())))

    if represents == "List":
        r = AdjacencyList(numVer, keys)
    elif represents == "Matrix":
        r = AdjacencyMatrix(numVer, keys)

    for edge in lst:
        r.add_edge(edge[0], edge[1])

    if r.edge_count == 0:
        print("No edges")
    else:
        r.display()

main()
