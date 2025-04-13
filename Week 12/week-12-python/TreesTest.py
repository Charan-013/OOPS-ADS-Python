
from Solution import *
# --- Helper Functions for Testing ---

def compare_2d_list(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def inorder_traversal(root):
    # Returns a list of node values from an inorder traversal.
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# --- Main Test Suite ---

def main():
    bt = BinaryTree()
    bst = BinarySearchTree()
    balanced = BalancedBST()

    # ========================================================
    # Method 1: Zigzag Traversal (8 test cases)
    # ========================================================
    print("Testing zigzag_traversal:")
    # Test 1: Empty Tree.
    root = None
    expected = []
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 1 " + ("passed" if result == expected else "failed"))

    # Test 2: Single Node Tree.
    root = Node(1)
    expected = [[1]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 2 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # Test 3: Balanced tree with 3 levels.
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    expected = [[1], [3, 2], [4, 5, 6]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 3 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # Test 4: Tree with missing nodes.
    #       1
    #      / 
    #     2   
    #      \
    #       3
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(3)
    expected = [[1], [2], [3]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 4 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # Test 5: Left-skewed tree: 1 -> 2 -> 3 -> 4.
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.left = Node(4)
    expected = [[1], [2], [3], [4]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 5 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # Test 6: Right-skewed tree.
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    expected = [[1], [2], [3], [4]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 6 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # Test 7: Unbalanced tree.
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    #    \
    #     5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.right = Node(5)
    expected = [[1], [3, 2], [4], [5]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 7 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # Test 8: Tree with duplicate values.
    root = Node(1)
    root.left = Node(1)
    root.right = Node(1)
    expected = [[1], [1, 1]]
    result = bt.zigzag_traversal(root)
    print("zigzag_traversal Test 8 " + ("passed" if compare_2d_list(result, expected) else "failed"))

    # ========================================================
    # Method 2: Maximum Width (8 test cases)
    # ========================================================
    print("\nTesting max_width:")
    # Test 1: Empty Tree.
    root = None
    expected = 0
    result = bt.max_width(root)
    print("max_width Test 1 " + ("passed" if result == expected else "failed"))

    # Test 2: Single node.
    root = Node(1)
    expected = 1
    result = bt.max_width(root)
    print("max_width Test 2 " + ("passed" if result == expected else "failed"))

    # Test 3: Perfectly balanced tree.
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    expected = 4
    result = bt.max_width(root)
    print("max_width Test 3 " + ("passed" if result == expected else "failed"))

    # Test 4: Left-skewed tree.
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    expected = 1
    result = bt.max_width(root)
    print("max_width Test 4 " + ("passed" if result == expected else "failed"))

    # Test 5: Right-skewed tree.
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    expected = 1
    result = bt.max_width(root)
    print("max_width Test 5 " + ("passed" if result == expected else "failed"))

    # Test 6: Unbalanced tree with wide level.
    #       1
    #      / \
    #     2   3
    #          \
    #           4
    #          / \
    #         5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.right.left = Node(5)
    root.right.right.right = Node(6)
    expected = 2
    result = bt.max_width(root)
    print("max_width Test 6 " + ("passed" if result == expected else "failed"))

    # Test 7: Multiple maximum levels.
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6
    #          /
    #         7
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.right.left = Node(7)
    expected = 3
    result = bt.max_width(root)
    print("max_width Test 7 " + ("passed" if result == expected else "failed"))

    # Test 8: Tree with duplicate nodes.
    root = Node(1)
    root.left = Node(1)
    root.right = Node(1)
    expected = 2
    result = bt.max_width(root)
    print("max_width Test 8 " + ("passed" if result == expected else "failed"))

    # ========================================================
    # Method 3: Diameter of the Tree (8 test cases)
    # ========================================================
    print("\nTesting diameter:")
    # Test 1: Empty tree.
    root = None
    expected = 0    # assuming diameter as node count
    result = bt.diameter(root)
    print("diameter Test 1 " + ("passed" if result == expected else "failed"))

    # Test 2: Single node.
    root = Node(1)
    expected = 1
    result = bt.diameter(root)
    print("diameter Test 2 " + ("passed" if result == expected else "failed"))

    # Test 3: Balanced tree.
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    expected = 4
    result = bt.diameter(root)
    print("diameter Test 3 " + ("passed" if result == expected else "failed"))

    # Test 4: Unbalanced tree.
    #       1
    #      /
    #     2
    #    /
    #   3
    #    \
    #     4
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    root.left.left.right = Node(4)
    expected = 4
    result = bt.diameter(root)
    print("diameter Test 4 " + ("passed" if result == expected else "failed"))

    # Test 5: Two equally long paths.
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    expected = 5
    result = bt.diameter(root)
    print("diameter Test 5 " + ("passed" if result == expected else "failed"))

    # Test 6: Chain of nodes. 1 -> 2 -> 3 -> 4 -> 5.
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    root.right.right.right.right = Node(5)
    expected = 5
    result = bt.diameter(root)
    print("diameter Test 6 " + ("passed" if result == expected else "failed"))

    # Test 7: Branch in the middle.
    #         1
    #       /   \
    #      2     3
    #       \
    #        4
    #         \
    #          5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    expected = 5
    result = bt.diameter(root)
    print("diameter Test 7 " + ("passed" if result == expected else "failed"))

    # Test 8: Tree with duplicate values.
    root = Node(1)
    root.left = Node(1)
    root.right = Node(1)
    expected = 3
    result = bt.diameter(root)
    print("diameter Test 8 " + ("passed" if result == expected else "failed"))

    # ========================================================
    # Method 4: Lowest Common Ancestor (LCA) (8 test cases)
    # ========================================================
    print("\nTesting lowest_common_ancestor:")
    # Test 1: Both nodes are the same.
    root = Node(1)
    result_node = bt.lowest_common_ancestor(root, 1, 1)
    print("LCA Test 1 " + ("passed" if result_node is not None and result_node.val == 1 else "failed"))

    # Test 2: Simple binary tree.
    #        3
    #       / \
    #      5   1
    #     / \
    #    6   2
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    result_node = bt.lowest_common_ancestor(root, 6, 2)
    print("LCA Test 2 " + ("passed" if result_node is not None and result_node.val == 5 else "failed"))

    # Test 3: One node is ancestor of the other.
    result_node = bt.lowest_common_ancestor(root, 5, 6)
    print("LCA Test 3 " + ("passed" if result_node is not None and result_node.val == 5 else "failed"))

    # Test 4: Nodes in different subtrees.
    result_node = bt.lowest_common_ancestor(root, 6, 1)
    print("LCA Test 4 " + ("passed" if result_node is not None and result_node.val == 3 else "failed"))

    # Test 5: Non-existent node.
    result_node = bt.lowest_common_ancestor(root, 16, 919)
    print("LCA Test 5 " + ("passed" if result_node is None else "failed"))

    # Test 6: Deep tree LCA.
    #         8
    #        /
    #       4
    #      / \
    #     2   6
    #    /   / \
    #   1   5   7
    root = Node(8)
    root.left = Node(4)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.left.left = Node(1)
    root.left.right.left = Node(5)
    root.left.right.right = Node(7)
    result_node = bt.lowest_common_ancestor(root, 1, 7)
    print("LCA Test 6 " + ("passed" if result_node is not None and result_node.val == 4 else "failed"))

    # Test 7: LCA in tree with duplicate values.
    root = Node(1)
    root.left = Node(1)
    root.right = Node(1)
    result_node = bt.lowest_common_ancestor(root, 1, 1)
    print("LCA Test 7 " + ("passed" if result_node is not None and result_node.val == 1 else "failed"))

    # Test 8: LCA where one node is not present.
    result_node = bt.lowest_common_ancestor(root, 1, 99)
    print("LCA Test 8 " + ("passed" if result_node is not None and result_node.val == 1 else "failed"))

    # ========================================================
    # Method 5: kth Smallest Element (BST) (8 test cases)
    # ========================================================
    print("\nTesting kth_smallest:")
    # Test 1: k exceeds tree size.
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    result_int = bst.kth_smallest(root, 5)
    print("kth_smallest Test 1 " + ("passed" if result_int == -1 else "failed"))

    # Test 2: Single node tree.
    root = Node(10)
    result_int = bst.kth_smallest(root, 1)
    print("kth_smallest Test 2 " + ("passed" if result_int == 10 else "failed"))

    # Test 3: Regular BST.
    #         5
    #        / \
    #       3   7
    #      / \   \
    #     2   4   8
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(8)
    result_int = bst.kth_smallest(root, 3)  # Inorder: [2, 3, 4, 5, 7, 8]
    print("kth_smallest Test 3 " + ("passed" if result_int == 4 else "failed"))

    # Test 4: BST with duplicate values.
    # Tree: 5, 3, 3, 7
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(3)
    root.right = Node(7)
    result_int = bst.kth_smallest(root, 2)  # Expected second smallest is 3.
    print("kth_smallest Test 4 " + ("passed" if result_int == 3 else "failed"))

    # Test 5: k = 1 (minimum element).
    result_int = bst.kth_smallest(root, 1)
    print("kth_smallest Test 5 " + ("passed" if result_int == 3 else "failed"))
    # (Assuming duplicates count separately, adjust expected as per your rules.)

    # Test 6: k equals tree size.
    result_int = bst.kth_smallest(root, 4)
    print("kth_smallest Test 6 " + ("passed" if result_int == 7 else "failed"))

    # Test 7: Larger BST.
    #         15
    #        /  \
    #      10    20
    #     /  \
    #    8   12
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    result_int = bst.kth_smallest(root, 3)  # Inorder: [8,10,12,15,20]
    print("kth_smallest Test 7 " + ("passed" if result_int == 12 else "failed"))

    # Test 8: k equals tree size (largest element).
    result_int = bst.kth_smallest(root, 5)
    print("kth_smallest Test 8 " + ("passed" if result_int == 20 else "failed"))

    # ========================================================
    # Method 6: Inorder Successor (BST) (8 test cases)
    # ========================================================
    print("\nTesting inorder_successor:")
    # Test 1: Node with right subtree.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.right.left = Node(25)
    target = root  # target = 20, right subtree exists.
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 1 " + ("passed" if succ is not None and succ.val == 25 else "failed"))

    # Test 2: Node without right subtree.
    target = root.left  # target = 10, no right child.
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 2 " + ("passed" if succ is not None and succ.val == 20 else "failed"))

    # Test 3: Maximum element.
    target = root.right  # target = 30, maximum element.
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 3 " + ("passed" if succ is None else "failed"))

    # Test 4: Single node tree.
    root = Node(40)
    target = root
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 4 " + ("passed" if succ is None else "failed"))

    # Test 5: Complex BST.
    #         15
    #        /  \
    #      10    20
    #     /  \     \
    #    8   12    25
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.right = Node(25)
    target = root.left  # target = 10.
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 5 " + ("passed" if succ is not None and succ.val == 12 else "failed"))

    # Test 6: Target is root with right subtree.
    target = root  # target = 15, successor should be 20.
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 6 " + ("passed" if succ is not None and succ.val == 20 else "failed"))

    # Test 7: Target not in tree.
    target = Node(100)
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 7 " + ("passed" if succ is None else "failed"))

    # Test 8: BST with duplicate values.
    root = Node(10)
    root.left = Node(10)
    root.right = Node(20)
    target = root.left
    succ = bst.inorder_successor(root, target)
    print("inorder_successor Test 8 " + ("passed" if succ is not None and succ.val == 20 else "failed"))

    # ========================================================
    # Method 7: Merge Two BSTs (8 test cases)
    # ========================================================
    print("\nTesting merge_trees:")
    # For merge tests, we'll compare the inorder traversal of the merged tree to expected sorted lists.
    # Test 1: One empty tree.
    tree1 = None
    tree2 = Node(5)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = [5]
    print("merge_trees Test 1 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 2: Both trees non-empty with distinct values.
    tree1 = Node(3)
    tree1.left = Node(1)
    tree1.right = Node(4)
    tree2 = Node(7)
    tree2.left = Node(6)
    tree2.right = Node(8)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([3,1,4,7,6,8])
    print("merge_trees Test 2 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 3: Both trees non-empty with overlapping values.
    tree1 = Node(2)
    tree1.left = Node(1)
    tree2 = Node(2)
    tree2.right = Node(3)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([2,1,2,3])
    print("merge_trees Test 3 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 4: One tree single node, one multi-node.
    tree1 = Node(10)
    tree2 = Node(20)
    tree2.left = Node(15)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([10,20,15])
    print("merge_trees Test 4 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 5: Both trees single nodes.
    tree1 = Node(5)
    tree2 = Node(10)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([5,10])
    print("merge_trees Test 5 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 6: Larger BST merge.
    tree1 = Node(8)
    tree1.left = Node(3)
    tree1.right = Node(10)
    tree2 = Node(15)
    tree2.left = Node(12)
    tree2.right = Node(20)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([8,3,10,15,12,20])
    print("merge_trees Test 6 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 7: Merge where all nodes of one tree are smaller.
    tree1 = Node(1)
    tree1.right = Node(2)
    tree2 = Node(5)
    tree2.left = Node(4)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([1,2,5,4])
    print("merge_trees Test 7 " + ("passed" if inorder_merged == expected else "failed"))

    # Test 8: Merge where all nodes of one tree are larger.
    tree1 = Node(10)
    tree2 = Node(20)
    tree2.left = Node(15)
    merged = bst.merge_trees(tree1, tree2)
    inorder_merged = inorder_traversal(merged)
    expected = sorted([10,20,15])
    print("merge_trees Test 8 " + ("passed" if inorder_merged == expected else "failed"))

    # ========================================================
    # Method 8: Find Closest Value (8 test cases)
    # ========================================================
    print("\nTesting find_closest_value:")
    # Test 1: Exact match present.
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    closest = bst.find_closest_value(root, 10)
    print("find_closest_value Test 1 " + ("passed" if closest == 10 else "failed"))

    # Test 2: Target between two values.
    closest = bst.find_closest_value(root, 7)  # expected: 5 (difference: 2 vs 8)
    print("find_closest_value Test 2 " + ("passed" if closest == 5 else "failed"))

    # Test 3: Target less than minimum.
    closest = bst.find_closest_value(root, 2)  # expected: 5
    print("find_closest_value Test 3 " + ("passed" if closest == 5 else "failed"))

    # Test 4: Target greater than maximum.
    closest = bst.find_closest_value(root, 20)  # expected: 15
    print("find_closest_value Test 4 " + ("passed" if closest == 15 else "failed"))

    # Test 5: Target exactly between two nodes.
    root = Node(10)
    root.right = Node(20)
    closest = bst.find_closest_value(root, 15)  # assume expected: 10 (if lower chosen) or 20; adjust as needed.
    print("find_closest_value Test 5 " + ("passed" if closest == 10 else "failed"))

    # Test 6: Larger BST.
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(17)
    root.right.right = Node(25)
    closest = bst.find_closest_value(root, 13)  # expected: 12
    print("find_closest_value Test 6 " + ("passed" if closest == 12 else "failed"))

    # Test 7: Single node tree.
    root = Node(30)
    closest = bst.find_closest_value(root, 25)
    print("find_closest_value Test 7 " + ("passed" if closest == 30 else "failed"))

    # Test 8: Tree with duplicate values.
    root = Node(10)
    root.left = Node(10)
    root.right = Node(20)
    closest = bst.find_closest_value(root, 12)  # expected: 10
    print("find_closest_value Test 8 " + ("passed" if closest == 10 else "failed"))

    # ========================================================
    # Method 9: Split BST (Balanced BST) (8 test cases)
    # ========================================================
    print("\nTesting split_bst:")
    # Test 1: Empty tree.
    root = None
    tree_less, tree_ge = balanced.split_bst(root, 5)
    print("split_bst Test 1 " + ("passed" if tree_less is None and tree_ge is None else "failed"))

    # Test 2: Single node, pivot less than node.
    root = Node(10)
    tree_less, tree_ge = balanced.split_bst(root, 5)
    print("split_bst Test 2 " + ("passed" if tree_less is None and tree_ge is not None and tree_ge.val == 10 else "failed"))

    # Test 3: Single node, pivot equal to node.
    root = Node(10)
    tree_less, tree_ge = balanced.split_bst(root, 10)
    # Depending on your implementation, one tree may be None.
    passed = (tree_less is None or tree_ge is None)
    print("split_bst Test 3 " + ("passed" if passed else "failed"))

    # Test 4: Single node, pivot greater than node.
    root = Node(10)
    tree_less, tree_ge = balanced.split_bst(root, 15)
    print("split_bst Test 4 " + ("passed" if tree_less is not None and tree_less.val == 10 and tree_ge is None else "failed"))

    # Test 5: Balanced tree split.
    #        10
    #       /  \
    #      5   15
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    tree_less, tree_ge = balanced.split_bst(root, 10)
    # Check inorder for each split.
    left_inorder = inorder_traversal(tree_less) if tree_less else []
    right_inorder = inorder_traversal(tree_ge) if tree_ge else []
    passed = (left_inorder == [] or left_inorder == [5]) and (right_inorder == [10,15] or right_inorder == [15])
    print("split_bst Test 5 " + ("passed" if passed else "failed"))

    # Test 6: Unbalanced tree split.
    #        10
    #       /
    #      5
    #     /
    #    2
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    tree_less, tree_ge = balanced.split_bst(root, 6)
    left_inorder = inorder_traversal(tree_less) if tree_less else []
    right_inorder = inorder_traversal(tree_ge) if tree_ge else []
    # Expect left_inorder to contain nodes < 6 and right_inorder >= 6.
    passed = (left_inorder == [2,5] or left_inorder == [5]) and (right_inorder == [10] or right_inorder == [10])
    print("split_bst Test 6 " + ("passed" if passed else "failed"))

    # Test 7: All nodes less than pivot.
    root = Node(10)
    root.left = Node(5)
    tree_less, tree_ge = balanced.split_bst(root, 20)
    print("split_bst Test 7 " + ("passed" if tree_less is not None and tree_ge is None else "failed"))

    # Test 8: All nodes greater than or equal to pivot.
    root = Node(10)
    root.right = Node(15)
    tree_less, tree_ge = balanced.split_bst(root, 5)
    print("split_bst Test 8 " + ("passed" if tree_less is None and tree_ge is not None else "failed"))

    # ========================================================
    # Method 10: Join BSTs (Balanced BST) (8 test cases)
    # ========================================================
    print("\nTesting join_bst:")
    # Test 1: One empty tree.
    tree1 = None
    tree2 = Node(10)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = [10]
    print("join_bst Test 1 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 2: Two non-empty trees.
    tree1 = Node(5)
    tree2 = Node(15)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = sorted([5,15])
    print("join_bst Test 2 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 3: Larger trees join.
    tree1 = Node(3)
    tree1.right = Node(4)
    tree2 = Node(10)
    tree2.left = Node(8)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = sorted([3,4,10,8])
    print("join_bst Test 3 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 4: Join trees where one is a single node.
    tree1 = Node(1)
    tree2 = Node(2)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = [1,2]
    print("join_bst Test 4 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 5: Trees that are already balanced.
    tree1 = Node(5)
    tree1.left = Node(3)
    tree1.right = Node(7)
    tree2 = Node(12)
    tree2.left = Node(10)
    tree2.right = Node(15)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = sorted([5,3,7,12,10,15])
    print("join_bst Test 5 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 6: Join where max of first equals min of second.
    tree1 = Node(5)
    tree1.right = Node(7)
    tree2 = Node(7)
    tree2.right = Node(9)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = sorted([5,7,7,9])
    print("join_bst Test 6 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 7: Join larger balanced trees.
    tree1 = Node(2)
    tree1.left = Node(1)
    tree1.right = Node(3)
    tree2 = Node(8)
    tree2.left = Node(6)
    tree2.right = Node(9)
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = sorted([2,1,3,8,6,9])
    print("join_bst Test 7 " + ("passed" if inorder_joined == expected else "failed"))

    # Test 8: Join with one tree completely empty.
    tree1 = Node(5)
    tree2 = None
    joined = balanced.join_bst(tree1, tree2)
    inorder_joined = inorder_traversal(joined)
    expected = [5]
    print("join_bst Test 8 " + ("passed" if inorder_joined == expected else "failed"))

    # ========================================================
    # Method 11: Find Median (Balanced BST) (8 test cases)
    # ========================================================
    print("\nTesting find_median:")
    # Test 1: Empty tree.
    root = None
    median = balanced.find_median(root)
    print("find_median Test 1 " + ("passed" if median == -1 else "failed"))
    
    # Test 2: Single node.
    root = Node(10)
    median = balanced.find_median(root)
    print("find_median Test 2 " + ("passed" if median == 10 else "failed"))
    
    # Test 3: Odd number of nodes.
    #        10
    #       /  \
    #      5   15
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    median = balanced.find_median(root)
    print("find_median Test 3 " + ("passed" if median == 10 else "failed"))
    
    # Test 4: Even number of nodes.
    #        10
    #       /  \
    #      5   15
    #         /
    #        12
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    median = balanced.find_median(root)
    # Assuming lower median is returned (10)
    print("find_median Test 4 " + ("passed" if median == 10 else "failed"))
    
    # Test 5: Larger tree odd count.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    median = balanced.find_median(root)
    print("find_median Test 5 " + ("passed" if median == 15 else "failed"))
    
    # Test 6: Larger tree even count.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    median = balanced.find_median(root)
    print("find_median Test 6 " + ("passed" if median == 10 else "failed"))
    
    # Test 7: Tree with duplicate values.
    root = Node(10)
    root.left = Node(10)
    root.right = Node(20)
    median = balanced.find_median(root)
    print("find_median Test 7 " + ("passed" if median == 10 else "failed"))
    
    # Test 8: Complex tree.
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    median = balanced.find_median(root)
    print("find_median Test 8 " + ("passed" if median == 50 else "failed"))

    # ========================================================
    # Method 12: Range Sum Query (Balanced BST) (8 test cases)
    # ========================================================
    print("\nTesting range_sum_query:")
    # Test 1: Empty tree.
    root = None
    s = balanced.range_sum_query(root, 10, 20)
    print("range_sum_query Test 1 " + ("passed" if s == 0 else "failed"))
    
    # Test 2: Single node within range.
    root = Node(15)
    s = balanced.range_sum_query(root, 10, 20)
    print("range_sum_query Test 2 " + ("passed" if s == 15 else "failed"))
    
    # Test 3: Single node out of range.
    root = Node(5)
    s = balanced.range_sum_query(root, 10, 20)
    print("range_sum_query Test 3 " + ("passed" if s == 0 else "failed"))
    
    # Test 4: Multiple nodes, all within range.
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    s = balanced.range_sum_query(root, 5, 25)
    print("range_sum_query Test 4 " + ("passed" if s == 45 else "failed"))
    
    # Test 5: Range excludes some nodes.
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    s = balanced.range_sum_query(root, 12, 18)
    print("range_sum_query Test 5 " + ("passed" if s == 15 else "failed"))
    
    # Test 6: Range at boundaries.
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    s = balanced.range_sum_query(root, 15, 20)
    print("range_sum_query Test 6 " + ("passed" if s == 35 else "failed"))
    
    # Test 7: Larger tree range sum.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    s = balanced.range_sum_query(root, 10, 25)
    print("range_sum_query Test 7 " + ("passed" if s == 45 else "failed"))
    
    # Test 8: Range covering entire tree.
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    s = balanced.range_sum_query(root, 0, 100)
    print("range_sum_query Test 8 " + ("passed" if s == 60 else "failed"))

if __name__ == "__main__":
    main()
