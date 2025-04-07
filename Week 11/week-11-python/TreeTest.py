
from Solution import Node, BinaryTree, BinarySearchTree

# --------------------- Testing ---------------------
def test_levelOrder():
    print("Testing levelOrder method")
    passed = 0

    # Test 1: Empty tree.
    tree = BinaryTree()
    if tree.levelOrder() == []:
        passed += 1
    else:
        print("levelOrder test 1 failed")

    # Test 2: Single node tree.
    tree = BinaryTree(Node(10))
    if tree.levelOrder() == [[10]]:
        passed += 1
    else:
        print("levelOrder test 2 failed")

    # Test 3: Two nodes: root and left child.
    root = Node(1)
    root.left = Node(2)
    tree = BinaryTree(root)
    if tree.levelOrder() == [[1], [2]]:
        passed += 1
    else:
        print("levelOrder test 3 failed")

    # Test 4: Two nodes: root and right child.
    root = Node(1)
    root.right = Node(3)
    tree = BinaryTree(root)
    if tree.levelOrder() == [[1], [3]]:
        passed += 1
    else:
        print("levelOrder test 4 failed")

    # Test 5: Complete tree with three nodes.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    tree = BinaryTree(root)
    if tree.levelOrder() == [[1], [2, 3]]:
        passed += 1
    else:
        print("levelOrder test 5 failed")

    # Test 6: Tree with missing nodes (non-full level).
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(4)
    tree = BinaryTree(root)
    if tree.levelOrder() == [[1], [2], [4]]:
        passed += 1
    else:
        print("levelOrder test 6 failed")

    # Test 7: Left-skewed tree.
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    tree = BinaryTree(root)
    if tree.levelOrder() == [[1], [2], [3]]:
        passed += 1
    else:
        print("levelOrder test 7 failed")

    # Test 8: Right-skewed tree.
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    tree = BinaryTree(root)
    if tree.levelOrder() == [[1], [2], [3]]:
        passed += 1
    else:
        print("levelOrder test 8 failed")

    print(f"levelOrder: {passed}/8 tests passed.\n")

def test_isComplete():
    print("Testing isComplete method")
    passed = 0

    # Test 1: Empty tree (convention: complete).
    tree = BinaryTree()
    if tree.isComplete() == True:
        passed += 1
    else:
        print("isComplete test 1 failed")

    # Test 2: Single node.
    tree = BinaryTree(Node(10))
    if tree.isComplete() == True:
        passed += 1
    else:
        print("isComplete test 2 failed")

    # Test 3: Complete tree with two levels.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    tree = BinaryTree(root)
    if tree.isComplete() == True:
        passed += 1
    else:
        print("isComplete test 3 failed")

    # Test 4: Incomplete tree (node missing in left position at last level).
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    tree = BinaryTree(root)
    if tree.isComplete() == False:
        passed += 1
    else:
        print("isComplete test 4 failed")

    # Test 5: Left-skewed tree (still complete as every level is fully filled until last).
    root = Node(1)
    root.left = Node(2)
    tree = BinaryTree(root)
    if tree.isComplete() == True:
        passed += 1
    else:
        print("isComplete test 5 failed")

    # Test 6: Right-skewed tree (not complete because left child is missing).
    root = Node(1)
    root.right = Node(2)
    tree = BinaryTree(root)
    if tree.isComplete() == False:
        passed += 1
    else:
        print("isComplete test 6 failed")

    # Test 7: Full tree with three levels.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    tree = BinaryTree(root)
    if tree.isComplete() == True:
        passed += 1
    else:
        print("isComplete test 7 failed")

    # Test 8: Almost complete tree missing one node at far right.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = None  # Missing node.
    tree = BinaryTree(root)
    if tree.isComplete() == True:
        passed += 1
    else:
        print("isComplete test 8 failed")

    print(f"isComplete: {passed}/8 tests passed.\n")

def test_countLeaves():
    print("Testing countLeaves method")
    passed = 0

    # Test 1: Empty tree.
    tree = BinaryTree()
    if tree.countLeaves() == 0:
        passed += 1
    else:
        print("countLeaves test 1 failed")

    # Test 2: Single node.
    tree = BinaryTree(Node(10))
    if tree.countLeaves() == 1:
        passed += 1
    else:
        print("countLeaves test 2 failed")

    # Test 3: Two nodes (root and left).
    root = Node(1)
    root.left = Node(2)
    tree = BinaryTree(root)
    if tree.countLeaves() == 1:
        passed += 1
    else:
        print("countLeaves test 3 failed")

    # Test 4: Two nodes (root and right).
    root = Node(1)
    root.right = Node(3)
    tree = BinaryTree(root)
    if tree.countLeaves() == 1:
        passed += 1
    else:
        print("countLeaves test 4 failed")

    # Test 5: Full tree with three nodes.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    tree = BinaryTree(root)
    if tree.countLeaves() == 2:
        passed += 1
    else:
        print("countLeaves test 5 failed")

    # Test 6: Tree with one branch deeper.
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(4)
    tree = BinaryTree(root)
    if tree.countLeaves() == 1:
        passed += 1
    else:
        print("countLeaves test 6 failed")

    # Test 7: Left-skewed tree.
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    tree = BinaryTree(root)
    if tree.countLeaves() == 1:
        passed += 1
    else:
        print("countLeaves test 7 failed")

    # Test 8: Tree with two leaves at different levels.
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    tree = BinaryTree(root)
    if tree.countLeaves() == 2:
        passed += 1
    else:
        print("countLeaves test 8 failed")

    print(f"countLeaves: {passed}/8 tests passed.\n")

def test_pathSum():
    print("Testing pathSum method")
    passed = 0

    # Test 1: Empty tree.
    tree = BinaryTree()
    if tree.pathSum(0) == False:
        passed += 1
    else:
        print("pathSum test 1 failed")

    # Test 2: Single node equals target.
    tree = BinaryTree(Node(5))
    if tree.pathSum(5) == True:
        passed += 1
    else:
        print("pathSum test 2 failed")

    # Test 3: Single node not equal target.
    tree = BinaryTree(Node(5))
    if tree.pathSum(10) == False:
        passed += 1
    else:
        print("pathSum test 3 failed")

    # Test 4: Two-level tree with valid path.
    root = Node(1)
    root.left = Node(2)
    tree = BinaryTree(root)
    if tree.pathSum(3) == True:
        passed += 1
    else:
        print("pathSum test 4 failed")

    # Test 5: Two-level tree with no valid path.
    root = Node(1)
    root.right = Node(2)
    tree = BinaryTree(root)
    if tree.pathSum(5) == False:
        passed += 1
    else:
        print("pathSum test 5 failed")

    # Test 6: Tree with negative values.
    root = Node(-2)
    root.right = Node(-3)
    tree = BinaryTree(root)
    if tree.pathSum(-5) == True:
        passed += 1
    else:
        print("pathSum test 6 failed")

    # Test 7: Multi-level tree with valid path.
    #      5
    #     / \
    #    4   8
    #   /   / \
    # 11   13  4
    # /  \
    #7    2
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(11)
    root.left.left.left = Node(7)
    root.left.left.right = Node(2)
    tree = BinaryTree(root)
    if tree.pathSum(22) == True:
        passed += 1
    else:
        print("pathSum test 7 failed")

    # Test 8: Multi-level tree with no valid path.
    if tree.pathSum(26) == False:
        passed += 1
    else:
        print("pathSum test 8 failed")

    print(f"pathSum: {passed}/8 tests passed.\n")

def test_validateBST():
    print("Testing validateBST method")
    passed = 0

    # Test 1: Empty BST.
    bst = BinarySearchTree()
    if bst.validateBST() == True:
        passed += 1
    else:
        print("validateBST test 1 failed")

    # Test 2: Single node BST.
    bst = BinarySearchTree(Node(10))
    if bst.validateBST() == True:
        passed += 1
    else:
        print("validateBST test 2 failed")

    # Test 3: Proper BST.
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    bst = BinarySearchTree(root)
    if bst.validateBST() == True:
        passed += 1
    else:
        print("validateBST test 3 failed")

    # Test 4: Not BST (left child greater than root).
    root = Node(10)
    root.left = Node(12)
    bst = BinarySearchTree(root)
    if bst.validateBST() == False:
        passed += 1
    else:
        print("validateBST test 4 failed")

    # Test 5: Not BST (right child less than root).
    root = Node(10)
    root.right = Node(8)
    bst = BinarySearchTree(root)
    if bst.validateBST() == False:
        passed += 1
    else:
        print("validateBST test 5 failed")

    # Test 6: Valid BST (skewed left).
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    bst = BinarySearchTree(root)
    if bst.validateBST() == True:
        passed += 1
    else:
        print("validateBST test 6 failed")

    # Test 7: Valid BST (skewed right).
    root = Node(10)
    root.right = Node(15)
    root.right.right = Node(20)
    bst = BinarySearchTree(root)
    if bst.validateBST() == True:
        passed += 1
    else:
        print("validateBST test 7 failed")

    # Test 8: BST violation deep in tree.
    #      10
    #     /  \
    #    5   15
    #       /
    #      6   <-- violation: 6 is not >10
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(6)
    bst = BinarySearchTree(root)
    if bst.validateBST() == False:
        passed += 1
    else:
        print("validateBST test 8 failed")

    print(f"validateBST: {passed}/8 tests passed.\n")

def test_rangeSearch():
    print("Testing rangeSearch method")
    passed = 0

    # Test 1: Empty BST.
    bst = BinarySearchTree()
    if bst.rangeSearch(0, 10) == []:
        passed += 1
    else:
        print("rangeSearch test 1 failed")

    # Test 2: Single node inside range.
    bst = BinarySearchTree(Node(5))
    if bst.rangeSearch(0, 10) == [5]:
        passed += 1
    else:
        print("rangeSearch test 2 failed")

    # Test 3: Single node outside range.
    bst = BinarySearchTree(Node(15))
    if bst.rangeSearch(0, 10) == []:
        passed += 1
    else:
        print("rangeSearch test 3 failed")

    # Test 4: Multiple nodes with some in range.
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    bst = BinarySearchTree(root)
    if bst.rangeSearch(5, 10) == [5, 10]:
        passed += 1
    else:
        print("rangeSearch test 4 failed")

    # Test 5: Range covering all nodes.
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    bst = BinarySearchTree(root)
    if bst.rangeSearch(0, 20) == [5, 10, 15]:
        passed += 1
    else:
        print("rangeSearch test 5 failed")

    # Test 6: Range covering no nodes.
    if bst.rangeSearch(16, 20) == []:
        passed += 1
    else:
        print("rangeSearch test 6 failed")

    # Test 7: Partial range.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    bst = BinarySearchTree(root)
    if bst.rangeSearch(10, 25) == [10, 15, 20]:
        passed += 1
    else:
        print("rangeSearch test 7 failed")

    # Test 8: BST with negative values.
    root = Node(0)
    root.left = Node(-10)
    root.right = Node(10)
    bst = BinarySearchTree(root)
    if bst.rangeSearch(-20, 0) == [-10, 0]:
        passed += 1
    else:
        print("rangeSearch test 8 failed")

    print(f"rangeSearch: {passed}/8 tests passed.\n")

def test_balance():
    print("Testing balance method")
    passed = 0

    # Helper function to get height (for testing purposes)
    def get_height(node):
        if node is None:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    # Test 1: Empty tree.
    bst = BinarySearchTree()
    bst.balance()
    if bst.root is None:
        passed += 1
    else:
        print("balance test 1 failed")

    # Test 2: Single node tree.
    bst = BinarySearchTree(Node(10))
    bst.balance()
    if bst.root and bst.root.val == 10:
        passed += 1
    else:
        print("balance test 2 failed")

    # Test 3: Already balanced tree.
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    bst = BinarySearchTree(root)
    bst.balance()
    if get_height(bst.root) <= 2:
        passed += 1
    else:
        print("balance test 3 failed")

    # Test 4: Unbalanced left heavy tree.
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    bst = BinarySearchTree(root)
    bst.balance()
    if get_height(bst.root) <= 3:
        passed += 1
    else:
        print("balance test 4 failed")

    # Test 5: Unbalanced right heavy tree.
    root = Node(10)
    root.right = Node(15)
    root.right.right = Node(20)
    root.right.right.right = Node(25)
    bst = BinarySearchTree(root)
    bst.balance()
    if get_height(bst.root) <= 3:
        passed += 1
    else:
        print("balance test 5 failed")

    # Test 6: More nodes, random insertion.
    # Build a BST that is unbalanced.
    nums = [50, 30, 20, 40, 70, 60, 80, 10]
    root = Node(nums[0])
    for num in nums[1:]:
        curr = root
        while True:
            if num < curr.val:
                if curr.left is None:
                    curr.left = Node(num)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(num)
                    break
                else:
                    curr = curr.right
    bst = BinarySearchTree(root)
    bst.balance()
    if get_height(bst.root) <= 4:
        passed += 1
    else:
        print("balance test 6 failed")

    # Test 7: Completely skewed tree (left).
    root = Node(10)
    current = root
    for val in [9, 8, 7, 6, 5]:
        current.left = Node(val)
        current = current.left
    bst = BinarySearchTree(root)
    bst.balance()
    if get_height(bst.root) <= 4:
        passed += 1
    else:
        print("balance test 7 failed")

    # Test 8: Completely skewed tree (right).
    root = Node(10)
    current = root
    for val in [11, 12, 13, 14, 15]:
        current.right = Node(val)
        current = current.right
    bst = BinarySearchTree(root)
    bst.balance()
    if get_height(bst.root) <= 4:
        passed += 1
    else:
        print("balance test 8 failed")

    print(f"balance: {passed}/8 tests passed.\n")

def main():
    test_levelOrder()
    test_isComplete()
    test_countLeaves()
    test_pathSum()
    test_validateBST()
    test_rangeSearch()
    test_balance()

main()
