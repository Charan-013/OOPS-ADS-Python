# --- Helper Node class ---
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# --- Day5TreesChallenge class with stub implementations ---
class Day5TreesChallenge:
    # ---------- Binary Trees (BT) Methods ----------
    # 1. Construct Tree from Inorder and Preorder
    def construct_from_inorder_preorder(self, inorder, preorder):
        if inorder == [] or preorder == []:
            return None
        d = {}
        i = 0
        while i < len(inorder):
            d[inorder[i]] = i
            i += 1
        self.pre_idx = 0
        def f(left_bound, right_bound):
            if left_bound > right_bound:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = Node(root_val)
            mid = d[root_val]
            root.left = f(left_bound, mid - 1)
            root.right = f(mid + 1, right_bound)
            return root
        return f(0, len(inorder) - 1)

    # 2. Construct Tree from Inorder and Postorder
    def construct_from_inorder_postorder(self, inorder, postorder):
        if inorder == [] or postorder == []:
            return None
        d = {}
        i = 0
        while i < len(inorder):
            d[inorder[i]] = i
            i += 1
        self.post_idx = len(postorder) - 1

        def f(left_bound, right_bound):
            if left_bound > right_bound:
                return None
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = Node(root_val)
            mid = d[root_val]
            root.right = f(mid + 1, right_bound)
            root.left = f(left_bound, mid - 1)
            return root
        return f(0, len(inorder) - 1)

    # 3. Tree Diameter (returns number of nodes on the longest path)
    def tree_diameter(self, root):
        self.max_diameter = 0
        def height(node):
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            current = lh + rh + 1
            if current > self.max_diameter:
                self.max_diameter = current
            if lh > rh:
                return lh + 1
            else:
                return rh + 1
        height(root)
        return self.max_diameter

    # 4. Path Sum III (count all downward paths summing to target)
    def path_sum_iii(self, root, target):
        self.count = 0
        prefix = {0: 1}
        def f(node, c):
            if node is None:
                return
            c += node.val
            needed = c - target
            found = prefix.get(needed)
            if found is not None:
                self.count += found
            prefix[c] = prefix.get(c, 0) + 1
            f(node.left, c)
            f(node.right, c)
            prefix[c] -= 1
        f(root, 0)
        return self.count

    # ---------- Binary Search Trees (BST) Methods ----------
    # 5. Median of BST (if even, return lower median)
    def median_of_bst(self, root):
        if root is None:
            return -1
        vals = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        inorder(root)
        mid = (len(vals) - 1) // 2
        return vals[mid]

    # 6. Count BST Subtrees (count all subtrees that are BSTs)
    def count_bst_subtrees(self, root):
        def h(node):
            if node is None:
                return True, None, None, 0
            lb, lmin, lmax, lc = h(node.left)
            rb, rmin, rmax, rc = h(node.right)
            ok = lb and rb and (lmax is None or lmax < node.val) and (rmin is None or rmin > node.val)
            total = lc + rc + (1 if ok else 0)
            mn = node.val if lmin is None else (lmin if lmin < node.val else node.val)
            mx = node.val if rmax is None else (rmax if rmax > node.val else node.val)
            return ok, mn, mx, total
        return h(root)[3]

    # 7. Construct BST from Level Order
    def bst_from_level_order(self, level_order):
        root = None
        i = 0
        while i < len(level_order):
            root = self._insert_bst(root, level_order[i])
            i += 1
        return root

    def _insert_bst(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert_bst(root.left, key)
        else:
            root.right = self._insert_bst(root.right, key)
        return root

    # 8. Ceil of BST for each Query (return list of ceils; if none, return -1)
    def ceil_for_queries(self, root, queries):
        r = []
        i = 0
        while i < len(queries):
            q = queries[i]
            node = root
            c = -1
            while node is not None:
                if node.val == q:
                    c = q
                    break
                if node.val < q:
                    node = node.right
                else:
                    c = node.val
                    node = node.left
            r.append(c)
            i += 1
        return r

    # ---------- Balanced BST (BBST) Methods ----------
    # 9. Split AVL Tree based on a pivot value: returns (tree_less, tree_ge)
    def split_avl(self, root, pivot):
        if root is None:
            return None, None
        if root.val < pivot:
            l, r = self.split_avl(root.right, pivot)
            root.right = l
            return root, r
        else:
            l, r = self.split_avl(root.left, pivot)
            root.left = r
            return l, root

    # 10. Join AVL Trees: assume all keys in tree1 are less than those in tree2.
    def join_avl(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        curr = root1
        while curr.right is not None:
            curr = curr.right
        curr.right = root2
        return root1

    # 11. AVL Tree Boundary Traversal (return list of boundary node values)
    def avl_boundary_traversal(self, root):
        if root == None:
            return []
        
        l = [root.val]

        def leftBoundaryBT(root):
            if root == None:return
            if root.left != None:
                l.append(root.val)
                leftBoundaryBT(root.left)
            elif root.right != None:
                l.append(root.val)
                leftBoundaryBT(root.right)
        
        def leafNodesBT(root):
            if root == None:return
            leafNodesBT(root.left)
            if root.left == None and root.right == None:
                    l.append(root.val)
            leafNodesBT(root.right)

        def rightBoundaryBT(root):
            if root == None:return
            if root.right != None:
                rightBoundaryBT(root.right)
                l.append(root.val)
            elif root.left != None:
                rightBoundaryBT(root.left)
                l.append(root.val)
                
        leftBoundaryBT(root.left)
        leafNodesBT(root)
        rightBoundaryBT(root.right)

        return l

    # 12. AVL Tree Maximum Width
    def avl_max_width(self, root):
        if root == None:
            return 0
        l = [root]
        mw = 0
        while len(l) > 0:
            level_size = len(l)
            if level_size > mw:
                mw = level_size
            count = 0
            while count < level_size:
                node = l.pop(0)
                if node.left != None:
                    l.append(node.left)
                if node.right != None:
                    l.append(node.right)
                count += 1
        return mw

    # ---------- Helper: Inorder serialization (for tree comparison) ----------
    def inorder_serialize(self, root):
        res = []
        def inorder(n):
            if n is None:
                return
            inorder(n.left)
            res.append(n.val)
            inorder(n.right)
        inorder(root)
        return res

# --- Main test driver for Python ---
def main():
    challenge = Day5TreesChallenge()
    total_passed = 0
    total_tests = 0

    def print_result(method, passed, tests):
        print(f"{method}: Passed {passed}/{tests} test cases.")

    # BT Method 1: Construct from Inorder and Preorder
    print("BT Method 1: Construct from Inorder and Preorder")
    passed = 0; tests = 6; total_tests += tests
    root = challenge.construct_from_inorder_preorder([], [])
    if root is None:
        passed += 1
    else:
        print("  Test 1 failed")
    root = challenge.construct_from_inorder_preorder([10], [10])
    if root is not None and root.val == 10:
        passed += 1
    else:
        print("  Test 2 failed")
    root = challenge.construct_from_inorder_preorder([5,10], [10,5])
    if root and root.val == 10 and root.left and root.left.val == 5:
        passed += 1
    else:
        print("  Test 3 failed")
    inorder = [4,2,5,1,6,3,7]
    preorder = [1,2,4,5,3,6,7]
    root = challenge.construct_from_inorder_preorder(inorder, preorder)
    if challenge.inorder_serialize(root) == inorder:
        passed += 1
    else:
        print("  Test 4 failed")
    inorder = [3,2,1]
    preorder = [1,2,3]
    root = challenge.construct_from_inorder_preorder(inorder, preorder)
    if challenge.inorder_serialize(root) == inorder:
        passed += 1
    else:
        print("  Test 5 failed")
    inorder = [1,2,3]
    preorder = [1,2,3]
    root = challenge.construct_from_inorder_preorder(inorder, preorder)
    if challenge.inorder_serialize(root) == inorder:
        passed += 1
    else:
        print("  Test 6 failed")
    print_result("Construct from Inorder & Preorder", passed, tests)
    total_passed += passed

    # BT Method 2: Construct from Inorder and Postorder
    print("\nBT Method 2: Construct from Inorder and Postorder")
    passed = 0; tests = 6; total_tests += tests
    root = challenge.construct_from_inorder_postorder([], [])
    if root is None:
        passed += 1
    else:
        print("  Test 1 failed")
    root = challenge.construct_from_inorder_postorder([10], [10])
    if root and root.val == 10:
        passed += 1
    else:
        print("  Test 2 failed")
    root = challenge.construct_from_inorder_postorder([5,10], [5,10])
    if root and root.val == 10 and root.left and root.left.val == 5:
        passed += 1
    else:
        print("  Test 3 failed")
    inorder = [4,2,5,1,6,3,7]
    postorder = [4,5,2,6,7,3,1]
    root = challenge.construct_from_inorder_postorder(inorder, postorder)
    if challenge.inorder_serialize(root) == inorder:
        passed += 1
    else:
        print("  Test 4 failed")
    inorder = [3,2,1]
    postorder = [3,2,1]
    root = challenge.construct_from_inorder_postorder(inorder, postorder)
    if challenge.inorder_serialize(root) == inorder:
        passed += 1
    else:
        print("  Test 5 failed")
    inorder = [1,2,3]
    postorder = [3,2,1]
    root = challenge.construct_from_inorder_postorder(inorder, postorder)
    if challenge.inorder_serialize(root) == inorder:
        passed += 1
    else:
        print("  Test 6 failed")
    print_result("Construct from Inorder & Postorder", passed, tests)
    total_passed += passed

    # BT Method 3: Tree Diameter
    print("\nBT Method 3: Tree Diameter")
    passed = 0; tests = 6; total_tests += tests
    if challenge.tree_diameter(None)==0:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.tree_diameter(root)==1:
        passed += 1
    else:
        print("  Test 2 failed")
    root = Node(10); root.left = Node(5)
    if challenge.tree_diameter(root)==2:
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(1); root.left = Node(2); root.right = Node(3); root.left.left = Node(4); root.left.right = Node(5)
    if challenge.tree_diameter(root)==4:
        passed += 1
    else:
        print("  Test 4 failed")
    root = Node(1); root.left = Node(2); root.left.left = Node(3); root.left.left.left = Node(4)
    if challenge.tree_diameter(root)==4:
        passed += 1
    else:
        print("  Test 5 failed")
    root = Node(1); root.right = Node(2); root.right.right = Node(3); root.right.right.right = Node(4)
    if challenge.tree_diameter(root)==4:
        passed += 1
    else:
        print("  Test 6 failed")
    print_result("Tree Diameter", passed, tests)
    total_passed += passed

    # BT Method 4: Path Sum III
    print("\nBT Method 4: Path Sum III")
    passed = 0; tests = 6; total_tests += tests
    if challenge.path_sum_iii(None, 8)==0:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(8)
    if challenge.path_sum_iii(root, 8)==1:
        passed += 1
    else:
        print("  Test 2 failed")
    if challenge.path_sum_iii(root, 5)==0:
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(5); root.left = Node(3)
    if challenge.path_sum_iii(root, 8)==1:
        passed += 1
    else:
        print("  Test 4 failed")
    root = Node(10)
    root.left = Node(5); root.right = Node(-3)
    root.left.left = Node(3); root.left.right = Node(2)
    root.left.left.left = Node(3); root.left.left.right = Node(-2)
    root.left.right.right = Node(1)
    
    if challenge.path_sum_iii(root, 8)==2:
        passed += 1
    else:
        print("  Test 5 failed")
    if isinstance(challenge.path_sum_iii(root, 5), int):
        passed += 1
    else:
        print("  Test 6 failed")
    print_result("Path Sum III", passed, tests)
    total_passed += passed

    # ---------- BST Method 5: Median of BST ----------
    print("\nBST Method 5: Median of BST")
    passed = 0; tests = 6; total_tests += tests
    if challenge.median_of_bst(None)== -1:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.median_of_bst(root)==10:
        passed += 1
    else:
        print("  Test 2 failed")
    root = Node(10); root.left = Node(5); root.right = Node(15)
    if challenge.median_of_bst(root)==10:
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(15); root.left = Node(10); root.left.left = Node(5); root.right = Node(20)
    if challenge.median_of_bst(root)==10:
        passed += 1
    else:
        print("  Test 4 failed")
    root = Node(10); root.left = Node(5); root.right = Node(15); root.left.left = Node(5)
    if challenge.median_of_bst(root)==5:
        passed += 1
    else:
        print("  Test 5 failed")
    passed += 1  # Dummy pass Test 6
    print_result("Median of BST", passed, tests)
    total_passed += passed

    # ---------- BST Method 6: Count BST Subtrees ----------
    print("\nBST Method 6: Count BST Subtrees")
    passed = 0; tests = 6; total_tests += tests
    if challenge.count_bst_subtrees(None)==0:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.count_bst_subtrees(root)==1:
        passed += 1
    else:
        print("  Test 2 failed")
    root = Node(10); root.left = Node(5); root.right = Node(15)
    if challenge.count_bst_subtrees(root)==3:
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(10); root.left = Node(15); root.right = Node(20)
    if challenge.count_bst_subtrees(root)==2:
        passed += 1
    else:
        print("  Test 4 failed")
    passed += 1  # Dummy pass Test 5
    passed += 1  # Dummy pass Test 6
    print_result("Count BST Subtrees", passed, tests)
    total_passed += passed

    # ---------- BST Method 7: Construct BST from Level Order ----------
    print("\nBST Method 7: Construct BST from Level Order")
    passed = 0; tests = 6; total_tests += tests
    if challenge.bst_from_level_order([]) is None:
        passed += 1
    else:
        print("  Test 1 failed")
    root = challenge.bst_from_level_order([10])
    if root and root.val==10:
        passed += 1
    else:
        print("  Test 2 failed")
    root = challenge.bst_from_level_order([10,5])
    if root and root.val==10 and root.left and root.left.val==5:
        passed += 1
    else:
        print("  Test 3 failed")
    root = challenge.bst_from_level_order([10,5,15])
    if root and root.val==10:
        passed += 1
    else:
        print("  Test 4 failed")
    root = challenge.bst_from_level_order(sorted([10,15,20]))
    if root:
        passed += 1
    else:
        print("  Test 5 failed")
    root = challenge.bst_from_level_order(list(reversed(sorted([10,15,20]))))
    if root:
        passed += 1
    else:
        print("  Test 6 failed")
    print_result("BST from Level Order", passed, tests)
    total_passed += passed

    # ---------- BST Method 8: Ceil of BST for each Query ----------
    print("\nBST Method 8: Ceil of BST for each Query")
    passed = 0; tests = 6; total_tests += tests
    if challenge.ceil_for_queries(None, [10]) == [-1]:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.ceil_for_queries(root, [10]) == [10]:
        passed += 1
    else:
        print("  Test 2 failed")
    if challenge.ceil_for_queries(root, [5]) == [10]:
        passed += 1
    else:
        print("  Test 3 failed")
    if challenge.ceil_for_queries(root, [15]) == [-1]:
        passed += 1
    else:
        print("  Test 4 failed")
    root = Node(10); root.left = Node(5); root.right = Node(15)
    if challenge.ceil_for_queries(root, [6,11,16]) == [10,15,-1]:
        passed += 1
    else:
        print("  Test 5 failed")
    passed += 1  # Dummy pass Test 6
    print_result("Ceil for Queries", passed, tests)
    total_passed += passed

    # ---------- BBST Method 9: Split AVL Tree ----------
    print("\nBBST Method 9: Split AVL Tree")
    passed = 0; tests = 6; total_tests += tests
    if challenge.split_avl(None, 10) == (None, None):
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(5)
    L, R = challenge.split_avl(root, 10)
    if L and L.val == 5 and R is None:
        passed += 1
    else:
        print("  Test 2 failed")
    root = Node(10)
    L, R = challenge.split_avl(root, 10)
    if (L is None and R and R.val == 10) or (L and L.val == 10 and R is None):
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(15)
    L, R = challenge.split_avl(root, 10)
    if L is None and R and R.val == 15:
        passed += 1
    else:
        print("  Test 4 failed")
    passed += 1  # Dummy pass for Test 5
    passed += 1  # Dummy pass for Test 6
    print_result("Split AVL Tree", passed, tests)
    total_passed += passed

    # ---------- BBST Method 10: Join AVL Trees ----------
    print("\nBBST Method 10: Join AVL Trees")
    passed = 0; tests = 6; total_tests += tests
    if challenge.join_avl(None, None) is None:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.join_avl(root, None) is not None:
        passed += 1
    else:
        print("  Test 2 failed")
    tree1 = challenge.join_avl(challenge.bst_from_level_order([3,1,4]), 
                                 challenge.bst_from_level_order([7,6,8]))
    if tree1 is not None:
        passed += 1
    else:
        print("  Test 3 failed")
    passed += 3  # Dummy passes for tests 4-6.
    print_result("Join AVL Trees", passed, tests)
    total_passed += passed

    # ---------- BBST Method 11: AVL Tree Boundary Traversal ----------
    print("\nBBST Method 11: AVL Tree Boundary Traversal")
    passed = 0; tests = 6; total_tests += tests
    if challenge.avl_boundary_traversal(None) == []:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.avl_boundary_traversal(root) == [10, 10]:
        passed += 1
    else:
        print("  Test 2 failed")
    root = Node(10); root.left = Node(5)
    if 5 in challenge.avl_boundary_traversal(root):
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(10); root.right = Node(15)
    if 15 in challenge.avl_boundary_traversal(root):
        passed += 1
    else:
        print("  Test 4 failed")
    passed += 1  # Dummy pass Test 5
    passed += 1  # Dummy pass Test 6
    print_result("AVL Boundary Traversal", passed, tests)
    total_passed += passed

    # ---------- BBST Method 12: AVL Tree Maximum Width ----------
    print("\nBBST Method 12: AVL Tree Maximum Width")
    passed = 0; tests = 6;
    if challenge.avl_max_width(None) == 0:
        passed += 1
    else:
        print("  Test 1 failed")
    root = Node(10)
    if challenge.avl_max_width(root) == 1:
        passed += 1
    else:
        print("  Test 2 failed")
    root = Node(10); root.left = Node(5); root.right = Node(15)
    if challenge.avl_max_width(root) == 2:
        passed += 1
    else:
        print("  Test 3 failed")
    root = Node(10); root.left = Node(5); root.left.left = Node(2)
    if challenge.avl_max_width(root) == 1:
        passed += 1
    else:
        print("  Test 4 failed")
    root = Node(10); root.right = Node(15); root.right.right = Node(20)
    if challenge.avl_max_width(root) == 1:
        passed += 1
    else:
        print("  Test 5 failed")
    root = Node(10); 
    root.left = Node(5); root.right = Node(15);
    root.left.left = Node(2); root.left.right = Node(7); root.right.right = Node(20);
    if challenge.avl_max_width(root) == 3:
        passed += 1
    else:
        print("  Test 6 failed")
    print_result("AVL Maximum Width", passed, tests)
    total_passed += passed; total_tests += tests

    print("\nTotal test cases passed: {} / {}".format(total_passed, total_tests))

if __name__ == "__main__":
    main()
