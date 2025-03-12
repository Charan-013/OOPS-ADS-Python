class FullQueueException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self, size=0):
        self.head = None
        self.size = size
    
    def empty(self):
        return self.head == None
    
    def length(self):
        c = self.head
        count = 0
        while c != None:
            count = count + 1
            c = c.next
        return count
    
    def peek(self):
        if not self.empty():
            return self.head.item
        else:
            raise IndexError
        
    def pop(self):
        if not self.empty():
            r = self.head.item
            self.head = self.head.next
            return r
        else:
            raise IndexError
    
    def push(self, item):
        if self.length() >= self.size:
            raise FullQueueException()
        node = Node(item)
        if self.empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head.item
    
    def __str__(self):
        s = ""
        c = self.head
        while c != None:
            s += f"{c.item} "
            c = c.next
        return s.strip()

class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stackIn = Stack(capacity)
        self.stackOut = Stack(capacity)
    
    def size(self):
        return self.stackIn.length() + self.stackOut.length()
    
    def add(self, e):
        if self.size() >= self.capacity:
            raise FullQueueException()
        self.stackIn.push(e)
        return True

    def element(self):
        if self.empty():
            raise IndexError
        if self.stackOut.empty():
            self._transfer()
        return self.stackOut.peek()
    
    def offer(self, e):
        if self.size() >= self.capacity:
            return False
        self.stackIn.push(e)
        return True
    
    def peek(self):
        if self.empty():
            return None
        if self.stackOut.empty():
            self._transfer()
        return self.stackOut.peek()
    
    def poll(self):
        if self.empty():
            return None
        if self.stackOut.empty():
            self._transfer()
        return self.stackOut.pop()
    
    def remove(self):
        if self.empty():
            raise IndexError()
        if self.stackOut.empty():
            self._transfer()
        return self.stackOut.pop()
    
    def _transfer(self):
        while not self.stackIn.empty():
            self.stackOut.push(self.stackIn.pop())
    
    def empty(self):
        return self.stackIn.empty() and self.stackOut.empty()
