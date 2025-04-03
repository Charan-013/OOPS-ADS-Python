class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

# 1. copy: Return a deep copy of the tree.
def copy_tree(t):
    if t == None:return None
    return BTNode(t.data, copy_tree(t.left), copy_tree(t.right))

# 2. replace: Replace all occurrences of old_value with new_value.
#    Return the count of nodes replaced.
def replace(t, old_value, new_value):
    if t == None:return 0
    count = 0
    if t.data == old_value:
        t.data = new_value
        count += 1
    count += replace(t.left, old_value, new_value)
    count += replace(t.right, old_value, new_value)
    return count

# 3. countNodesAtDepth: Count the number of nodes at the given depth.
def countNodesAtDepth(t, depth):
    if t == None: return 0
    if depth == 0: return 1
    return countNodesAtDepth(t.left, depth - 1) + countNodesAtDepth(t.right, depth - 1)

# 4. allSame: Return True if every value in the tree is the same.
def allSame(t, value=None):
    if t == None: return True
    if value == None:
        value = t.data
    return t.data == value and allSame(t.left, value) and allSame(t.right, value)

# 5. leafList: Return a list of the data values in the leaves of the tree.
def leafList(t):
    if t == None: return []
    if t.left == None and t.right == None:
        return [t.data]
    return leafList(t.left) + leafList(t.right)

# 6. reflect: Modify the tree so that it is reflected horizontally.
def reflect(t):
    if t == None: return
    t.left, t.right = t.right, t.left
    reflect(t.left)
    reflect(t.right)

# 7. condense: Remove nodes with exactly one child.
def condense(t):
    if t == None: return None
    if t.left == None and t.right == None:
        return t
    if t.left == None:
        return condense(t.right)
    if t.right == None:
        return condense(t.left)
    t.left = condense(t.left)
    t.right = condense(t.right)
    return t

# Function to perform pre-order traversal of the tree.
def print_preorder(t):
    if t == None: return
    print(t.data, end=" ")
    print_preorder(t.left)
    print_preorder(t.right)
