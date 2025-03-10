from typing import Generic, TypeVar, List, Optional, Collection
T = TypeVar('T')

class IllegalArgumentException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NoSuchElementException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class UnsupportedOperationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class Deque(Generic[T]):
    def __init__(self):
        self.head = None
        self.front = None
        self.end = None
        self._size = 0
    
    def is_empty(self):
        return self.head == None and self._size == 0
    
    def size(self):
        return self._size
    
    def add_first(self,item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.front = node
            self.end = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            self.head.next.prev = node
            self.front = self.head
        self._size += 1
        return True
            
    def add_last(self,item):
        node = Node(item)
        if self.end == None:
            self.head = node
            self.front = node
            self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node
        self._size = self._size + 1
        return True

    def remove_first(self):
        if self.size() == 0:
            return "Deque is empty"
        r = self.front
        if self.head != None and self.head.next != None:
            self.head = self.head.next
            self.head.prev = None
            self.front = self.head
            self._size = self._size - 1
        else:
            self.head = None
            self.end = None
            self.front = None
        if r != None:
            return r.item
    
    def remove_last(self):
        if self.size() == 0:
            return "Deque is empty"
        r = self.end
        if self.end != None:
            if self.end.prev != None:
                self.end = self.end.prev
                self.end.next = None
            else:
                self.head = None
                self.end = None
                self.front = None
            self._size = self._size - 1
        if r != None:
            return r.item
    
    def iterator(self):
        s = []
        c = self.head
        while c != None:
            s.append(c.item)
            c = c.prev
        return s

    def __str__(self):
        if self.size() == 0:
            return "Deque is empty"
        s = ""
        c = self.head
        while c != None:
            s += f"{c.item}, "
            c = c.next
        return s[:-2]
    
    def reverse(self):
        s = ""
        c = self.end
        while c != None:
            s += f"{c.item}, "
            c = c.prev
        return s[:-2]
    
def main():
    m = {"Integer": int , "String": str, "Double": float}
    try:
        while True:
            inp = input()
            if not inp:
                break
            inp = inp.split(" ")
            if len(inp) == 2 and inp[0] == "Deque()":
                type_safe = None
                if inp[1] in m:
                    for k,v in m.items():
                        if k == inp[1]:
                            type_safe = v
                            break

                deque = Deque[type_safe]()
            
            if inp[0] == "isEmpty()":
                a = deque.is_empty()
                if a == True:
                    print("true")
                else:
                    print("false")

            elif inp[0] == "size()":
                a = deque.size()
                print(a)

            elif inp[0] == "addFirst()":
                a = deque.add_first(inp[1])
            elif inp[0] == "addLast()":
                a = deque.add_last(inp[1])
            elif inp[0] == "removeFirst()":
                a = deque.remove_first()
                print(a)
            elif inp[0] == "removeLast()":
                a = deque.remove_last()
                print(a)
            elif inp[0] == "toString()":
                a = deque
                print(deque)
            elif inp[0] == "iterator()":
                print(deque.iterator())
            # print(deque)
            # print(deque.reverse())
    except EOFError:
        pass

main()

        

