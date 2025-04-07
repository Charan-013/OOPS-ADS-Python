# Define the Node class used by both BinaryTree and BinarySearchTree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BinaryTree with methods: levelOrder, isComplete, countLeaves, and pathSum.
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # 1. Level Order Traversal: returns list of lists of node values per level.
    def levelOrder(self):
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if isinstance(node,list):
                l = []
                for ele in node:
                    l.append(ele.val)
                result.append(l)
            else:
                result.append([node.val])
            if isinstance(node,Node):
                if node.left and node.right:
                    queue.append([node.left,node.right])
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return result
        

    # 2. Check Completeness: returns True if the tree is complete.
    def isComplete(self):
        result = []
        if not self.root:
            return True
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for ele in result:
            if ele.left == None and ele.right == None:
                continue
            elif ele.left != None and ele.right != None:
                continue
            elif ele.left == None and ele.right != None:
                return False
            elif ele.left != None and ele.right == None:
                continue
        return True
        

    # 3. Count Leaf Nodes: returns the number of leaf nodes.
    def countLeaves(self):
        def leafList(t = self.root):
            if t == None: return []
            if t.left == None and t.right == None:
                return [t.val]
            return leafList(t.left) + leafList(t.right)
        
        return len(leafList(self.root))
        # Todo

    # 4. Root-to-Leaf Path Sum: returns True if a root-to-leaf path equals target sum.
    def pathSum(self, target):
        result = []
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if sum(result) == target:
                return True
            if sum(result[:1]+result[1::2]) == target or sum(result[:1]+result[2::2]) == target:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sum(result) == target
            
        

# BinarySearchTree (inherits from BinaryTree) with methods: validateBST, rangeSearch, balance.
class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    # 5. Validate BST: returns True if the tree satisfies BST properties.
    def validateBST(self):
        x = self.root
        if not x :
            return True
        
        def _val(x,root,sidefromroot = None):
            if not x:
                return True
            if x.left:
                if x.left.val > x.val:
                    return False
                if x.left.val < x.val and sidefromroot == "right":
                    return False
            if x.right:
                if x.right.val < x.val:
                    return False
                if x.right.val > x.val and sidefromroot == "left":
                    return False
            
            return _val(x.left,root,"left") and _val(x.right,root,"right")

        return _val(x,root = self.root)

    # 6. Range Search: returns a sorted list of node values within [low, high].
    def rangeSearch(self, low, high):

        def _keys( x, result, lo, hi):
            if x == None:
                return
            if lo < x.val:
                _keys(x.left, result, lo, hi)
            if lo <= x.val <= hi:
                result.append(x.val)
            if hi > x.val:
                _keys(x.right, result, lo, hi)
        result = []
        _keys(self.root, result, low, high)
        return result

    # 7. Balance BST: rebuilds the tree so that it is balanced.
    def balance(self):
        def add(val, node=None):
            if node is None:
                if self.root is None:
                    self.root = Node(val)
                else:
                    return self.add(val, self.root)
            else:
                if val < node.val:
                    if node.left is None:
                        node.left = Node(val)
                    else:
                        return self.add(val, node.left)
                elif val > node.val:
                    if node.right is None:
                        node.right = Node(val)
                    else:
                        return self.add(val, node.right)
        def nodes():            
            result = []
            if not self.root:
                return result
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                result.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return result
        
        def get_height(node):
            if node is None:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        if get_height(self.root) == 1:
            return
        else:
            list_of_nodes = nodes()
            copy = self.root
            self.root = None
            for ele in list_of_nodes:
                add(ele.val,ele)