def inorder_traversal(root):
    # Returns a list of node values from an inorder traversal.
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def zigzag_traversal(self, root):
        """
        Perform a zigzag (spiral order) traversal of the binary tree.
        
        Args:
            root (Node): The root node of the tree.
            
        Returns:
            List[List[int]]: List of lists of node values per level in zigzag order.
        """
        # TODO: Implement zigzag traversal.

        return []
        

    def max_width(self, root):
        """
        Compute the maximum width (max number of nodes at any level) of the tree.
        
        Args:
            root (Node): The root node.
            
        Returns:
            int: The maximum width.
        """
        # TODO: Implement maximum width computation.
        return 0

    def diameter(self, root):
        """
        Compute the diameter of the tree (the longest path between any two nodes).
        
        Args:
            root (Node): The root node.
            
        Returns:
            int: The diameter (node count or edge count as per design).
        """
        # TODO: Implement diameter calculation.
        return 0

    def lowest_common_ancestor(self, root, val1, val2):
        """
        Find the lowest common ancestor (LCA) of two nodes by value.
        
        Args:
            root (Node): The root node.
            val1 (int): The value of the first node.
            val2 (int): The value of the second node.
            
        Returns:
            Node or None: The LCA node, or None if one or both values are not present.
        """
        # TODO: Implement lowest common ancestor finder.
        pass

class BinarySearchTree(BinaryTree):                
    def kth_smallest(self, root, k):
        """
        Find the kth smallest element in the BST using in-order traversal.
        
        Args:
            root (Node): The root node of the BST.
            k (int): The kth order statistic.
            
        Returns:
            int: The kth smallest element's value, or -1 if k is out of bounds.
        """
        # TODO: Implement kth smallest finder.
        r = []
        s = []
        node = root
        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            r.append(node.val)
            node = node.right
        if k > len(r):
            return -1
        return r[k-1]

    def inorder_successor(self, root, target):
        """
        Find the inorder successor of a given target node in the BST.
        
        Args:
            root (Node): The root of the BST.
            target (Node): The target node.
            
        Returns:
            Node or None: The inorder successor node, or None if none exists.
        """
        # TODO: Implement inorder successor finder.
        r = []
        s = []
        node = root
        while s or node:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            r.append(node.val)
            node = node.right
        n = []
        for ele in r:
            if ele not in n:
                n.append(ele)
        i = 0
        if target.val in n:
            i = n.index(target.val) + 1
            
            if i >= len(n):
                return
            return Node(n[i])
        return

    def merge_trees(self, root1, root2):
        """
        Merge two BSTs into a new BST that maintains BST properties.
        
        Args:
            root1 (Node): The root of the first BST.
            root2 (Node): The root of the second BST.
            
        Returns:
            Node or None: The root of the merged BST.
        """
        # TODO: Implement merging of two BSTs.
        def inorder_traversal(root):
            # Returns a list of node values from an inorder traversal.
            if not root:
                return []
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

        bst1_data = inorder_traversal(root1)
        bst2_data = inorder_traversal(root2)
        new = bst1_data + bst2_data
        bst_new = new_BST()
        for ele in new:
            bst_new.add(ele)
        return bst_new.root

    def find_closest_value(self, root, target):
        """
        Find the value in the BST that is closest to the given target value.
        
        Args:
            root (Node): The root of the BST.
            target (int): The target value.
            
        Returns:
            int: The closest value found, or -1 if the tree is empty.
        """
        # TODO: Implement closest value search.
        def inorder_traversal(root):
            # Returns a list of node values from an inorder traversal.
            if not root:
                return []
            return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
        l = inorder_traversal(root)
        l = sorted(l)
        if target in l: return target

        lt = [ele for ele in l if ele < target]
        gt = [ele for ele in l if ele > target]
        lt = sorted(lt)
        gt = sorted(gt)
        if lt == []:
            return gt[0]
        elif gt == []  and lt != []:
            return lt[-1]
        elif target - lt[-1] > gt[0] - target:
            return gt[0]
        elif target - lt[-1] < gt[0] - target:
            return lt[-1]
        else:
            return min(lt[-1],gt[0])

class BalancedBST(BinarySearchTree):
    def split_bst(self, root, key):
        """
        Split the balanced BST into two BSTs by a pivot key.
        
        Args:
            root (Node): The root of the BST.
            key (int): The pivot key.
            
        Returns:
            Tuple[Node or None, Node or None]: (tree_less, tree_greater_or_equal)
        """
        # TODO: Implement BST split preserving balance.
        l = inorder_traversal(root)
        lt = [ele for ele in l if ele < key]
        gt = [ele for ele in l if ele > key]
        tree_less = new_BST()
        tree_ge = new_BST()
        for ele in lt:
            tree_less.add(ele)
        for ele in gt:
            tree_ge.add(ele)

        return (tree_less.root, tree_ge.root)

    def join_bst(self, root1, root2):
        """
        Join two balanced BSTs into one balanced BST.
        Assumes every element in root1 is less than every element in root2.
        
        Args:
            root1 (Node): The first BST root.
            root2 (Node): The second BST root.
            
        Returns:
            Node or None: The root of the joined balanced BST.
        """
        # TODO: Implement joining of two balanced BSTs.
        lt = inorder_traversal(root1)
        gt = inorder_traversal(root2)
        new = lt + gt
        join_bst = new_BST()
        for ele in new:
            join_bst.add(ele)
        return join_bst.root

    def find_median(self, root):
        """
        Find the median element in the balanced BST.
        (May require augmentation such as storing subtree sizes.)
        
        Args:
            root (Node): The root of the BST.
            
        Returns:
            int: The median value, or -1 if the tree is empty.
        """
        # TODO: Implement median finder.
        l = inorder_traversal(root)
        l = sorted(l)
        length = len(l)
        if length == 0:
            return -1
        elif length == 1:
            return l[0]
        if length % 2 != 0:
            return l[length//2]
        else:
            return l[length//2 -1]

    def range_sum_query(self, root, low, high):
        """
        Compute the sum of all node values within the inclusive range [low, high].
        (May use augmented subtree sum values for efficiency.)
        
        Args:
            root (Node): The root of the BST.
            low (int): The lower bound.
            high (int): The upper bound.
            
        Returns:
            int: The sum of values in the specified range.
        """
        # TODO: Implement range sum query.
        l = inorder_traversal(root)
        new = [ele for ele in l if low <= ele <= high]
        if len(new) == 0:
            return 0
        elif len(new) == 1:
            return new[0]
        else:
            return sum(new)

class new_BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def add(self, val, node=None):
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
            elif val >= node.val:
                if node.right is None:
                    node.right = Node(val)
                else:
                    return self.add(val, node.right)
            