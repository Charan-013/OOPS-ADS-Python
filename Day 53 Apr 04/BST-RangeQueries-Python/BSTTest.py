
from Solution import BST, Node

# ------------------ Main Testing Section ------------------
if __name__ == "__main__":
    bst = BST()

    # Test 1: is_empty and size on an empty tree
    if bst.is_empty() and bst.size() == 0:
        print("Test 1 (empty tree) passed")
    else:
        print("Test 1 (empty tree) failed")

    # Insert key-value pairs
    bst.put(5, "five")
    bst.put(3, "three")
    bst.put(7, "seven")
    bst.put(2, "two")
    bst.put(4, "four")
    bst.put(6, "six")
    bst.put(8, "eight")

    # Test 2: size after insertion (should be 7)
    if (not bst.is_empty()) and bst.size() == 7:
        print("Test 2 (size after insertion) passed")
    else:
        print("Test 2 (size after insertion) failed")

    # Test 3: get and contains
    if bst.get(5) == "five" and bst.contains(4) and not bst.contains(10):
        print("Test 3 (get and contains) passed")
    else:
        print("Test 3 (get and contains) failed")

    # Test 4: min and max
    if bst.min() == 2 and bst.max() == 8:
        print("Test 4 (min and max) passed")
    else:
        print("Test 4 (min and max) failed")

    # Test 5: floor
    try:
        # For key=5, floor should be 5.
        if bst.floor(5) == 5:
            print("Test 5 (floor with existing key) passed")
        else:
            print("Test 5 (floor with existing key) failed")
    except ValueError:
        print("Test 5 (floor with existing key) failed with exception")
    try:
        bst.floor(1)  # This should raise an exception because 1 is less than min.
        print("Test 5 (floor with too small key) failed")
    except ValueError:
        print("Test 5 (floor with too small key) passed")

    # Test 6: floor2
    try:
        if bst.floor2(5) == 5:
            print("Test 6 (floor2) passed")
        else:
            print("Test 6 (floor2) failed")
    except ValueError:
        print("Test 6 (floor2) failed with exception")

    # Test 7: ceiling
    try:
        if bst.ceiling(5) == 5:
            print("Test 7 (ceiling with existing key) passed")
        else:
            print("Test 7 (ceiling with existing key) failed")
    except ValueError:
        print("Test 7 (ceiling with existing key) failed with exception")
    try:
        bst.ceiling(9)  # This should raise an exception because 9 is greater than max.
        print("Test 7 (ceiling with too large key) failed")
    except ValueError:
        print("Test 7 (ceiling with too large key) passed")

    # Test 8: select
    try:
        if bst.select(0) == 2 and bst.select(6) == 8:
            print("Test 8 (select) passed")
        else:
            print("Test 8 (select) failed")
    except ValueError:
        print("Test 8 (select) failed with exception")

    # Test 9: rank
    # In sorted order [2, 3, 4, 5, 6, 7, 8], rank(2)=0 and rank(5)=3.
    if bst.rank(2) == 0 and bst.rank(5) == 3:
        print("Test 9 (rank) passed")
    else:
        print("Test 9 (rank) failed")

    # Test 10: keys (all keys)
    keys_all = bst.keys()
    if keys_all == [2, 3, 4, 5, 6, 7, 8]:
        print("Test 10 (keys - all) passed")
    else:
        print("Test 10 (keys - all) failed", keys_all)

    # Test 11: keys in range (3, 7)
    keys_range = bst.keys(3, 7)
    if keys_range == [3, 4, 5, 6, 7]:
        print("Test 11 (keys in range) passed")
    else:
        print("Test 11 (keys in range) failed", keys_range)

    # Test 12: size_range (3, 7) should return 5
    if bst.size_range(3, 7) == 5:
        print("Test 12 (size_range) passed")
    else:
        print("Test 12 (size_range) failed")

    # Test 13: height (should be non-negative)
    h = bst.height()
    if isinstance(h, int) and h >= 0:
        print("Test 13 (height) passed")
    else:
        print("Test 13 (height) failed")

    # Test 14: level order traversal
    # For the inserted keys in order, the expected level order is [5, 3, 7, 2, 4, 6, 8]
    if bst.level_order() == [5, 3, 7, 2, 4, 6, 8]:
        print("Test 14 (level order) passed")
    else:
        print("Test 14 (level order) failed", bst.level_order())

    # Test 15: delete_min
    bst.delete_min()  # Removes key 2
    if bst.min() == 3 and bst.size() == 6:
        print("Test 15 (delete_min) passed")
    else:
        print("Test 15 (delete_min) failed")

    # Test 16: delete_max
    bst.delete_max()  # Removes key 8
    if bst.max() == 7 and bst.size() == 5:
        print("Test 16 (delete_max) passed")
    else:
        print("Test 16 (delete_max) failed")

    # Test 17: delete (delete key 5)
    bst.delete(5)
    if (not bst.contains(5)) and bst.size() == 4:
        print("Test 17 (delete key) passed")
    else:
        print("Test 17 (delete key) failed")

