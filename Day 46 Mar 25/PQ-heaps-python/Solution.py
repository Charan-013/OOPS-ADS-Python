class BinaryHeapPriorityQueue:
    def __init__(self):
        self.queue = []
    
    def add(self,e):
        self.queue.append(e)
        self.bubble_up(self.size() - 1)

    def offer(self,e):
        self.add(e)
    
    def clear(self):
        self.queue = []

    def contains(self,o):
        if o in self.queue:
            return True
        return False
    
    def iterator(self):
        return iter(sorted(self.queue))

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None
    
    def poll(self):
        if len(self.queue) < 1:
            return
        root = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.bubble_down(0)
        return root
    
    def remove(self,o):
        if o in self.queue:
            idx = self.queue.index(o)
            self.queue[idx] = self.queue[-1]
            self.queue.pop()
            self.bubble_down(idx)
            self.bubble_up(idx)
            return True
        return False
    
    def size(self):
        return len(self.queue)
    
    def bubble_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.queue[idx] < self.queue[parent]:
            self.queue[idx], self.queue[parent] = self.queue[parent], self.queue[idx]
            idx = parent
            parent = (idx - 1) // 2
    
    def bubble_down(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx
        
        if left_child < len(self.queue) and self.queue[left_child] < self.queue[smallest]:
            smallest = left_child
        if right_child < len(self.queue) and self.queue[right_child] < self.queue[smallest]:
            smallest = right_child
        
        if smallest != idx:
            self.queue[idx], self.queue[smallest] = self.queue[smallest], self.queue[idx]
            self.bubble_down(smallest)
