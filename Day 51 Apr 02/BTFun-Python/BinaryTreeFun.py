
from Solution import BTNode, copy_tree, replace, countNodesAtDepth, allSame, leafList, reflect, condense, print_preorder

# -------------------------------
# Main function with test cases
# -------------------------------
def main():
    print("==== Testing copy ====")
    # Test copy on a null tree.
    null_tree = None
    copy_null = copy_tree(null_tree)
    print("Copy of null tree:", copy_null)  # Expected: None

    # Test copy on a single node tree.
    single_node = BTNode(10)
    copy_single = copy_tree(single_node)
    print("Original single node:", single_node.data)
    print("Copied single node:", copy_single.data)
    # Modify original to verify deep copy.
    single_node.data = 20
    print("After modifying original, copied remains:", copy_single.data)

    # Test copy on a multi-node tree.
    tree = BTNode(1,
                  BTNode(2,
                         BTNode(3),
                         BTNode(4)),
                  BTNode(5,
                         None,
                         BTNode(6)))
    copy_tree_multi = copy_tree(tree)
    print("Original tree (pre-order):", end=" ")
    print_preorder(tree)
    print("\nCopied tree (pre-order):", end=" ")
    print_preorder(copy_tree_multi)
    print()
    # Modify original tree to ensure the copy is independent.
    tree.left.data = 99
    print("After modifying original, copied tree remains (pre-order):", end=" ")
    print_preorder(copy_tree_multi)
    print("\n---------------------------------------")

    print("==== Testing replace ====")
    # Replace on null tree.
    count = replace(null_tree, 1, 100)
    print("Replace on null tree, count:", count)

    # Single node where value matches.
    node_test = BTNode(10)
    count = replace(node_test, 10, 50)
    print("Single node (match) replaced count:", count, "new value:", node_test.data)

    # Single node where value does not match.
    node_test = BTNode(10)
    count = replace(node_test, 5, 50)
    print("Single node (no match) replaced count:", count, "value remains:", node_test.data)

    # Multi-node tree replace.
    tree2 = BTNode(1,
                   BTNode(2,
                          BTNode(2),
                          BTNode(3)),
                   BTNode(2,
                          BTNode(4),
                          None))
    count = replace(tree2, 2, 9)
    print("Multi-node tree replaced count:", count)
    print("Modified tree (pre-order):", end=" ")
    print_preorder(tree2)
    print("\n---------------------------------------")

    print("==== Testing countNodesAtDepth ====")
    # Null tree.
    print("Null tree, depth 3:", countNodesAtDepth(null_tree, 3))
    # Single node tree.
    print("Single node, depth 0:", countNodesAtDepth(single_node, 0))
    print("Single node, depth 1:", countNodesAtDepth(single_node, 1))
    # Multi-node tree.
    print("Multi-node tree, depth 0:", countNodesAtDepth(tree, 0))
    print("Multi-node tree, depth 1:", countNodesAtDepth(tree, 1))
    print("Multi-node tree, depth 2:", countNodesAtDepth(tree, 2))
    print("Multi-node tree, depth 3 (should be 0):", countNodesAtDepth(tree, 3))
    print("---------------------------------------")

    print("==== Testing allSame ====")
    # Null tree.
    print("Null tree allSame:", allSame(null_tree))
    # Single node tree.
    same_tree = BTNode(7)
    print("Single node tree allSame:", allSame(same_tree))
    # Uniform tree.
    same_tree.left = BTNode(7)
    same_tree.right = BTNode(7)
    same_tree.left.left = BTNode(7)
    same_tree.right.right = BTNode(7)
    print("Uniform tree allSame:", allSame(same_tree))
    # Non-uniform tree.
    diff_tree = BTNode(7, BTNode(7), BTNode(8))
    print("Non-uniform tree allSame:", allSame(diff_tree))
    print("---------------------------------------")

    print("==== Testing leafList ====")
    # Null tree.
    print("Null tree leafList:", leafList(null_tree))
    # Single node tree.
    print("Single node tree leafList:", leafList(BTNode(100)))
    # Multi-node tree.
    tree3 = BTNode(1,
                   BTNode(2,
                          BTNode(9),
                          BTNode(3)),
                   BTNode(4,
                          None,
                          BTNode(7)))
    print("Multi-node tree leafList (expected [9, 3, 7]):", leafList(tree3))
    print("---------------------------------------")

    print("==== Testing reflect ====")
    # Reflect on null tree.
    reflect_null = None
    reflect(reflect_null)
    print("Reflect null tree remains:", reflect_null)
    # Reflect on single node tree.
    reflect_single = BTNode(5)
    print("Before reflect (single node):", end=" ")
    print_preorder(reflect_single)
    reflect(reflect_single)
    print("\nAfter reflect (single node):", end=" ")
    print_preorder(reflect_single)
    print()
    # Reflect on multi-node tree.
    tree4 = BTNode(1,
                   BTNode(2,
                          BTNode(3),
                          BTNode(4)),
                   BTNode(5,
                          BTNode(6),
                          BTNode(7)))
    print("Before reflect (pre-order):", end=" ")
    print_preorder(tree4)
    reflect(tree4)
    print("\nAfter reflect (pre-order):", end=" ")
    print_preorder(tree4)
    print("\n---------------------------------------")

    print("==== Testing condense ====")
    # Condense on null tree.
    condense_null = None
    result = condense(condense_null)
    print("Condense null tree:", result)
    # Condense on single node tree.
    condense_single = BTNode(10)
    result = condense(condense_single)
    print("Condense single node tree (should be unchanged):", end=" ")
    print_preorder(result)
    print()
    # Tree that is a chain (every node has one child).
    chain = BTNode(1, BTNode(2, BTNode(3), None), None)
    print("Chain tree before condense (pre-order):", end=" ")
    print_preorder(chain)
    result = condense(chain)
    print("\nChain tree after condense (should be a single node):", end=" ")
    print_preorder(result)
    print()
    # Mixed tree: some nodes with one child, others with two.
    tree5 = BTNode(10,
                   BTNode(20,
                          BTNode(30),
                          None),  # one-child node
                   BTNode(40,
                          BTNode(50),
                          BTNode(60)))
    print("Mixed tree before condense (pre-order):", end=" ")
    print_preorder(tree5)
    result = condense(tree5)
    print("\nMixed tree after condense (pre-order):", end=" ")
    print_preorder(result)
    print("\n---------------------------------------")


if __name__ == '__main__':
    main()
