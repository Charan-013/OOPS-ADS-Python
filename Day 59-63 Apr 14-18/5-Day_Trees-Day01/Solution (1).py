# Assume the student provides the implementations for all the methods below.
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

# ---------- Binary Trees (BT) Methods ----------

def boundary_traversal(root):
    # STUDENT IMPLEMENTATION HERE
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
            if root.val not in l:
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

def vertical_order_traversal(root):
    # STUDENT IMPLEMENTATION HERE
    if root == None:
        return []
    l = [(root,0)]
    vm = {}
    while l:
        n,dis = l.pop(0)
        if dis in vm:
            vm[dis].append(n.val)
        else:
            vm[dis] = [n.val]

        if n.left:
            l.append((n.left,dis - 1))
        if n.right:
            l.append((n.right,dis + 1))
    new = []
    for k in sorted(vm.keys()):
        new.append(vm[k])
    return new

def bottom_view(root):
    # STUDENT IMPLEMENTATION HERE
    if root == None:
        return []
    l = [(root,0)]
    hm = {}
    while l:
        n,hd = l.pop(0)
        hm[hd] = n.val

        if n.left:
            l.append((n.left,hd-1))
        if n.right:
            l.append((n.right,hd+1))
    new = []
    for k in sorted(hm.keys()):
        new.append(hm[k])
    return new

def sum_at_kth_level(root, k):  
    # STUDENT IMPLEMENTATION HERE
    def levelOrder(root,lev,r):
        if root == None:return
        if len(r)<=lev: 
            r.append([])

        r[lev].append(root.val)

        levelOrder(root.left,lev + 1,r)
        levelOrder(root.right,lev + 1,r)
    lev = []
    levelOrder(root,lev=0,r=lev)
    if lev != None and k < len(lev):
        return sum(lev[k])
    else:
        return 0

# ---------- Binary Search Trees (BST) Methods ----------

def is_full_bst(root):
    # STUDENT IMPLEMENTATION HERE
    if not root :return True
    if root.left == None and root.right == None:
        return True
    if root.left and root.right:
        return is_full_bst(root.left) and is_full_bst(root.right)
    return False

def second_largest(root):
    # STUDENT IMPLEMENTATION HERE
    l = inorder_traversal(root)
    l.sort()
    if len(l) >= 2:
        return l[-2]

def floor_ceil(root, key):
    # STUDENT IMPLEMENTATION HERE
    l = inorder_traversal(root)
    if root != None and root.val == key:
        return (root.val,key)
    lt = [ele for ele in l if ele < key]
    gt = [ele for ele in l if ele > key]
    floor = -1
    ceil = -1
    if len(lt) >= 1:
        floor = lt[-1]
    if len(gt) >= 1:
        ceil = gt[0]
    return (floor,ceil)
    # Return tuple: (floor, ceil) with -1 for none.
    return (-1, -1)

def count_nodes_in_range(root, low, high):
    # STUDENT IMPLEMENTATION HERE
    l = inorder_traversal(root)
    count = 0
    for i in range(len(l)):
        if low <= l[i] <= high:
            count += 1
    return count

# ---------- Balanced BST (BBST) Methods ----------

def construct_balanced_bst(sorted_array):
    # STUDENT IMPLEMENTATION HERE
    newBST = BST()
    for ele in sorted_array:
        newBST.add(ele)
    return newBST.root

def is_avl(root):
    # STUDENT IMPLEMENTATION HERE
    if not root :return True
    if root.left == None and root.right == None:
        return True
    if root.left and root.right:
        return is_avl(root.left) and is_avl(root.right)
    return False

def delete_from_avl(root, key):
    # STUDENT IMPLEMENTATION HERE
    l = inorder_traversal(root)
    newBST = BST()
    if key in l:
        l.remove(key)
    for ele in l:
        newBST.add(ele)

    return newBST.root

def convert_to_balanced_bst(root):
    # STUDENT IMPLEMENTATION HERE
    l = inorder_traversal(root)
    newBST = BST()
    for ele in l:
        newBST.add(ele)
    return newBST.root

# ---------- Utility Function ----------
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# ---------- Test Functions ----------

def test_boundary_traversal():
    print("Testing Boundary Traversal:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = boundary_traversal(root)
    expected = []
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = boundary_traversal(root)
    expected = [1]
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Tree with both left & right children
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4); root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = boundary_traversal(root)
    expected = [1,2,4,5,6,3]
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Only left subtree
    #   1
    #  /
    # 2
    #/
    #3
    root = TreeNode(1)
    root.left = TreeNode(2); root.left.left = TreeNode(3)
    result = boundary_traversal(root)
    expected = [1,2,3]
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Only right subtree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2); root.right.right = TreeNode(3)
    result = boundary_traversal(root)
    # (Assuming right boundary is returned in reverse order)
    expected = [1,3,2]
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Boundary Traversal Passed", passed, "/5 tests\n")

def test_vertical_order_traversal():
    print("Testing Vertical Order Traversal:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = vertical_order_traversal(root)
    expected = []
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = vertical_order_traversal(root)
    expected = [[1]]
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4); root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = vertical_order_traversal(root)
    expected = [[4], [2], [1,5], [3], [6]]
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Left skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2); root.left.left = TreeNode(3)
    result = vertical_order_traversal(root)
    expected = [[3], [2], [1]]
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Right skewed tree
    root = TreeNode(1)
    root.right = TreeNode(2); root.right.right = TreeNode(3)
    result = vertical_order_traversal(root)
    expected = [[1], [2], [3]]
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Vertical Order Traversal Passed", passed, "/5 tests\n")

def test_bottom_view():
    print("Testing Bottom View:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = bottom_view(root)
    expected = []
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = bottom_view(root)
    expected = [1]
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3:
    #         20
    #        /  \
    #       8    22
    #      / \     \
    #     5   3     25
    #        / \
    #       10 14
    root = TreeNode(20)
    root.left = TreeNode(8); root.right = TreeNode(22)
    root.left.left = TreeNode(5); root.left.right = TreeNode(3)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10); root.left.right.right = TreeNode(14)
    result = bottom_view(root)
    expected = [5,10,3,14,25]
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Left skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2); root.left.left = TreeNode(3)
    result = bottom_view(root)
    expected = [3,2,1]
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Right skewed tree
    root = TreeNode(1)
    root.right = TreeNode(2); root.right.right = TreeNode(3)
    result = bottom_view(root)
    expected = [1,2,3]
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Bottom View Passed", passed, "/5 tests\n")

def test_sum_at_kth_level():
    print("Testing Sum of Nodes at Kth Level:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = sum_at_kth_level(root, 2)
    expected = 0
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node (level 0)
    root = TreeNode(5)
    result = sum_at_kth_level(root, 0)
    expected = 5
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Two-level tree
    #      1
    #     / \
    #    2   3
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    result = sum_at_kth_level(root, 1)
    expected = 5  # 2+3
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Deeper tree
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    result = sum_at_kth_level(root, 2)
    expected = 4
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Non-existent level
    result = sum_at_kth_level(root, 5)
    expected = 0
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Sum of Nodes at Kth Level Passed", passed, "/5 tests\n")

def test_is_full_bst():
    print("Testing Check if BST is Full:")
    passed = 0
    # Test 1: Empty tree (assume True)
    root = None
    result = is_full_bst(root)
    expected = True
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = is_full_bst(root)
    expected = True
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Full BST:  2 / \ 1 3
    root = TreeNode(2)
    root.left = TreeNode(1); root.right = TreeNode(3)
    result = is_full_bst(root)
    expected = True
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Not full BST: 2 with left child only
    root = TreeNode(2)
    root.left = TreeNode(1)
    result = is_full_bst(root)
    expected = False
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Larger tree with a missing child
    root = TreeNode(4)
    root.left = TreeNode(2); root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.left.right = TreeNode(15)
    root.right.left = TreeNode(5); root.right.right = TreeNode(7)
    result = is_full_bst(root)
    expected = False
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Check if BST is Full Passed", passed, "/5 tests\n")

def test_second_largest():
    print("Testing Second Largest Element:")
    passed = 0
    # Test 1: One node
    root = TreeNode(10)
    result = second_largest(root)
    expected = None
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Two nodes: 10 -> 20
    root = TreeNode(10)
    root.right = TreeNode(20)
    result = second_largest(root)
    expected = 10
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Multiple nodes
    #      20
    #     /  \
    #   10   30
    #           \
    #            40
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root.right.right = TreeNode(40)
    result = second_largest(root)
    expected = 30
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Largest has left subtree
    #      20
    #     /
    #   10
    #     \
    #     15
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.right = TreeNode(15)
    result = second_largest(root)
    expected = 15
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Largest with left subtree candidate
    #      20
    #     /  \
    #   10   30
    #         /
    #        25
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root.right.left = TreeNode(25)
    result = second_largest(root)
    expected = 25
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Second Largest Element Passed", passed, "/5 tests\n")

def test_floor_ceil():
    print("Testing Floor and Ceil of a Value:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = floor_ceil(root, 15)
    expected = (-1, -1)
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node equals key
    root = TreeNode(15)
    result = floor_ceil(root, 15)
    expected = (15, 15)
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Key between nodes
    #       20
    #      /  \
    #    10    30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    result = floor_ceil(root, 25)
    expected = (20, 30)
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Key less than smallest
    result = floor_ceil(root, 5)
    expected = (-1, 10)
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Key greater than largest
    result = floor_ceil(root, 35)
    expected = (30, -1)
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Floor and Ceil of a Value Passed", passed, "/5 tests\n")

def test_count_nodes_in_range():
    print("Testing Count Nodes within Range:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = count_nodes_in_range(root, 10, 20)
    expected = 0
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node inside range
    root = TreeNode(15)
    result = count_nodes_in_range(root, 10, 20)
    expected = 1
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Single node outside range
    root = TreeNode(25)
    result = count_nodes_in_range(root, 10, 20)
    expected = 0
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Larger tree
    #         20
    #        /  \
    #      10   30
    #     /  \
    #    5   15
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root.left.left = TreeNode(5); root.left.right = TreeNode(15)
    result = count_nodes_in_range(root, 10, 20)
    expected = 3  # (10,15,20)
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: All nodes in range
    result = count_nodes_in_range(root, 0, 40)
    expected = 5
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Count Nodes within Range Passed", passed, "/5 tests\n")

def test_construct_balanced_bst():
    print("Testing Construct Balanced BST from Sorted Array:")
    passed = 0
    # Test 1: Empty array
    arr = []
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == []:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single element
    arr = [10]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [10]:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Two elements
    arr = [5,10]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [5,10]:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Multiple elements
    arr = [1,2,3,4,5,6,7]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [1,2,3,4,5,6,7]:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Non continuous sorted array
    arr = [2,5,8,10,13]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [2,5,8,10,13]:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Construct Balanced BST Passed", passed, "/5 tests\n")

def test_is_avl():
    print("Testing AVL Tree Check:")
    passed = 0
    # Test 1: Empty tree
    root = None
    if is_avl(root) == True:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(10)
    if is_avl(root) == True:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Balanced BST
    #      10
    #     /  \
    #    5   15
    root = TreeNode(10)
    root.left = TreeNode(5); root.right = TreeNode(15)
    if is_avl(root) == True:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Unbalanced tree
    #      10
    #     /
    #    5
    #   /
    #  2
    root = TreeNode(10)
    root.left = TreeNode(5); root.left.left = TreeNode(2)
    if is_avl(root) == False:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Complex unbalanced tree
    #      30
    #     /
    #   20
    #     \
    #     25
    root = TreeNode(30)
    root.left = TreeNode(20); root.left.right = TreeNode(25)
    if is_avl(root) == False:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("AVL Tree Check Passed", passed, "/5 tests\n")

def test_delete_from_avl():
    print("Testing Delete Node from AVL Tree:")
    passed = 0
    # Test 1: Delete from empty tree
    root = None
    root = delete_from_avl(root, 10)
    if root is None:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Delete a leaf node
    #      20
    #     /  \
    #   10   30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root = delete_from_avl(root, 10)
    if inorder_traversal(root) == [20,30]:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Delete root node with two children
    #      20
    #     /  \
    #   10   30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root = delete_from_avl(root, 20)
    if inorder_traversal(root) == [10,30]:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Delete node causing unbalance
    #      30
    #     /  \
    #   20   40
    #   /
    # 10
    root = TreeNode(30)
    root.left = TreeNode(20); root.right = TreeNode(40)
    root.left.left = TreeNode(10)
    root = delete_from_avl(root, 40)
    if inorder_traversal(root) == [10,20,30]:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Delete non-existent node
    root = TreeNode(30)
    root.left = TreeNode(20); root.right = TreeNode(40)
    original = inorder_traversal(root)
    root = delete_from_avl(root, 50)
    if inorder_traversal(root) == original:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Delete Node from AVL Tree Passed", passed, "/5 tests\n")

def test_convert_to_balanced_bst():
    print("Testing Convert BST to Balanced BST:")
    passed = 0
    # Test 1: Empty tree
    root = None
    root = convert_to_balanced_bst(root)
    if root is None:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Already balanced tree
    #      20
    #     /  \
    #   10   30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(root) == inorder_traversal(balanced):
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Unbalanced tree conversion
    #      10
    #        \
    #        20
    #          \
    #          30
    root = TreeNode(10)
    root.right = TreeNode(20); root.right.right = TreeNode(30)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(balanced) == [10,20,30]:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Larger unbalanced tree
    arr = [1,2,3,4,5,6,7,8,9]
    root = construct_balanced_bst(arr)
    # Unbalance: attach extra node to rightmost branch
    temp = root
    while temp.right:
        temp = temp.right
    temp.right = TreeNode(10)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(balanced) == [1,2,3,4,5,6,7,8,9,10]:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: BST with duplicate values
    arr = [1,2,2,3,4]
    root = construct_balanced_bst(arr)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(balanced) == [1,2,2,3,4]:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Convert BST to Balanced BST Passed", passed, "/5 tests\n")

if __name__ == "__main__":
    test_boundary_traversal()
    test_vertical_order_traversal()
    test_bottom_view()
    test_sum_at_kth_level()
    test_is_full_bst()
    test_second_largest()
    test_floor_ceil()
    test_count_nodes_in_range()
    test_construct_balanced_bst()
    test_is_avl()
    test_delete_from_avl()
    test_convert_to_balanced_bst()

