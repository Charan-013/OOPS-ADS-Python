class BinaryTree:
    class BTNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.data)

    def __init__(self, element=None, left_tree=None, right_tree=None):
        if element is None:
            self.root = None
        else:
            self.root = BinaryTree.BTNode(element)
            if left_tree is not None:
                self.root.left = left_tree.root
            if right_tree is not None:
                self.root.right = right_tree.root

    def countInternal(self):
        """Returns the number of internal (non-leaf) nodes in the tree."""
        def count(node):
            if node is None or (node.left is None and node.right is None):
                return 0
            return 1 + count(node.left) + count(node.right)
        
        return count(self.root)

    def height(self):
        """Returns the height of the tree."""
        def get_height(node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        return get_height(self.root)

    def isPerfect(self):
        """Returns True if the tree is perfect."""
        def get_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        def check_perfect(node, depth, level=0):
            if node is None:
                return True
            if node.left is None and node.right is None:
                return depth == level + 1
            if node.left is None or node.right is None:
                return False
            return check_perfect(node.left, depth, level + 1) and check_perfect(node.right, depth, level + 1)
        
        depth = get_depth(self.root)
        return check_perfect(self.root, depth)

    def __str__(self):
        lines = []
        self.preOrderTraversal(self.root, 0, lines)
        return "\n".join(lines)

    def preOrderTraversal(self, node, depth, lines):
        indent = "  " * (depth - 1) if depth > 0 else ""
        if node is None:
            lines.append(indent + "null")
        else:
            lines.append(indent + str(node))
            self.preOrderTraversal(node.left, depth + 1, lines)
            self.preOrderTraversal(node.right, depth + 1, lines)
