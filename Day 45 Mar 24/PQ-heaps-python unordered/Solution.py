class BinaryHeapPriorityQueue:
    def __init__(self):
        self.queue = []
        self.size_ = 0
    
    def add(self,e):
        self.queue.append(e)
        self.size_ += 1

    def offer(self,e):
        self.queue.append(e)
        self.size_ += 1
    
    def clear(self):
        self.queue = []
        self.size_  = 0

    def contains(self,o):
        if o in self.queue:
            return True
        return False
    
    def iterator(self):
        return iter(sorted(self.queue))

    def peek(self):
        if len(self.queue) < 1:
            return
        highest_priority = min(self.queue)
        return highest_priority
    
    def poll(self):
        if len(self.queue) < 1:
            return
        highest_priority = min(self.queue)
        self.queue.remove(highest_priority)
        self.size_ -= 1
        return highest_priority
    
    def remove(self,o):
        if len(self.queue) < 1:
            return
        for ele in self.queue[::]:
            if ele == o:
                self.queue.remove(ele)
                return True
        return False
    
    def size(self):
        return self.size_