from functools import cmp_to_key

class Heap:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    def add(self,e):
        self.minHeap.append(e)
        self.maxHeap.append(e)
        # self.queue1 = sorted(self.queue1)
        self.bubble_up(self.size() - 1)
        self.bubble_up_min(self.size() - 1)

    
    def remove(self,o):
        if o in self.minHeap and o in self.maxHeap:
            idx = self.minHeap.index(o)
            idx1 = self.maxHeap.index(o)
            self.minHeap[idx] = self.minHeap[-1]
            self.minHeap.pop()
            self.maxHeap[idx] = self.maxHeap[-1]
            self.maxHeap.pop()
            # try:
            #     # self.bubble_down(idx)
            #     # self.bubble_up(idx)
            # except IndexError:
            #     pass
            return o
        return o
    
    def size(self):
        return len(self.minHeap)
    
    def bubble_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.maxHeap[idx] > self.maxHeap[parent]:
            self.maxHeap[idx], self.maxHeap[parent] = self.maxHeap[parent], self.maxHeap[idx]
            idx = parent
            parent = (idx - 1) // 2
    
    def bubble_down(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx
        
        if left_child < len(self.maxHeap) and self.maxHeap[left_child] > self.maxHeap[smallest]:
            smallest = left_child
        if right_child < len(self.maxHeap) and self.maxHeap[right_child] > self.maxHeap[smallest]:
            smallest = right_child
        
        if smallest != idx:
            self.maxHeap[idx], self.maxHeap[smallest] = self.maxHeap[smallest], self.maxHeap[idx]
            self.bubble_down(smallest)

    def bubble_up_min(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.minHeap[idx] < self.minHeap[parent]:
            self.minHeap[idx], self.minHeap[parent] = self.minHeap[parent], self.minHeap[idx]
            idx = parent
            parent = (idx - 1) // 2
    
    def bubble_down_min(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx
        
        if left_child < len(self.minHeap) and self.minHeap[left_child] < self.minHeap[smallest]:
            smallest = left_child
        if right_child < len(self.minHeap) and self.minHeap[right_child] < self.minHeap[smallest]:
            smallest = right_child
        
        if smallest != idx:
            self.minHeap[idx], self.minHeap[smallest] = self.minHeap[smallest], self.minHeap[idx]
            self.bubble_down(smallest)


class DynamicMeanFinder:
    def __init__(self):
        self.list = Heap()

    def size(self):
        return self.list.size()
    
    def insert(self,item):
        self.list.add(item)
        # self.list = sorted(self.list.q,key=cmp_to_key(Item.compare))

    def find_median(self):
        if self.size() % 2 == 0:
            median = min(self.list.minHeap[0],self.list.maxHeap[0])
            return median
        else:
            if len(self.list.minHeap) < len(self.list.maxHeap):
                return self.list.minHeap[0]
            else:
                return self.list.maxHeap[0]

        # if self.size() % 2 == 0:
        #     median_one = (self.size()) // 2
        #     median_two = ((self.size()) // 2) - 1
        #     median = min(self.list.queue1[median_one],self.list.queue1[median_two])
        #     return median
        # else:
        #     median_idx = (self.size()) // 2
        #     median = self.list.queue1[median_idx]
        #     return median

    def remove_median(self):
        r = self.find_median()
        removed = self.list.remove(r)
        return removed

    
def main():
    treasurer = DynamicMeanFinder()
    try:
        while True:
            inp = input()

            if not inp:
                break
            inp = inp.split(" ")
            
            if inp[0] == "I":
                treasurer.insert(int(inp[1]))

            elif treasurer.size() == 0 and (inp[0] == "M" or inp[0] == "R"):
                print(f"Invalid")
            else:
                if inp[0] == "M":
                    m =treasurer.find_median()
                    print(m)
                    
                if inp[0] == "R":
                    removed_median = treasurer.remove_median()
                    print(removed_median)
    except EOFError:
        pass
main()