class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def add_first(self, s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self._size += 1

    def contains(self, s):
        current = self.head
        while current is not None:
            if current.data == s:
                return True
            current = current.next
        return False

    def get(self, idx):
        count = 0
        current = self.head
        while count <= idx and current.next != None:
            current = current.next
        return current.data

    def get_first(self):
        if self.head != None:
            return self.head.data

    def get_last(self):
        if self.tail != None:
            return self.tail.data

    def size(self):
        return self._size

    def remove(self):
        if self.head != None:
            temp = self.head.data
            self.head = self.head.next
            self._size -= 1
            return temp
        else: return

    def remove_last(self):
        if self.head == None:
            return 
        
        if self.head == self.tail:
            temp = self.tail.data
            self.head = None
            self.tail = None
            self._size = self._size - 1
            return temp

        current = self.head
        while current.next != self.tail:
            current = current.next

        temp = self.tail.data
        self.tail = current
        self.tail.next = None
        self._size = self._size - 1
        return temp

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        if self.head == None:
            return "LinkedList is empty"
        s = ""
        current = self.head
        while current is not None:
            s += f"[{current.data}]"
            current = current.next
        return f"{s}"
