class Node:
    """Represents a node in the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """A Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def add(self, data, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(data)
            else:
                return self.add(data, self.root)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    return self.add(data, node.left)
            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    return self.add(data, node.right)

    def contains(self, data):
        node = self.root
        while node != None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return True
        return False

    def max(self):
        node = self.root
        while node and node.right != None:
            node = node.right
        return node.data if node else None

    def size(self):
        count = 0
        lst = [self.root]
        while lst:
            node = lst.pop()
            if node:
                count += 1
                lst.append(node.left)
                lst.append(node.right)
        return count

    def in_order(self):
        r = []
        s = []
        node = self.root
        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            r.append(node.data)
            node = node.right
        for ele in r:
            print(ele,end=" ")
        print()

    def pre_order(self):
        r = []
        if self.root == None:
            return r
        s = [self.root]
        while s:
            node = s.pop()
            r.append(node.data)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        for ele in r:
            print(ele,end=" ")
        print()

