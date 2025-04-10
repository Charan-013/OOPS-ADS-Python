class Node:
    def __init__(self, key, value, color, left=None, right=None, size=1):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.size = size

class RedBlackBST:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = 0

    def _put(self, x, key, value):
        if x is None:
            return Node(key, value, 1)
        
        if key < x.key:
            x.left = self._put(x.left, key, value)
        elif key > x.key:
            x.right = self._put(x.right, key, value)
        else:
            x.value = value
        
        if self._isRed(x.right) and not self._isRed(x.left):
            x = self._rotateLeft(x)
        if self._isRed(x.left) and self._isRed(x.left.left):
            x = self._rotateRight(x)
        if self._isRed(x.left) and self._isRed(x.right):
            self._flipColors(x)

        x.size = 1 + self._size(x.left) + self._size(x.right)
        return x

    def _isRed(self, x):
        if x is None:
            return False
        return x.color == 1

    def _rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 1
        x.size = h.size
        h.size = 1 + self._size(h.left) + self._size(h.right)
        return x

    def _rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 1
        x.size = h.size
        h.size = 1 + self._size(h.left) + self._size(h.right)
        return x

    def _flipColors(self, h):
        h.color = 1
        h.left.color = 0
        h.right.color = 0

    def _size(self, x):
        if x is None:
            return 0
        return x.size

    def isBST(self):
        return self._isBST(self.root, None, None)

    def _isBST(self, x, min_key, max_key):
        if x is None:
            return True
        if (min_key is not None and x.key <= min_key) or (max_key is not None and x.key >= max_key):
            return False
        return self._isBST(x.left, min_key, x.key) and self._isBST(x.right, x.key, max_key)

    def is23(self):
        return self._is23(self.root)

    def _is23(self, x):
        if x is None:
            return True
        if self._isRed(x.right):
            return False
        if self._isRed(x.left) and self._isRed(x.left.left):
            return False
        return self._is23(x.left) and self._is23(x.right)

    def isBalanced(self):
        black_count = self._blackHeight(self.root)
        return self._isBalanced(self.root, black_count, 0)

    def _blackHeight(self, x):
        if x is None:
            return 0
        left_black = self._blackHeight(x.left)
        right_black = self._blackHeight(x.right)
        if left_black != right_black:
            raise ValueError("Tree is not balanced.")
        return left_black + (1 if x.color == 0 else 0)

    def _isBalanced(self, x, black_count, current_black_count):
        if x is None:
            return current_black_count == black_count
        next_black_count = current_black_count + (1 if x.color == 0 else 0)
        return self._isBalanced(x.left, black_count, next_black_count) and self._isBalanced(x.right, black_count, next_black_count)

    def isRedBlackBST(self):
        return self.isBST() and self.is23() and self.isBalanced()
