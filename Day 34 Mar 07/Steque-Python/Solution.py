class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Steque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self,s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self._size = self._size + 1

    def pop(self):
        if self.head == None:return
        r = self.head.data
        self.head = self.head.next
        self._size = self._size - 1
        return r
    
    def enqueue(self,s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size = self._size + 1

    def size(self):
        return self._size
    
    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.head == None:return f"Steque is empty"
        c = self.head
        s = ""
        while c!= None:
            s += f"[{c.data}]"
            c = c.next
        return s