class Node:
    def __init__(self, key, val):
        self.key = int(key)
        self.val = int(val)
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def insert(self, key, val):
        def insert_node(node, key, val):
            if not node:
                return Node(key, val)
            if key < node.key:
                node.left = insert_node(node.left, key, val)
            elif key > node.key:
                node.right = insert_node(node.right, key, val)
            else:
                node.val = val
                return node

            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            balance = self.get_balance(node)

            if balance > 1:
                if key < node.left.key:
                    return self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)
            if balance < -1:
                if key > node.right.key:
                    return self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)

            return node

        self.root = insert_node(self.root, int(key), int(val))

    def delete(self, key):
        def min_value_node(node):
            while node.left:
                node = node.left
            return node

        def delete_node(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = delete_node(node.left, key)
            elif key > node.key:
                node.right = delete_node(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = min_value_node(node.right)
                node.key, node.val = temp.key, temp.val
                node.right = delete_node(node.right, temp.key)

            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            balance = self.get_balance(node)

            if balance > 1:
                if self.get_balance(node.left) >= 0:
                    return self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)
            if balance < -1:
                if self.get_balance(node.right) <= 0:
                    return self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)

            return node

        self.root = delete_node(self.root, int(key))

    def range_query(self, low, high):
        result = []

        def search_range(node):
            if not node:
                return
            if low < node.key:
                search_range(node.left)
            if low <= node.key <= high:
                result.append(f"{node.key}:{node.val}")
            if high > node.key:
                search_range(node.right)

        search_range(self.root)
        print(" ".join(result) if result else "EMPTY")

    def aggregate_query(self, low, high):
        def sum_range(node):
            if not node:
                return 0
            total = 0
            if low < node.key:
                total += sum_range(node.left)
            if low <= node.key <= high:
                total += node.val
            if high > node.key:
                total += sum_range(node.right)
            return total

        print(sum_range(self.root))


def main():
    t = int(input())
    for i in range(t):
        tree = AVL()
        n = int(input())
        for j in range(n):
            parts = input().split()
            if parts[0] == "I":
                tree.insert(parts[1], parts[2])
            elif parts[0] == "D":
                tree.delete(parts[1])
            elif parts[0] == "R":
                tree.range_query(int(parts[1]), int(parts[2]))
            elif parts[0] == "A":
                tree.aggregate_query(int(parts[1]), int(parts[2]))
        print()
main()

