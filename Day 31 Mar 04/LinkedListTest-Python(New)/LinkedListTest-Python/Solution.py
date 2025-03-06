# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def add(self, s):
#         node = Node(s)
#         if self.head == None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.size += 1

#     def add_first(self, s):
#         node = Node(s)
#         if self.head == None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node
#         self.size += 1

#     def contains(self, s):
#         current = self.head
#         while current is not None:
#             if current.data == s:
#                 return True
#             current = current.next
#         return False

#     def get(self, idx):
#         count = 0
#         current = self.head
#         while count <= idx and current.next != None:
#             current = current.next
#         return current.data

#     def get_first(self):
#         if self.head != None:
#             return self.head.data

#     def get_last(self):
#         if self.tail != None:
#             return self.tail.data

#     def size(self):
#         return self.size

#     def remove(self):
#         if self.head != None:
#             temp = self.head.data
#             self.head = self.head.next
#             self.size -= 1
#             return temp
#         else:
#             return

#     def remove_last(self):
#         if self.head == None:
#             return

#         if self.head == self.tail:
#             temp = self.tail.data
#             self.head = None
#             self.tail = None
#             self.size = self.size - 1
#             return temp

#         current = self.head
#         while current.next != self.tail:
#             current = current.next

#         temp = self.tail.data
#         self.tail = current
#         self.tail.next = None
#         self.size = self.size - 1
#         return temp

#     def clear(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     def find_middle(self):
#         s = self.size
#         middle = s // 2
#         current = self.head
#         for i in range(middle):
#             current = current.next
#         return current.data

#     def nth_from_end(self, n):
#         s = self.size
#         if n > s:
#             return
#         num = s - n
#         current = self.head
#         for i in range(num):
#             current = current.next
#         return current.data

#     def insert_at_position(self, idx, s):
#         if idx < 0 or idx > self.size:
#             return
#         node = Node(s)
#         if idx == 0:
#             self.add_first(s)
#         elif idx == self.size:
#             self.add(s)
#         else:
#             current = self.head
#             for i in range(idx - 1):
#                 current = current.next
#             node.next = current.next
#             current.next = node
#             self.size += 1

#     def insert_before(self, s, new):
#         if s != self.head.data:
#             current = self.head
#             while current.next.data != s:
#                 current = current.next
#             temp = current.next
#             current.next = Node(new)
#             current.next.next = temp
#         elif s == self.head.data:
#             self.add_first(new)

#     def delete_after(self, s):
#         current = self.head
#         while current != None and current.data != s:
#             current = current.next
#         if current is not None and current.next is not None:
#             current.next = current.next.next
#             self.size = self.size - 1

#     def to_string(self):
#         if self.head == None:
#             return "LinkedList is empty"
#         s = ""
#         current = self.head
#         while current is not None:
#             s += f"[{current.data}]"
#             current = current.next
#         return f"{s}"

#     def __str__(self):
#         if self.head == None:
#             return "LinkedList is empty"
#         s = ""
#         current = self.head
#         while current is not None:
#             s += f"[{current.data}]"
#             current = current.next
#         return f"{s}"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, s):
        node = Node(s)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def add_first(self, s):
        node = Node(s)
        if self.head == None:
            self.head = node
            self.head.next = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

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
        return self.size

    def remove(self):
        if self.head != None:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp
        else:
            return

    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next
            current.next = None
        self.size -= 1

    def clear(self):
        self.head = None
        self.size = 0

    def find_middle(self):
        s = self.size
        middle = s // 2
        current = self.head
        for i in range(middle):
            current = current.next
        return current.data

    def nth_from_end(self, n):
        s = self.size
        if n > s:
            return
        num = s - n
        current = self.head
        for i in range(num):
            current = current.next
        return current.data

    def insert_at_position(self, idx, s):
        if idx < 0 or idx > self.size:
            return
        node = Node(s)
        if idx == 0:
            self.add_first(s)
        elif idx == self.size:
            self.add(s)
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def insert_before(self, s, new):
        if s != self.head.data:
            current = self.head
            while current.next.data != s:
                current = current.next
            temp = current
            current.next = Node(new)
            current.next.next = temp
        elif s == self.head.data:
            self.add_first(new)

    def delete_after(self, s):
        current = self.head
        while current != None and current.data != s:
            current = current.next
        if current is not None and current.next is not None:
            current.next = current.next.next
            self.size = self.size - 1

    def to_string(self):
        if self.head == None:
            return "LinkedList is empty"
        s = ""
        current = self.head
        for i in range(self.size):
            s += f"[{current.data}]"
            current = current.next
        return f"{s}"

    def __str__(self):
        if self.head == None:
            return "LinkedList is empty"
        s = ""
        current = self.head
        for i in range(self.size):
            s += f"[{current.data}]"
            current = current.next
        return f"{s}"
    