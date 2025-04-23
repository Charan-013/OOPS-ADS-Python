
from Solution import LinearProbingHashST

# Main method to test the LinearProbingHashST class
def main():
    st = LinearProbingHashST()

    # Test is_empty method
    if st.is_empty():
        print("Symbol table is empty initially.")
    else:
        print("Symbol table is not empty initially.")

    # Test put method
    st.put("apple", 1)
    st.put("banana", 2)
    st.put("cherry", 3)
    st.put("date", 4)

    # Test size method
    if st.size() == 4:
        print("4 items added successfully. Current size:", st.size())
    else:
        print("Error in size after adding items.")

    # Test get method for an existing key
    if st.get("banana") is not None:
        print("Value for 'banana':", st.get("banana"))
    else:
        print("Key 'banana' not found.")

    # Test contains method
    if st.contains("apple"):
        print("'apple' is present in the symbol table.")
    else:
        print("'apple' is not present in the symbol table.")

    # Test updating a key-value pair
    st.put("banana", 20)
    if st.get("banana") == 20:
        print("Updated 'banana' to", st.get("banana"))
    else:
        print("Failed to update 'banana'.")

    # Test delete method
    st.delete("cherry")
    if not st.contains("cherry"):
        print("'cherry' has been successfully deleted.")
    else:
        print("Error: 'cherry' still exists.")

    # Test get method for a non-existing key
    if st.get("fig") is None:
        print("Key 'fig' not found, as expected.")
    else:
        print("Error: 'fig' unexpectedly found.")

    # Test keys iteration and print remaining key-value pairs
    print("Remaining keys in the symbol table:")
    for key in st.keys_iter():
        print(key, "->", st.get(key))


if __name__ == "__main__":
    main()

