RED = True
BLACK = False

class Node:
    def __init__(self, key, val, color, count):
        self.key = key
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.count = count

class RedBlackBST:
    def __init__(self):
        self.root = None

    def is_red(self, x):
        if x is None:
            return False
        return x.color == RED

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        return x.count if x else 0

    def get(self, key):
        x = self.root
        while x:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
        self.root.color = BLACK

    def _put(self, h, key, val):
        if h is None:
            return Node(key, val, RED, 1)
        if key < h.key:
            h.left = self._put(h.left, key, val)
        elif key > h.key:
            h.right = self._put(h.right, key, val)
        else:
            h.val = val
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return h

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.count = h.count
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.count = h.count
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return x

    def flip_colors(self, h):
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    def min(self):
        if not self.root:
            return None
        return self._min(self.root).key

    def _min(self, x):
        while x.left:
            x = x.left
        return x

    def max(self):
        if not self.root:
            return None
        return self._max(self.root).key

    def _max(self, x):
        while x.right:
            x = x.right
        return x

    def floor(self, key):
        x = self._floor(self.root, key)
        if not x:
            raise ValueError("No floor found")
        return x.key

    def _floor(self, x, key):
        if x is None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        return t if t else x

    def ceiling(self, key):
        x = self._ceiling(self.root, key)
        if not x:
            raise ValueError("No ceiling found")
        return x.key

    def _ceiling(self, x, key):
        if x is None:
            return None
        if key == x.key:
            return x
        if key > x.key:
            return self._ceiling(x.right, key)
        t = self._ceiling(x.left, key)
        return t if t else x

    def select(self, k):
        x = self._select(self.root, k)
        if not x:
            raise ValueError("Rank out of bounds")
        return x.key

    def _select(self, x, k):
        if x is None:
            return None
        t = self._size(x.left)
        if t > k:
            return self._select(x.left, k)
        elif t < k:
            return self._select(x.right, k - t - 1)
        else:
            return x

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, x, key):
        if x is None:
            return 0
        if key < x.key:
            return self._rank(x.left, key)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(x.right, key)
        else:
            return self._size(x.left)

    def keys(self, lo=None, hi=None):
        if lo is None:
            lo = self.min()
        if hi is None:
            hi = self.max()
        result = []
        self._keys(self.root, result, lo, hi)
        return result

    def _keys(self, x, result, lo, hi):
        if x is None:
            return
        if lo < x.key:
            self._keys(x.left, result, lo, hi)
        if lo <= x.key <= hi:
            result.append(x.key)
        if hi > x.key:
            self._keys(x.right, result, lo, hi)

    def size_range(self, lo, hi):
        if hi < lo:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        return self.rank(hi) - self.rank(lo)

    def height(self):
        return self._height(self.root)

    def _height(self, x):
        if x is None:
            return -1
        return 1 + max(self._height(x.left), self._height(x.right))

    def level_order(self):
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def delete_min(self):
        if not self.root:
            return
        self.root = self._delete_min(self.root)

    def _delete_min(self, x):
        if x.left is None:
            return x.right
        x.left = self._delete_min(x.left)
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x

    def delete_max(self):
        if not self.root:
            return
        self.root = self._delete_max(self.root)

    def _delete_max(self, x):
        if x.right is None:
            return x.left
        x.right = self._delete_max(x.right)
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x
