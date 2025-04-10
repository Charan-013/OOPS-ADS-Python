

from Solution import RedBlackBST
# Main method with test cases.
def main():
    tree = RedBlackBST()
    # Insert test keys.
    tree.put(5, "Five")
    tree.put(3, "Three")
    tree.put(7, "Seven")
    tree.put(2, "Two")
    tree.put(4, "Four")
    tree.put(6, "Six")
    tree.put(8, "Eight")

    # Test isBST.
    if tree.isBST():
        print("The tree is a BST.")
    else:
        print("The tree is NOT a BST.")

    # Test is23.
    if tree.is23():
        print("The tree has no right-leaning red links and no node is connected to two red links.")
    else:
        print("The tree violates the 2-3 property.")

    # Test isBalanced.
    if tree.isBalanced():
        print("The tree is balanced with respect to black links.")
    else:
        print("The tree is NOT balanced with respect to black links.")

    # Test isRedBlackBST.
    if tree.isRedBlackBST():
        print("The tree is a valid Red-Black BST.")
    else:
        print("The tree is NOT a valid Red-Black BST.")
        
main()
