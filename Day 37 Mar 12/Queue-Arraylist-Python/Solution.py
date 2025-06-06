class FullQueueException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

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
    def __init__(self,size):
        self.queue = ArrayListADT(size)
        self.front = None
        self.back = None
    
    def add(self,e):
        if self.queue.size_() >= self.queue.capacity:
            raise FullQueueException()
        if self.front == None and self.back == None:
            self.queue.add(e)
            self.front = e
            self.back = e
            return True
        else:
            self.queue.add(e)
            self.back = e
            return True


    def element(self):
        if self.front == None:
            raise IndexError
        return self.front
    
    def offer(self,e):
        if self.queue.size_() < self.queue.capacity:
            if self.front == None and self.back == None:
                self.queue.add(e)
                self.front = e
                self.back = e
            else:
                self.queue.add(e)
                self.back = e
            return True
        return False
    
    def peek(self):
        if self.front == None:
            return None
        return self.front
    
    def poll(self):
        if self.front == None:
            return
        if not self.queue.is_empty():
            r = self.queue.remove_at(0)
            if self.queue.is_empty():
                self.front = None
                self.back = None
            else:
                self.front = self.queue.data[0]
        return r
    
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