
from Solution import BinaryTree
# Test functions to mimic the Java test cases

def countTest():
    # Binary Tree #1
    tree1 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40)),
                       BinaryTree(78,
                                  BinaryTree(61),
                                  BinaryTree(92)))
    print("Number of internal nodes =", tree1.countInternal())

    # Binary Tree #2
    tree2 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40,
                                             BinaryTree(37),
                                             BinaryTree(49))),
                       BinaryTree(78))
    print("Number of internal nodes =", tree2.countInternal())

    # Binary Tree #3
    tree3 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40)),
                       BinaryTree(78))
    print("Number of internal nodes =", tree3.countInternal())

    # Binary Tree #4
    tree4 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40,
                                             BinaryTree(37),
                                             BinaryTree(49))),
                       BinaryTree(61,
                                  None,
                                  BinaryTree(92,
                                             BinaryTree(78),
                                             None)))
    print("Number of internal nodes =", tree4.countInternal())

    # Binary Tree #5
    tree5 = BinaryTree(11,
                       BinaryTree(22,
                                  BinaryTree(33,
                                             BinaryTree(44,
                                                        BinaryTree(55,
                                                                   BinaryTree(66,
                                                                              BinaryTree(77,
                                                                                         BinaryTree(88,
                                                                                                    BinaryTree(99),
                                                                                                    None),
                                                                                         None),
                                                                              None),
                                                                   None),
                                                        None),
                                             None),
                                  None))
    print("Number of internal nodes =", tree5.countInternal())

    # Binary Tree #6
    tree6 = BinaryTree(42)
    print("Number of internal nodes =", tree6.countInternal())

    # Binary Tree #7 (empty tree)
    tree7 = BinaryTree()
    print("Number of internal nodes =", tree7.countInternal())


def heightTest():
    # Binary Tree #1
    tree1 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40)),
                       BinaryTree(78,
                                  BinaryTree(61),
                                  BinaryTree(92)))
    print("Tree height =", tree1.height())

    # Binary Tree #2
    tree2 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40,
                                             BinaryTree(37),
                                             BinaryTree(49))),
                       BinaryTree(78))
    print("Tree height =", tree2.height())

    # Binary Tree #3
    tree3 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40)),
                       BinaryTree(78))
    print("Tree height =", tree3.height())

    # Binary Tree #4
    tree4 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40,
                                             BinaryTree(37),
                                             BinaryTree(49))),
                       BinaryTree(61,
                                  None,
                                  BinaryTree(92,
                                             BinaryTree(78),
                                             None)))
    print("Tree height =", tree4.height())

    # Binary Tree #5
    tree5 = BinaryTree(11,
                       BinaryTree(22,
                                  BinaryTree(33,
                                             BinaryTree(44,
                                                        BinaryTree(55,
                                                                   BinaryTree(66,
                                                                              BinaryTree(77,
                                                                                         BinaryTree(88,
                                                                                                    BinaryTree(99),
                                                                                                    None),
                                                                                         None),
                                                                              None),
                                                                   None),
                                                        None),
                                             None),
                                  None))
    print("Tree height =", tree5.height())

    # Binary Tree #6
    tree6 = BinaryTree(42)
    print("Tree height =", tree6.height())

    # Binary Tree #7 (empty tree)
    tree7 = BinaryTree()
    print("Tree height =", tree7.height())


def isPerfectTest():
    # Binary Tree #1
    tree1 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40)),
                       BinaryTree(78,
                                  BinaryTree(61),
                                  BinaryTree(92)))
    print("Tree is perfect:", tree1.isPerfect())

    # Binary Tree #2
    tree2 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40,
                                             BinaryTree(37),
                                             BinaryTree(49))),
                       BinaryTree(78))
    print("Tree is perfect:", tree2.isPerfect())

    # Binary Tree #3
    tree3 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40)),
                       BinaryTree(78))
    print("Tree is perfect:", tree3.isPerfect())

    # Binary Tree #4
    tree4 = BinaryTree(56,
                       BinaryTree(34,
                                  BinaryTree(23),
                                  BinaryTree(40,
                                             BinaryTree(37),
                                             BinaryTree(49))),
                       BinaryTree(61,
                                  None,
                                  BinaryTree(92,
                                             BinaryTree(78),
                                             None)))
    print("Tree is perfect:", tree4.isPerfect())

    # Binary Tree #5
    tree5 = BinaryTree(11,
                       BinaryTree(22,
                                  BinaryTree(33,
                                             BinaryTree(44,
                                                        BinaryTree(55,
                                                                   BinaryTree(66,
                                                                              BinaryTree(77,
                                                                                         BinaryTree(88,
                                                                                                    BinaryTree(99),
                                                                                                    None),
                                                                                         None),
                                                                              None),
                                                                   None),
                                                        None),
                                             None),
                                  None))
    print("Tree is perfect:", tree5.isPerfect())

    # Binary Tree #6
    tree6 = BinaryTree(42)
    print("Tree is perfect:", tree6.isPerfect())

    # Binary Tree #7 (empty tree)
    tree7 = BinaryTree()
    print("Tree is perfect:", tree7.isPerfect())


if __name__ == "__main__":
    print("----- Count Internal Test -----")
    countTest()
    print("\n----- Height Test -----")
    heightTest()
    print("\n----- Is Perfect Test -----")
    isPerfectTest()
