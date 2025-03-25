def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


class BinaryHeapPriorityQueue:
    def __init__(self):
        self.queue = []
        self.size_ = 0
    
    def add(self,e):
        self.queue.append(e)
        self.queue = quick_sort(self.queue)
        self.size_ += 1

    def offer(self,e):
        self.queue.append(e)
        self.queue = quick_sort(self.queue)
        self.size_ += 1
    
    def clear(self):
        self.queue = []
        self.size_  = 0

    def contains(self,o):
        if o in self.queue:
            return True
        return False
    
    def iterator(self):
        return iter(self.queue)

    def peek(self):
        if len(self.queue) < 1:
            return
        return self.queue[0]
    
    def poll(self):
        if len(self.queue) < 1:
            return
        r = self.queue[0]
        self.queue = self.queue[1:]
        self.size_ -= 1
        return r
    
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