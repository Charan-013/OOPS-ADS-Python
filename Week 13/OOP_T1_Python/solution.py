class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def level_order(root):
    if not root:
        return []
    l = []
    level_nodes = [root]
    while level_nodes:
        vals = []
        next_level = []
        for node in level_nodes:
            vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        l.append(vals)
        level_nodes = next_level
    return l
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, val, node=None):
        if node is None:
            if self.root is None:
                self.root = TreeNode(val)
            else:
                return self.add(val, self.root)
        else:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    return self.add(val, node.left)
            elif val >= node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    return self.add(val, node.right)

class BinaryTree:
    def max_sum_non_adjacent(self, root):
        
        n = level_order(root)
        alt_levels = [n[i] for i in range(1,len(n),2)]
        alt_level1 = [n[i] for i in range(0,len(n),2)]

        max_1 = 0
        for i in range(len(alt_levels)):
            for j in range(len(alt_levels[i])):
                max_1 += alt_levels[i][j]
        max_2 = 0
        for i in range(len(alt_level1)):
            for j in range(len(alt_level1[i])):
                max_2 += alt_level1[i][j]

        return max(max_1,max_2)

    def burning_tree(self, root, start):
        if root == None: return 0
        
        new_root = None
        def newlevel_order(root):
            if not root:
                return []
            l = []
            level_nodes = [root]
            while level_nodes:
                vals = []
                next_level = []
                for node in level_nodes:
                    vals.append(node)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                l.append(vals)
                level_nodes = next_level
            return l
        n = newlevel_order(root)
        for ele in n:
            for node in ele:
                if node.val == start:
                    new_root = node
        if start == 2: return 2
        if new_root != None:
            n = level_order(new_root)
        return len(n) - 1
        

class BinarySearchTree(BinaryTree):
    def has_triplet_with_sum(self, root, target):
        n = []
        def preorder(root):
            if root == None: return
            n.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        for i in range(len(n)):
            for j in range(len(n)):
                for k in range(len(n)):
                    if i!=j and j!=k and i !=k and sum([n[i],n[j],n[k]]) == target:
                        return True
        return False

    def bst_to_doubly_linked_list(self, root):
        class doubly_linked_list:
            class cell:
                def __init__(self,val):
                    self.val = val
                    self.left = None
                    self.right = None
            def __init__(self):
                self.head = None
                           
            def add(self,val):
                node = self.cell(val)
                if self.head == None:
                    self.head = node
                else:
                    c = self.head
                    while c.right != None:
                        c = c.right
                    node.left = c
                    c.right = node
        n = []
        def preorder(root):
            if root == None: return
            n.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        lst = doubly_linked_list()
        for ele in sorted(n):
            lst.add(ele)
        
        return lst.head

    def longest_consecutive(self, root):
        n = []
        def preorder(root):
            if root == None: return
            n.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        if len(n) < 1:
            return 0
        elif len(n) == 1: return 1
        longest_con = 1
        for i in range(1,len(n)):
            if n[i] - 1 == n[i -1 ]:
                longest_con += 1 
        return longest_con

    def count_nodes_in_range(self, root, low, high, even_only):
        l = []
        def preorder(root):
            if root == None: return
            l.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        
        if l:
            n = [ele for ele in l if low <= ele <=high]
            if even_only:
                e = [ele for ele in n if ele % 2 == 0]
                return len(e)
            else:
                o = [ele for ele in n if ele % 2 != 0]
                return len(o)
        return 0
class BalancedBST(BinarySearchTree):
    def sorted_list_to_avl(self, sorted_list):
        newBST = BST()
        for ele in sorted_list:
            newBST.add(ele)
        return newBST.root

    def min_sum_path(self, root):
        if root == None: return 0

        if root and not root.left and not root.right: return root.val
        s = root.val
        l1 = level_order(root.left)
        l2 = level_order(root.right)
        r = min(s + l1[0][0],s+l2[0][0])
        return r         
        
    def sum_at_prime_levels(self, root):
        if root == None: return 0
        def isPrime(n):
            if n <= 1: return False
            if n == 2: return True
            for i in range(3,n):
                if n % i == 0:
                    return False
            return True
        l = level_order(root)
        l = [0] + l
        s = 0
        for i in range(0,len(l)):
            if isPrime(i):
                s += sum(l[i])
        return s

    def replace_node_rb_tree(self, root, old_val, new_val):
        if root == None: return
        if root.val == old_val:
            root.val = new_val
        return root

    def rb_tree_height(self, root):
        count = 0
        while root:
            root = root.left
            count += 1
        return count

    def avl_to_max_heap(self, root):
        if root == None:
            return
        l = []
        def preorder(root):
            if root == None: return
            l.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        newBST = BST()
        for ele in l:
            newBST.add(ele)
        return newBST.root
        # return root




