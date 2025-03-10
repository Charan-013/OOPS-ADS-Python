class Node:
	def __init__(self,item):
		self.item = item
		self.next = None

class Stack:
	def __init__(self):
		self.head = None  # Assume head as top of stack

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

	def __str__(self):
		c = self.head
		s = ""
		while c != None:
			s += f"{c.item}"
			c = c.next
		return s

def hasBalancedParentheses(s):
	text = str(s)
	stack = Stack()
	for ele in text:
		if ele == "(":
			stack.push(s)
		elif ele == ")":
			if stack.empty():
				return False
			stack.pop()
	return stack.empty()

print(hasBalancedParentheses(input()))