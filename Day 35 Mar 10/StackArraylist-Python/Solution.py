class ArrayListADT:
    def __init__(self):
        self.data = []
        self.size = len(self.data)
        self.capacity = 10
    
    def add(self, e):
        if self.size == self.capacity:
            self.ensure_capacity(self.capacity * 2)
        self.data.append(e)
        self.size += 1
        return True
    
    def size_(self):
        return self.size
    
    def get(self, i):
        return self.data[i]
    
    def ensure_capacity(self, capacity):
        if len(self.data) < capacity:
            for i in range(capacity - len(self.data)):
                self.add(None)
        self.capacity = capacity
    
    def is_empty(self):
        return self.size == 0
    
    def remove_at(self, index):
        first = self.data[:index]
        last = self.data[index + 1:]
        item = self.data[index]
        self.data = first + last
        self.size -= 1
        return item

    def remove(self, obj):
        for i in range(self.size):
            if self.data[i] == obj:
                self.data = self.data[:i] + self.data[i+1:]
                self.size -= 1
                return True
        return False
    
class Stack:
    def __init__(self):
        self.stack = ArrayListADT()
    
    def empty(self):
        return self.stack.size_() == 0
    
    def peek(self):
        if not self.empty():
            return self.stack.get(self.stack.size_() - 1)
        else:
            raise IndexError
        
    def pop(self):
        if not self.empty():
            r = self.stack.get(self.stack.size_() - 1)
            self.stack.remove_at(self.stack.size_() - 1)
            return r
        else:
            raise IndexError
    
    def push(self, item):
        self.stack.add(item)
        return self.stack.get(self.stack.size_() - 1)
    
    def search(self, o):
        for i in range(self.stack.size_()):
            if self.stack.get(self.stack.size_() - 1 - i) == o:
                return i + 1
        return -1
