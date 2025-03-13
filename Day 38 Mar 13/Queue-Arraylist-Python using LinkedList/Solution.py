class Node:
    def __init__(self,element):
        self.element = element
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        node = Node(e)
        if self.head is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def remove_first(self):
        if self.head != None:
            temp = self.head.element
            self.head = self.head.next
            self.size -= 1
            return temp
        else: return

    def __str__(self):
        if self.head == None:
            return "LinkedList is empty"
        s = ""
        current = self.head
        while current is not None:
            s += f"[{current.element}]"
            current = current.next
        return f"{s}"

class MyQueue:
    def __init__(self,queueSize):
        self.queue = SingleLinkedList()
        self.queueSize = queueSize
        self.front = None
        self.back = None

    def add(self,e):
        if self.queueSize <= self.queue.size:
            raise FullQueueException()
        if self.queue.size == 0:
            self.queue.add(e)
            self.front = self.queue.head
            self.back = self.queue.tail
        else:
            self.queue.add(e)
            self.back = self.queue.tail
        return True
    
    def element(self):
        if self.queue.size == 0:
            raise IndexError
        return self.queue.head.element
    
    def offer(self,e):
        if self.queueSize <= self.queue.size:
            return False
        self.queue.add(e)
        self.back = self.queue.tail
        if self.front is None:
            self.front = self.queue.head
        return True
        
    def peek(self):
        if self.queue.size == 0:
            return None
        return self.queue.head.element 
    
    def poll(self):
        if self.queue.size == 0:
            return None
        return self.remove()
    
    def remove(self):
        if self.queue.size == 0:
            raise IndexError
        r = self.queue.remove_first()
        if self.queue.size == 0:
            self.front = self.back = None
        else:
            self.front = self.queue.head
        return r

    
    def __str__(self):
        return f"{str(self.queue)}"
    
class FullQueueException(Exception):
    def __init__(self, *args):
        super().__init__(*args)