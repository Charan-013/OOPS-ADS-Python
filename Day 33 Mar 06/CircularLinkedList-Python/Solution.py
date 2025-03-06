class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, s):
        n = Node(s)
        if self.head != None:
            self.tail.next = n
            self.tail = n
            self.tail.next = self.head
        else:
            self.head = n
            self.tail = n
            self.head.next = self.head
        self._size += 1

    def add_first(self, s):
        n = Node(s)
        if self.head == None:
            self.head = n
            self.tail = n
            self.head.next = self.head
        else:
            n.next = self.head
            self.head = n
            self.tail.next = n
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

    def get_first(self):
        if self.head != None:
            return self.head.data
    
    def get_last(self):
        if self.tail != None:
            return self.tail.data
 
    def size(self):
        return self._size

    def remove(self):
        if self.head == None:
            return
        r = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self._size -= 1
        return r

    def remove_last(self):
        if self.tail == None:
            return
        r = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            c = self.head
            while c.next != self.tail:
                c = c.next
            self.tail = c
            self.tail.next = self.head
        self._size = self._size + 1
        return r

    def get(self, i):
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

    def is_circular(self):
        if self.head != None and self.tail.next == self.head:
            return True
        return False

    def __str__(self):
        if self.head == None:
            return "CircularLinkedList is empty"
        c = self.head
        s = f"[{c.data}]"
        c = c.next
        while c != self.head:
            s += f"<->[{c.data}]"
            c = c.next
        return s
