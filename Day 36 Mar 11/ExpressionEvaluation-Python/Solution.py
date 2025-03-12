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


def calculate(op1,operator,op2):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2

def main():
    inp = input().strip()
    stack = Stack()
    i = 0
    n = len(inp)

    while i < n:
        ch = inp[i]
        
        if ch == ")":
            num2 = stack.pop()
            operator = stack.pop()
            num1 = stack.pop()
            stack.pop()
            r = calculate(num1, operator, num2)
            stack.push(r)
        elif ch == "(":
            stack.push(ch)
        elif ch in "+-*/":
            stack.push(ch)
        elif ch == " ":
            pass
        else:
            num = 0
            while i < n and inp[i].isdigit():
                num = num * 10 + float(inp[i])
                i += 1
            stack.push(num)
            continue
        i += 1

    print(stack.pop())

main()