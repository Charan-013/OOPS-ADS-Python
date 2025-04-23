
from Solution import SeparateChainingHashST

# Test cases in Python
if __name__ == "__main__":
    st = SeparateChainingHashST()

    # Test 1: is_empty and size on an empty table
    if st.is_empty() and st.size() == 0:
        print("Test 1 passed: Empty table")
    else:
        print("Test 1 failed: Empty table")

    # Test 2: put and get methods
    st.put("apple", 1)
    st.put("banana", 2)
    st.put("cherry", 3)
    if st.get("apple") == 1 and st.get("banana") == 2 and st.get("cherry") == 3:
        print("Test 2 passed: put and get")
    else:
        print("Test 2 failed: put and get")

    # Test 3: Update value for an existing key
    st.put("banana", 20)
    if st.get("banana") == 20:
        print("Test 3 passed: update value")
    else:
        print("Test 3 failed: update value")

    # Test 4: contains method
    if st.contains("cherry") and not st.contains("date"):
        print("Test 4 passed: contains")
    else:
        print("Test 4 failed: contains")

    # Test 5: delete method
    st.delete("apple")
    if st.get("apple") is None and st.size() == 2:
        print("Test 5 passed: delete")
    else:
        print("Test 5 failed: delete")

    # Test 6: keys method
    keys_list = st.keys()
    if "banana" in keys_list and "cherry" in keys_list and "apple" not in keys_list:
        print("Test 6 passed: keys")
    else:
        print("Test 6 failed: keys")

    print("All Python tests completed.")
