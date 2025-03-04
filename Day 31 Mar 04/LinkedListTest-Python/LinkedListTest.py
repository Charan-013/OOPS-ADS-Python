# linked_list_test.py
# This script tests your MyLinkedList implementation.
# It expects a file (for example, my_linked_list.py) containing the MyLinkedList class.
# Ensure that the __str__ method of MyLinkedList prints the list in the following format:
# - For non-empty lists, each element is printed within square brackets (e.g., "[elem1][elem2]")
# - For an empty list, the string "LinkedList is empty" is returned

from Solution import MyLinkedList  # adjust the import according to your implementation

def run_basic_tests():
    count = 0
    ll = MyLinkedList()
    
    # Test case 1
    ll.add("Hello World")
    if str(ll) == "[Hello World]":
        print("Test case 1 passed")
        count += 1
    else:
        print("Test case 1 failed")
    
    # Test case 2
    ll.add_first("Linked List")
    if str(ll) == "[Linked List][Hello World]":
        print("Test case 2 passed")
        count += 1
    else:
        print("Test case 2 failed")
    
    # Test case 3
    ll.add("Data Structure")
    if str(ll) == "[Linked List][Hello World][Data Structure]":
        print("Test case 3 passed")
        count += 1
    else:
        print("Test case 3 failed")
    
    # Test case 4
    if not ll.contains("Data Structur"):  # note: missing 'e'
        print("Test case 4 passed")
        count += 1
    else:
        print("Test case 4 failed")
    
    # Test case 5
    if ll.get_first() == "Linked List":
        print("Test case 5 passed")
        count += 1
    else:
        print("Test case 5 failed")
    
    # Test case 6
    if ll.get_last() == "Data Structure":
        print("Test case 6 passed")
        count += 1
    else:
        print("Test case 6 failed")
    
    # Test case 7
    if ll.size() == 3:
        print("Test case 7 passed")
        count += 1
    else:
        print("Test case 7 failed")
    
    # Test case 8
    removed = ll.remove()
    if str(ll) == "[Hello World][Data Structure]":
        print("Test case 8 passed")
        count += 1
    else:
        print("Test case 8 failed")
    
    # Test case 9
    if removed == "Linked List":
        print("Test case 9 passed")
        count += 1
    else:
        print("Test case 9 failed")
    
    # Test case 10
    removed_last = ll.remove_last()
    if str(ll) == "[Hello World]":
        print("Test case 10 passed")
        count += 1
    else:
        print("Test case 10 failed")
    
    # Test case 11
    if removed_last == "Data Structure":
        print("Test case 11 passed")
        count += 1
    else:
        print("Test case 11 failed")
    
    # Test case 12
    if ll.size() == 1:
        print("Test case 12 passed")
        count += 1
    else:
        print("Test case 12 failed")
    
    # Test case 13
    if ll.get(0) == "Hello World":
        print("Test case 13 passed")
        count += 1
    else:
        print("Test case 13 failed")
    
    # Test case 14
    removed2 = ll.remove()
    if str(ll) == "LinkedList is empty":
        print("Test case 14 passed")
        count += 1
    else:
        print("Test case 14 failed")
    
    # Test case 15
    if removed2 == "Hello World":
        print("Test case 15 passed")
        count += 1
    else:
        print("Test case 15 failed")
    
    # Test case 16
    if ll.size() == 0:
        print("Test case 16 passed")
        count += 1
    else:
        print("Test case 16 failed")
    
    if count == 16:
        print("***************************************")
        print("All basic testcases passed")
        print("Great going, try edge cases below")
        print("***************************************")
    else:
        print(f"{count}/16 basic testcases passed")
        
def run_edge_cases():
    count = 0
    ll = MyLinkedList()
    
    # Test case 17
    if str(ll) == "LinkedList is empty":
        print("Test case 17 passed")
        count += 1
    else:
        print("Test case 17 failed")
    
    # Test case 18
    if ll.size() == 0:
        print("Test case 18 passed")
        count += 1
    else:
        print("Test case 18 failed")
    
    # Test case 19
    ll.add("")
    if str(ll) == "[]":
        print("Test case 19 passed")
        count += 1
    else:
        print("Test case 19 failed")
    
    # Test case 20
    ll.add("\t")
    if str(ll) == "[][\t]":
        print("Test case 20 passed")
        count += 1
    else:
        print("Test case 20 failed")
    
    # Test case 21
    ll.clear()
    if str(ll) == "LinkedList is empty":
        print("Test case 21 passed")
        count += 1
    else:
        print("Test case 21 failed")
    
    # Test case 22
    ll.remove()
    if str(ll) == "LinkedList is empty":
        print("Test case 22 passed")
        count += 1
    else:
        print("Test case 22 failed")
    
    # Test case 23
    ll.remove_last()
    if str(ll) == "LinkedList is empty":
        print("Test case 23 passed")
        count += 1
    else:
        print("Test case 23 failed")
    
    # Test case 24
    if ll.get_first() is None:
        print("Test case 24 passed")
        count += 1
    else:
        print("Test case 24 failed")
    
    # Test case 25
    if ll.get_last() is None:
        print("Test case 25 passed")
        count += 1
    else:
        print("Test case 25 failed")
    
    # Test case 26
    if not ll.contains(None):
        print("Test case 26 passed")
        count += 1
    else:
        print("Test case 26 failed")
    
    # Test case 27
    ll.add_first("1")
    ll.add_first("2")
    ll.add_first("3")
    ll.add_first("5")
    ll.add_first("1")
    if str(ll) == "[1][5][3][2][1]":
        print("Test case 27 passed")
        count += 1
    else:
        print("Test case 27 failed")
    
    # Test case 28
    ll.add("1")
    ll.add("2")
    ll.add("3")
    ll.add("5")
    if str(ll) == "[1][5][3][2][1][1][2][3][5]":
        print("Test case 28 passed")
        count += 1
    else:
        print("Test case 28 failed")
    
    # Test case 29
    for _ in range(9):
        ll.remove_last()
    if str(ll) == "LinkedList is empty":
        print("Test case 29 passed")
        count += 1
    else:
        print("Test case 29 failed")
    
    # Test case 30
    ll.remove_last()
    ll.remove()
    ll.remove()
    if str(ll) == "LinkedList is empty" and ll.size() == 0:
        print("Test case 30 passed")
        count += 1
    else:
        print("Test case 30 failed")
    
    if count == 14:
        print("***************************************")
        print("Great Job")
        print("***************************************")
    else:
        print(f"{count}/14 edge testcases passed")

if __name__ == '__main__':
    run_basic_tests()
    run_edge_cases()
