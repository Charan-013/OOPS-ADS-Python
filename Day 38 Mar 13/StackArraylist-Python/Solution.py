class ArrayListADT:
    def __init__(self,capacity = 10):
        self.data = []
        self.size = len(self.data)
        self.capacity = capacity

    def add(self, e):
        self.data = self.data + [e]
        self.size = len(self.data)
        return True


    def size_(self):
        return self.size

    def is_empty(self):
        return len(self.data) == 0

    def remove_at(self, index):
        first = self.data[:index]
        middle = self.data[index]
        last = self.data[index + 1 :]
        self.data = first + last
        self.size = len(self.data)
        return middle

    def __str__(self):
        return f"{self.data}"
    
class MyQueue:
    def __init__(self,size=10):
        self.queue = ArrayListADT(size)
        self.front = None
        self.back = None
    
    def add(self,e):
        if self.queue.size_() >= self.queue.capacity:
                return
        if self.front == None and self.back == None:
            self.queue.add(e)
            self.front = e
            self.back = e
            return True
        else:
            self.queue.add(e)
            self.back = e
            return True
    
    def peek(self):
        if self.front == None:
            return None
        return self.front
    
    def remove(self):
        if self.front == None:
            raise IndexError
        if not self.queue.is_empty():
            r = self.queue.remove_at(0)
            if self.queue.is_empty():
                self.front = None
                self.back = None
            else:
                self.front = self.queue.data[0]
        return r
    
    def __str__(self):
        return str(self.queue)
    
class Stack:
    def __init__(self):
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()
        self.top = None
    
    def empty(self):
        return self.top == None
    
    def peek(self):
        if self.queue2.queue.is_empty():
            raise IndexError
        return self.top

    
    def pop(self):
        if self.queue2.queue.is_empty():
            raise IndexError
        r = self.queue2.remove()
        if not self.queue2.queue.is_empty():
            self.top = self.queue2.queue.data[0]
        else:
            self.top = None
        return r
    
    def push(self, e):
        self.queue1.add(e)
        self.top = e
        while not self.queue2.queue.is_empty():
            self.queue1.add(self.queue2.remove())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return e

    def search(self, e): 
        for i in range(self.queue2.queue.size_()):
            if self.queue2.queue.data[i] == e:
                return i + 1
        return -1
