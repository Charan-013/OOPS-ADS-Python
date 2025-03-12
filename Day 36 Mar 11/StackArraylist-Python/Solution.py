class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head == None
    
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
    
    def push(self,item):
        node = Node(item)
        if self.empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head.item

    def search(self,o):
        c = self.head
        count = -1
        while c != None:
            if c.item == o:
                return count + 2
            else:
                count += 1
            c = c.next
        return count

            