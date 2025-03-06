class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_front(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size = self.size + 1

    def add_to_end(self, data):
        node = Node(data)
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size = self.size + 1

    def remove_from_front(self):
        if self.head != None and self.head.next != None:
            self.head = self.head.next
            self.head.prev = None
            self.size = self.size - 1
        else:
            self.head = None
            self.tail = None

    def remove_from_end(self):
        if self.tail != None:
            if self.tail.prev != None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.size = self.size - 1

    def find(self, value):
        c = self.head
        while c != None:
            if c.value == value:
                return True
            c = c.next
        return False

    def check_empty(self):
        if self.head == None:
            return True
        return False

    def get_size(self):
        return self.size

    def insert_at(self, i, value):
        if i < 0 or i > self.size:
            return
        if i == 0:
            self.add_to_front(value)
        elif i == self.size:
            self.add_to_end(value)
        else:
            node = Node(value)
            c = self.head
            for n in range(i - 1):
                c = c.next
            node.next = c.next
            if c.next:
                c.next.prev = node
            c.next = node
            node.prev = c
            self.size += 1

    def get_at(self, i):
        if i < 0 or i >= self.size:
            return
        c = self.head
        for n in range(i):
            if c == None:
                return
            c = c.next
        return c.value

    def get_node_at(self, i):
        if i < 0 or i >= self.size:
            return
        c = self.head
        for n in range(i):
            if c == None:
                return
            c = c.next
        return c

    def remove_at(self, i):
        if i < 0 or i >= self.size:
            return
        if i == 0:
            self.remove_from_front()
        elif i == self.size - 1:
            self.remove_from_end()
        else:
            c = self.head
            for n in range(i):
                c = c.next
            c.prev.next = c.next
            if c.next:
                c.next.prev = c.prev
            self.size -= 1

    def reverse_traversal(self):
        current = self.tail
        while current:
            print(current.value, end=" ")
            current = current.prev
        print()

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def clear_list(self):
        self.head = None
        self.tail = None
        self.size = 0

    def swap_nodes(self, i1, i2):
        if i1 == i2:
            return
        n1 = self.get_node_at(i1)
        n2 = self.get_node_at(i2)
        if n1 == None or n2 == None:
            return
        n1.value, n2.value = n2.value, n1.value
        return True

    def detect_cycle(self):
        n1 = self.head
        n2 = self.head
        while n2 != None and n2.next != None:
            n1 = n1.next
            n2 = n2.next.next
            if n1 == n2:
                return True
        return False

