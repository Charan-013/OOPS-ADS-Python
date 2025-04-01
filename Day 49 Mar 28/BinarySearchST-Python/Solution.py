class BinarySearchST:
    def __init__(self):
        self.keys = []
        self.values = []
        self.size_ = 0

    def isEmpty(self):
        return self.size_ == 0

    def size(self):
        return self.size_

    def rank(self,key):
        lo, hi = 0, self.size_ - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.keys[mid] < key:
                lo = mid + 1
            elif self.keys[mid] > key:
                hi = mid - 1
            else:
                return mid
        return lo

    def put(self,key,value):
        i = self.rank(key)
        
        if i < self.size_ and self.keys[i] == key:
            self.values[i] = value
        else:
            self.keys.insert(i, key)
            self.values.insert(i, value)
            self.size_ += 1

    def get(self, key):
        i = self.rank(key)
        if i < self.size_ and self.keys[i] == key:
            return self.values[i]
        return None

    def delete(self, key):
        i = self.rank(key)
        if i < self.size_ and self.keys[i] == key:
            self.keys.pop(i)
            self.values.pop(i)
            self.size_ -= 1

    def contains(self, key):
        return self.get(key) is not None

    def min(self):
        if self.isEmpty():
            return None
        return self.keys[0]

    def max(self):
        if self.isEmpty():
            return None
        return self.keys[-1]

    def floor(self, key):
        i = self.rank(key)
        if i < self.size_ and self.keys[i] == key:
            return self.keys[i]
        if i > 0:
            return self.keys[i - 1]
        return None

    def ceiling(self, key):
        i = self.rank(key)
        if i < self.size_ and self.keys[i] >= key:
            return self.keys[i]
        return None

    def select(self, k):
        if 0 <= k < self.size_:
            return self.keys[k]
        return None

    def deleteMin(self):
        if not self.isEmpty():
            self.delete(self.keys[0])

    def deleteMax(self):
        if not self.isEmpty():
            self.delete(self.keys[-1])

    def size_range(self, start, stop):
        return self.rank(stop + 1) - self.rank(start)

    def keys(self):
        return self.keys

    def keys_range(self, start, stop):
        i_start = self.rank(start)
        i_end = self.rank(stop + 1)
        return self.keys[i_start:i_end]

    def keys_all(self):
        return self.keys
