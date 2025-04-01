class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append(node)
        self.bubble_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        self.swap(0, len(self.data) - 1)
        min_node = self.data.pop()
        self.bubble_down(0)
        return min_node

    def bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].priority < self.data[parent].priority:
                self.swap(index, parent)
                index = parent
            else:
                break

    def bubble_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < size and self.data[left].priority < self.data[smallest].priority:
                smallest = left
            if right < size and self.data[right].priority < self.data[smallest].priority:
                smallest = right
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_empty(self):
        return len(self.data) == 0


class Board:
    def __init__(self, tiles):
        self.tiles = [row[:] for row in tiles]
        self.n = len(self.tiles)
        self.blank = self.find_blank()

    def find_blank(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] == 0:
                    return [i, j]

    def is_goal(self):
        count = 1
        for i in range(self.n):
            for j in range(self.n):
                if i == self.n - 1 and j == self.n - 1:
                    if self.tiles[i][j] != 0:
                        return False
                else:
                    if self.tiles[i][j] != count:
                        return False
                    count += 1
        return True

    def manhattan(self):
        dist = 0
        for i in range(self.n):
            for j in range(self.n):
                val = self.tiles[i][j]
                if val != 0:
                    goal_row = (val - 1) // self.n
                    goal_col = (val - 1) % self.n
                    dist += abs(i - goal_row) + abs(j - goal_col)
        return dist

    def neighbors(self):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        neighbors = []
        x, y = self.blank[0], self.blank[1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < self.n and 0 <= ny < self.n:
                new_tiles = [row[:] for row in self.tiles]
                new_tiles[x][y], new_tiles[nx][ny] = new_tiles[nx][ny], new_tiles[x][y]
                neighbors.append(Board(new_tiles))
        return neighbors

    def twin(self):
        new_tiles = [row[:] for row in self.tiles]
        for i in range(self.n):
            for j in range(self.n - 1):
                if new_tiles[i][j] != 0 and new_tiles[i][j + 1] != 0:
                    new_tiles[i][j], new_tiles[i][j + 1] = new_tiles[i][j + 1], new_tiles[i][j]
                    return Board(new_tiles)

    def equals(self, other_board):
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] != other_board.tiles[i][j]:
                    return False
        return True

    def __str__(self):
        out = str(self.n) + "\n"
        for row in self.tiles:
            out += " ".join("{:2}".format(num) for num in row) + " \n"
        return out


class SearchNode:
    def __init__(self, board, moves, prev):
        self.board = board
        self.moves = moves
        self.prev = prev
        self.priority = self.moves + self.board.manhattan()


class Solver:
    def __init__(self, initial_board):
        self.solution_path = []
        self.solve(initial_board)

    def solve(self, initial_board):
        pq = MinHeap()
        twin_pq = MinHeap()
        pq.push(SearchNode(initial_board, 0, None))
        twin_pq.push(SearchNode(initial_board.twin(), 0, None))

        while True:
            result = self.expand(pq)
            if result is not None:
                self.reconstruct(result)
                return
            if self.expand(twin_pq) is not None:
                self.solution_path = None
                return

    def expand(self, pq):
        if pq.is_empty():
            return None
        node = pq.pop()
        if node.board.is_goal():
            return node
        for neighbor in node.board.neighbors():
            if node.prev is not None and neighbor.equals(node.prev.board):
                continue
            pq.push(SearchNode(neighbor, node.moves + 1, node))
        return None

    def reconstruct(self, node):
        while node is not None:
            self.solution_path.insert(0, node.board)
            node = node.prev

    def moves(self):
        return len(self.solution_path) - 1 if self.solution_path else -1

    def solution(self):
        return self.solution_path


def read_input():
    n = int(input())
    tiles = []
    for _ in range(n):
        row = list(map(int, input().split()))
        tiles.append(row)
    return Board(tiles)

def run_solver():
    initial_board = read_input()
    solver = Solver(initial_board)
    if solver.solution():
        print("Minimum number of moves =", solver.moves())
        for board in solver.solution():
            print(board)
    else:
        print("No solution possible")

run_solver()
     