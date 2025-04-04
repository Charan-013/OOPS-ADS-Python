
from Solution import BinarySearchTree, Node

tree = BinarySearchTree()
tree.add(7)
tree.add(5)
tree.add(4)
tree.add(10)
tree.add(6)
tree.add(8)

print("inOrder:")
tree.in_order()

print("preOrder:")
tree.pre_order()

print("max:", tree.max())
print("size:", tree.size())

print("contains 6:", tree.contains(6))
print("contains 112:", tree.contains(112))
print("contains 7:", tree.contains(7))
print("contains 10:", tree.contains(10))
