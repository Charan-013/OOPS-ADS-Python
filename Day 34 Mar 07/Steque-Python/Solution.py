class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Steque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = None

    def push(self,s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size = self._size + 1

    def pop(self,s):
        pass

    def enqueue(self,s):
        pass

    def size(self):
        return self._size
    
    def isEmpty(self):
        pass

    def __str__(self):
        pass