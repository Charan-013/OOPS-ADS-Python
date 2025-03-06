class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size
    
    def add(self, s):
        node = Node(s)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1

    def add_first(self,s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1
    
    def contains(self,s):
        c = self.head
        while c is not None:
            if c.data == s:
                return True
            c = c.next
        return False
    
    def get_first(self):
        if self.head != None:return self.head.data
    
    def get_last(self):
        if self.tail != None:return self.tail.data
    
    def remove(self):
        if self.head != None:
            temp = self.head.data
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            self._size -= 1
            return temp
        else: return
        
    
    def remove_last(self):
        if self.tail is not None:
            temp = self.tail.data
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self._size -= 1
            return temp
        return None
        
    def get(self, idx):
        if self._size < idx or idx < 0:
            return
        current = self.head
        count = 0
        while current is not None:
            if count == idx:
                return current.data
            current = current.next
            count += 1
        return
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        
    def __str__(self):
        if self.head == None:
            return f"DoublyLinkedList is empty"
        c = self.head
        s = ""
        for i in range(self.size()):
            s += f"[{c.data}]<->"
            c = c.next
        return f"{s[:-3]}"