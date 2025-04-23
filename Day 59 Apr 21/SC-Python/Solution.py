class Node:
    def __init__(self,key,value,next = None):
        self.key = key
        self.value = value
        self.next = next

class SeparateChainingHashST:
    def __init__(self,capacity = 10):
        self.numOfpairs = 0
        self.noChains = capacity
        self.array = [None] * self.noChains

    def put(self, k, v):
        if v is None:
            self.delete(k)
            return
        i = self.hashfun(k)
        x = self.array[i]
        while x:
            if x.key == k:
                x.value = v
                return
            x = x.next

        self.array[i] = Node(k, v, self.array[i])
        self.numOfpairs += 1

        if self.numOfpairs >= 10 * self.noChains:
            self.resize(2 * self.noChains)

    def get(self, k):
        i = self.hashfun(k)
        x = self.array[i]
        while x:
            if x.key == k:
                return x.value
            x = x.next
        return None

    def contains(self, k):
        if self.get(k) != None:
            return True
        return False

    def delete(self, k):
        def delete_node(node, key):
            if not node:
                return None, False
            if node.key == key:
                return node.next, True
            rest, deleted = delete_node(node.next, key)
            node.next = rest
            return node, deleted
        i = self.hashfun(k)
        self.array[i], deleted = delete_node(self.array[i], k)
        if deleted:
            self.numOfpairs -= 1
            if self.noChains > 4 and self.numOfpairs <= 2 * self.noChains:
                self.resize(self.noChains // 2)


    def keys(self):
        k = []
        for ele in self.array:
            x = ele
            while x:
                k.append(x.key)
                x = x.next
        return k

    def is_empty(self):
        return self.numOfpairs == 0

    def size(self):
        return self.numOfpairs
    
    def resize(self, new_capacity):
        temp = SeparateChainingHashST(new_capacity)
        for key in self.keys():
            temp.put(key, self.get(key))
        self.noChains = temp.noChains
        self.numOfpairs = temp.numOfpairs
        self.array = temp.array

    def hashfun(self, key):
        return hash(key) % self.noChains