def insertionSort(l1):
    for i in range(1,len(l1)):
        for j in range(i,0,-1):
            if l1[j] < l1[j-1]:
                l1[j],l1[j-1] = l1[j-1],l1[j]
            else:
                break
    return l1

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class SequentialSearchST:
    def __init__(self):
        self.head = None
        self.size_ = 0

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        return self.size_
    
    def put(self,key,value):
        c = self.head
        while c:
            if c.key == key:
                c.value = value
                return
            c = c.next
        node = Node(key, value)
        node.next = self.head
        self.head = node
        self.size_ += 1

    def get(self,key):
        c = self.head
        while c:
            if c.key == key:
                return c.value
            c = c.next
        return None

    def delete(self,key):
        if self.head == None:
            return
        if self.head.key == key:
            self.head = self.head.next
            self.size_ -= 1
            return
        c = self.head
        while c.next:
            if c.next.key == key:
                c.next = c.next.next
                self.size_ -= 1
                return
            c = c.next
                
            
    def contains(self,key):
        if self.get(key):
            return True
        return False

    def min(self):
        c = self.head
        min_key = float("inf")
        while c:
            if c.key < min_key:
                min_key = c.key
            c = c.next
        return min_key

    def max(self):
        c = self.head
        max_key = float("-inf")
        while c:
            if c.key >= max_key:
                max_key = c.key
            c = c.next
        return max_key
        
    def floor(self, key):
        c = self.head
        floor_key = None
        while c:
            if c.key <= key:
                if floor_key is None or c.key > floor_key:
                    floor_key = c.key
            c = c.next
        return floor_key

    def ceiling(self, key):
        c = self.head
        ceiling_key = None
        while c:
            if c.key >= key:
                if ceiling_key is None or c.key < ceiling_key:
                    ceiling_key = c.key
            c = c.next
        return ceiling_key
        
    def rank(self,key):
        c = self.head
        count = 0
        while c:
            if c.key < key:
                count += 1
            c = c.next
        return count

    def select(self, k):
        c = self.head
        i = 0
        while c:
            if i == k:
                return c.key
            i += 1
            c = c.next
        return None


    def deleteMin(self):
        m = self.min()
        self.delete(m)

    def deleteMax(self):
        m = self.max()
        self.delete(m)
        

    def keys(self):
        k = []
        c = self.head
        while c:
            k.append(c.key)
            c = c.next
        return k
    
    def size_range(self,start,stop):
        c = self.head
        size = 0
        while c:
            if start <= c.key <= stop:
                size += 1
            c = c.next
        return size

    def keys_range(self,start,stop):
        keys = []
        c = self.head
        while c:
            if start <= c.key <= stop:
                keys.append(c.key)
            c = c.next
        return insertionSort(keys)