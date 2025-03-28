
from Solution import SequentialSearchST

def main():
    st = SequentialSearchST()

    # Test isEmpty and size
    if st.isEmpty():
        print("Symbol table is empty initially. (PASS)")
    else:
        print("Symbol table should be empty but is not. (FAIL)")

    if st.size() == 0:
        print("Size is 0 initially. (PASS)")
    else:
        print("Size should be 0 but is not. (FAIL)")

    # Insert some values
    st.put(3, "three")
    st.put(1, "one")
    st.put(2, "two")
    st.put(4, "four")

    # Check size
    if st.size() == 4:
        print("Size is 4 after inserts. (PASS)")
    else:
        print("Size should be 4 but is not. (FAIL)")

    # Test get
    if st.get(2) == "two":
        print("Value for key 2 is 'two'. (PASS)")
    else:
        print("Value for key 2 should be 'two' but is not. (FAIL)")

    # Test update
    st.put(2, "TWO")
    if st.get(2) == "TWO":
        print("Updated value for key 2 is 'TWO'. (PASS)")
    else:
        print("Value for key 2 should be 'TWO' but is not. (FAIL)")

    # Test contains
    if st.contains(3):
        print("Key 3 is in the table. (PASS)")
    else:
        print("Key 3 should be in the table but is not. (FAIL)")

    # Test delete
    st.delete(3)
    if not st.contains(3):
        print("Key 3 is removed from the table. (PASS)")
    else:
        print("Key 3 should be removed but is still present. (FAIL)")

    # Test min, max
    if st.min() == 1:
        print("Min key is 1. (PASS)")
    else:
        print("Min key should be 1 but is not. (FAIL)")

    if st.max() == 4:
        print("Max key is 4. (PASS)")
    else:
        print("Max key should be 4 but is not. (FAIL)")

    # Test floor, ceiling
    if st.floor(2) == 2:
        print("Floor of 2 is 2. (PASS)")
    else:
        print("Floor of 2 should be 2 but is not. (FAIL)")

    if st.ceiling(2) == 2:
        print("Ceiling of 2 is 2. (PASS)")
    else:
        print("Ceiling of 2 should be 2 but is not. (FAIL)")

    # Test rank
    rankOf2 = st.rank(2)
    if rankOf2 == 1:
        print("Rank of 2 is 1. (PASS)")
    else:
        print(f"Rank of 2 should be 1 but is {rankOf2}. (FAIL)")

    # Test select
    keyAtRank1 = st.select(1)
    if keyAtRank1 == 2:
        print("Key at rank 1 is 2. (PASS)")
    else:
        print(f"Key at rank 1 should be 2 but is {keyAtRank1}. (FAIL)")

    # Test deleteMin, deleteMax
    st.deleteMin()
    if not st.contains(1):
        print("Min key 1 is deleted. (PASS)")
    else:
        print("Min key 1 should be deleted but is not. (FAIL)")

    st.deleteMax()
    if not st.contains(4):
        print("Max key 4 is deleted. (PASS)")
    else:
        print("Max key 4 should be deleted but is not. (FAIL)")

    # Test size_range
    st.put(5, "five")
    st.put(6, "six")
    st.put(7, "seven")
    rangeSize = st.size_range(2, 6)
    if rangeSize == 3:
        print("Keys between 2 and 6 inclusive are 2,5,6. (PASS)")
    else:
        print(f"size_range(2,6) should be 3 but is {rangeSize}. (FAIL)")

    # Test keys() and keys_range()
    print("All keys (unsorted):", st.keys())
    sorted_all_keys = sorted(st.keys())
    print("All keys in sorted order:", sorted_all_keys)
    print("Keys between 2 and 6 in sorted order:", st.keys_range(2, 6))

    print("Testing completed.")


main()

