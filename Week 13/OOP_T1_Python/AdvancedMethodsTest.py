from solution import Node, BinaryTree, BinarySearchTree, BalancedBST
import collections

def to_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.right
    return vals

def inorder(root, out):
    if not root:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)

def main():
    bt = BinaryTree()
    bst = BinarySearchTree()
    balanced = BalancedBST()

    print("Testing maxSumNonAdjacent:")
    root = None; exp = 0
    res = bt.max_sum_non_adjacent(root)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(5); exp = 5
    res = bt.max_sum_non_adjacent(root)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(10)
    root.left = Node(1); root.right = Node(2)
    exp = 10
    res = bt.max_sum_non_adjacent(root)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(5)
    root.left = Node(1); root.right = Node(2)
    root.left.left = Node(3); root.left.right = Node(4)
    exp = 12
    res = bt.max_sum_non_adjacent(root)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting burningTree:")
    root = None; exp = 0
    res = bt.burning_tree(root, 0)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(1); exp = 0
    res = bt.burning_tree(root, 1)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(1)
    root.left = Node(2); root.right = Node(3)
    exp = 2
    res = bt.burning_tree(root, 2)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(1)
    root.right = Node(2); root.right.right = Node(3); root.right.right.right = Node(4)
    exp = 2
    res = bt.burning_tree(root, 2)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting hasTripletWithSum:")
    root = None; exp = False
    res = bst.has_triplet_with_sum(root, 10)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(2)
    root.right = Node(3); root.right.right = Node(5)
    exp = True
    res = bst.has_triplet_with_sum(root, 10)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(4)
    root.left = Node(2); root.right = Node(6)
    root.left.left = Node(1); root.left.right = Node(3)
    exp = True
    res = bst.has_triplet_with_sum(root, 11)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(3)
    root.left = Node(3); root.right = Node(3)
    exp = True
    res = bst.has_triplet_with_sum(root, 9)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting bstToDoublyLinkedList:")
    root = None; exp = []
    head = bst.bst_to_doubly_linked_list(root)
    res = to_list(head)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(7); exp = [7]
    head = bst.bst_to_doubly_linked_list(root)
    res = to_list(head)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(2)
    root.left = Node(1); root.right = Node(3)
    exp = [1,2,3]
    head = bst.bst_to_doubly_linked_list(root)
    res = to_list(head)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(5)
    root.left = Node(3); root.left.left = Node(2); root.left.left.left = Node(1)
    exp = [1,2,3,5]
    head = bst.bst_to_doubly_linked_list(root)
    res = to_list(head)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting longestConsecutive:")
    root = None; exp = 0
    res = bst.longest_consecutive(root)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(10); exp = 1
    res = bst.longest_consecutive(root)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(1)
    root.right = Node(2); root.right.right = Node(3)
    exp = 3
    res = bst.longest_consecutive(root)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(2)
    root.left = Node(1); root.right = Node(4)
    exp = 1
    res = bst.longest_consecutive(root)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting countNodesInRange:")
    root = None; exp = 0
    res = bst.count_nodes_in_range(root, 0, 100, True)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(10); exp = 1
    res = bst.count_nodes_in_range(root, 5, 15, True)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    exp = 0
    res = bst.count_nodes_in_range(root, 5, 15, False)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(8)
    root.left = Node(3); root.right = Node(10)
    root.left.left = Node(1); root.left.right = Node(6)
    exp = 1
    res = bst.count_nodes_in_range(root, 2, 8, False)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting sortedListToAVL:")
    in_list = []
    out_list = []
    root = balanced.sorted_list_to_avl(in_list)
    inorder(root, out_list)
    print("Test 1 passed" if out_list==in_list else "Test 1 failed")

    in_list = [5]; out_list = []
    root = balanced.sorted_list_to_avl(in_list)
    inorder(root, out_list)
    print("Test 2 passed" if out_list==in_list else "Test 2 failed")

    in_list = [1,2,3]; out_list = []
    root = balanced.sorted_list_to_avl(in_list)
    inorder(root, out_list)
    print("Test 3 passed" if out_list==in_list else "Test 3 failed")

    in_list = [1,2,3,4,5]; out_list = []
    root = balanced.sorted_list_to_avl(in_list)
    inorder(root, out_list)
    print("Test 4 passed" if out_list==in_list else "Test 4 failed")

    print("\nTesting minSumPath:")
    root = None; exp = 0
    res = balanced.min_sum_path(root)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(7); exp = 7
    res = balanced.min_sum_path(root)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(5)
    root.left = Node(3); root.right = Node(8)
    exp = 8
    res = balanced.min_sum_path(root)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(10)
    root.left = Node(5); root.right = Node(2)
    exp = 12
    res = balanced.min_sum_path(root)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting sumAtPrimeLevels:")
    root = None; exp = 0
    res = balanced.sum_at_prime_levels(root)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(10); exp = 0
    res = balanced.sum_at_prime_levels(root)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    root = Node(1)
    root.left = Node(2); root.right = Node(3)
    exp = 5
    res = balanced.sum_at_prime_levels(root)
    print("Test 3 passed" if res==exp else "Test 3 failed")

    root = Node(1)
    root.left = Node(2); root.right = Node(3)
    root.left.left = Node(4); root.left.right = Node(5)
    exp = 14
    res = balanced.sum_at_prime_levels(root)
    print("Test 4 passed" if res==exp else "Test 4 failed")

    print("\nTesting replaceNodeRBTree:")
    root = None
    res_node = balanced.replace_node_rb_tree(root, 5, 10)
    print("Test 1 passed" if res_node is None else "Test 1 failed")

    root = Node(5)
    res_node = balanced.replace_node_rb_tree(root, 5, 8)
    exp = 8
    print("Test 2 passed" if (res_node and res_node.val==exp) else "Test 2 failed")

    print("\nTesting rbTreeHeight:")
    root = None; exp = 0
    res = balanced.rb_tree_height(root)
    print("Test 1 passed" if res==exp else "Test 1 failed")

    root = Node(7); exp = 1
    res = balanced.rb_tree_height(root)
    print("Test 2 passed" if res==exp else "Test 2 failed")

    print("\nTesting avlToMaxHeap:")
    in_list = []; out_list = []
    root = None
    root = balanced.avl_to_max_heap(root)
    inorder(root, out_list)
    print("Test 1 passed" if out_list==in_list else "Test 1 failed")

    root = balanced.sorted_list_to_avl([1,2,3])
    res = balanced.avl_to_max_heap(root)
    print("Test 2 (manual check) passed" if res else "Test 2 failed")

if __name__ == "__main__":
    main()
