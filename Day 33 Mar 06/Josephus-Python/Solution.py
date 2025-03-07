class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, s):
        n = Node(s)
        if self.head != None:
            self.tail.next = n
            n.prev = self.tail
            n.next = self.head
            self.head.prev = n
            self.tail = n
        else:
            self.head = n
            self.tail = n
            self.head.next = self.head
            self.head.prev = self.head
        self._size += 1

    def contains(self, s):
        c = self.head
        if c == None:
            return False
        for n in range(self._size):
            if c.data == s:
                return True
            c = c.next
        return False
 
    def size(self):
        return self._size
    
    def remove_at(self, i):
        if self.head == None:
            return 
        if i >= 0:
            c = self.head
            for n in range(i):
                c = c.next
        else:
            c = self.tail
            for n in range(-i):
                c = c.prev
        c.prev.next = c.next
        c.next.prev = c.prev
        if c == self.tail:
            self.tail = c.prev
        if c == self.head:
            self.head = c.next

        self._size = self._size - 1
        return c.data


    def getData(self, i):
        if i < 0 or i >= self.size():
            return None
        c = self.head
        for n in range(i):
            c = c.next
        return c.data

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        c = self.head
        s = f"[{c.data}]"
        c = c.next
        while c != self.head:
            s += f"<->[{c.data}]"
            c = c.next
        return s

class Josephus:
    def josephusDCLL(self, size, rotation):
        doubleCircular = DoublyCircularLL()
        for i in range(1,size+1):
            doubleCircular.add(i)
        if size == rotation == 1:
            return doubleCircular.getData(0)
        # print(doubleCircular)
        idx = 0
        k = rotation - 1
        while doubleCircular.size() > 1:
            idx = (idx + k) % doubleCircular.size()
            d = doubleCircular.remove_at(idx)
        return doubleCircular.getData(0)
