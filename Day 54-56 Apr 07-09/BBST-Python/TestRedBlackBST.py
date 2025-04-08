
from Solution import RedBlackBST
# ---------------------------
# Test cases for the Python version
# ---------------------------
def main():
    st = RedBlackBST()

    # Test is_empty() and size() on an empty symbol table.
    if st.is_empty() and st.size() == 0:
        print("Test is_empty and size (empty) passed")
    else:
        print("Test is_empty and size (empty) failed")

    # Test put() and size().
    st.put(5, "five")
    if (not st.is_empty()) and (st.size() == 1):
        print("Test put and size passed")
    else:
        print("Test put and size failed")

    # Test get().
    if st.get(5) == "five":
        print("Test get passed")
    else:
        print("Test get failed")

    # Test contains().
    if st.contains(5) and (not st.contains(10)):
        print("Test contains passed")
    else:
        print("Test contains failed")

    # Insert more elements.
    st.put(3, "three")
    st.put(7, "seven")
    st.put(2, "two")
    st.put(4, "four")
    st.put(6, "six")
    st.put(8, "eight")

    # Test min() and max().
    if st.min() == 2 and st.max() == 8:
        print("Test min and max passed")
    else:
        print("Test min and max failed")

    # Test floor() and ceiling().
    if st.floor(5) == 5 and st.ceiling(5) == 5:
        print("Test floor and ceiling passed")
    else:
        print("Test floor and ceiling failed")

    # Test select().
    if st.select(0) == 2 and st.select(st.size()-1) == 8:
        print("Test select passed")
    else:
        print("Test select failed")

    # Test rank().
    # With keys [2, 3, 4, 5, 6, 7, 8]: rank(2) should be 0, rank(5) should be 3, rank(8) should be 6.
    if st.rank(2) == 0 and st.rank(5) == 3 and st.rank(8) == 6:
        print("Test rank passed")
    else:
        print("Test rank failed")

    # Test keys() – should return keys in ascending order.
    keys_list = st.keys()
    if keys_list == [2, 3, 4, 5, 6, 7, 8]:
        print("Test keys() passed")
    else:
        print("Test keys() failed:", keys_list)

    # Test keys(lo, hi) – for example, keys between 3 and 6.
    keys_range_list = st.keys(3, 6)
    if keys_range_list == [3, 4, 5, 6]:
        print("Test keys(lo, hi) passed")
    else:
        print("Test keys(lo, hi) failed:", keys_range_list)

    # Test size_range().
    if st.size_range(3, 6) == 4:
        print("Test size(lo, hi) passed")
    else:
        print("Test size(lo, hi) failed:", st.size_range(3, 6))

    # Test height() (ensure it returns a non-negative value).
    h = st.height()
    if h >= 0:
        print("Test height passed, height:", h)
    else:
        print("Test height failed, height:", h)

    # Test delete_min() – after deleting the minimum, min() should return the next smallest key.
    st.delete_min()
    if st.min() == 3 and st.size() == 6:
        print("Test delete_min passed")
    else:
        print("Test delete_min failed")

    # Test delete_max() – after deleting the maximum, max() should return the next largest key.
    st.delete_max()
    if st.max() == 7 and st.size() == 5:
        print("Test delete_max passed")
    else:
        print("Test delete_max failed")

    # Test delete() – delete a middle key (e.g., 5).
    st.delete(5)
    if (not st.contains(5)) and st.size() == 4:
        print("Test delete passed")
    else:
        print("Test delete failed")

if __name__ == '__main__':
    main()
