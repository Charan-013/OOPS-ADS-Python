
from Solution import Stack

def main():
    passed = 0
    failed = 0
    stack = Stack()

    # Test 1: Stack is empty
    if stack.empty():
        print("Test 1 passed")
        passed += 1
    else:
        print("Test 1 failed: Stack should be empty")
        failed += 1

    # Test 2: Peek on empty stack should raise exception
    try:
        stack.peek()
        print("Test 2 failed: peek() did not raise exception on empty stack")
        failed += 1
    except IndexError:
        print("Test 2 passed: peek() raised exception on empty stack")
        passed += 1

    # Test 3: Pop on empty stack should raise exception
    try:
        stack.pop()
        print("Test 3 failed: pop() did not raise exception on empty stack")
        failed += 1
    except IndexError:
        print("Test 3 passed: pop() raised exception on empty stack")
        passed += 1

    # Test 4: Push "A", then check not empty.
    stack.push("A")
    if not stack.empty():
        print("Test 4 passed: Stack is not empty after push")
        passed += 1
    else:
        print("Test 4 failed: Stack is still empty after push")
        failed += 1

    # Test 5: Peek returns "A"
    if stack.peek() == "A":
        print("Test 5 passed: peek() returned A")
        passed += 1
    else:
        print("Test 5 failed: peek() did not return A")
        failed += 1

    # Test 6: Search "A" should return 1
    if stack.search("A") == 1:
        print("Test 6 passed: search(A) returned 1")
        passed += 1
    else:
        print("Test 6 failed: search(A) did not return 1")
        failed += 1

    # Test 7: Push "B", check peek returns "B"
    stack.push("B")
    if stack.peek() == "B":
        print("Test 7 passed: peek() returned B after push")
        passed += 1
    else:
        print("Test 7 failed: peek() did not return B after push")
        failed += 1

    # Test 8: Search "B" should return 1
    if stack.search("B") == 1:
        print("Test 8 passed: search(B) returned 1")
        passed += 1
    else:
        print("Test 8 failed: search(B) did not return 1")
        failed += 1

    # Test 9: Search "A" should return 2
    if stack.search("A") == 2:
        print("Test 9 passed: search(A) returned 2")
        passed += 1
    else:
        print("Test 9 failed: search(A) did not return 2")
        failed += 1

    # Test 10: Push "C", check peek returns "C"
    stack.push("C")
    if stack.peek() == "C":
        print("Test 10 passed: peek() returned C")
        passed += 1
    else:
        print("Test 10 failed: peek() did not return C")
        failed += 1

    # Test 11: Search "C" should return 1
    if stack.search("C") == 1:
        print("Test 11 passed: search(C) returned 1")
        passed += 1
    else:
        print("Test 11 failed: search(C) did not return 1")
        failed += 1

    # Test 12: Pop returns "C"
    if stack.pop() == "C":
        print("Test 12 passed: pop() returned C")
        passed += 1
    else:
        print("Test 12 failed: pop() did not return C")
        failed += 1

    # Test 13: After pop, peek returns "B"
    if stack.peek() == "B":
        print("Test 13 passed: peek() returned B after pop")
        passed += 1
    else:
        print("Test 13 failed: peek() did not return B after pop")
        failed += 1

    # Test 14: Pop returns "B"
    if stack.pop() == "B":
        print("Test 14 passed: pop() returned B")
        passed += 1
    else:
        print("Test 14 failed: pop() did not return B")
        failed += 1

    # Test 15: Pop returns "A"
    if stack.pop() == "A":
        print("Test 15 passed: pop() returned A")
        passed += 1
    else:
        print("Test 15 failed: pop() did not return A")
        failed += 1

    # Test 16: Stack is empty now.
    if stack.empty():
        print("Test 16 passed: Stack is empty after popping all elements")
        passed += 1
    else:
        print("Test 16 failed: Stack is not empty after popping all elements")
        failed += 1

    # Test 17: Search "Z" returns -1.
    if stack.search("Z") == -1:
        print("Test 17 passed: search(Z) returned -1")
        passed += 1
    else:
        print("Test 17 failed: search(Z) did not return -1")
        failed += 1

    # Test 18: Push "X", "Y", "Z" and check search positions.
    stack.push("X")
    stack.push("Y")
    stack.push("Z")
    if stack.search("Z") == 1 and stack.search("Y") == 2 and stack.search("X") == 3:
        print("Test 18 passed: search positions correct after multiple pushes")
        passed += 1
    else:
        print("Test 18 failed: search positions incorrect after multiple pushes")
        failed += 1

    # Test 19: Pop returns "Z" and peek returns "Y"
    if stack.pop() == "Z" and stack.peek() == "Y":
        print("Test 19 passed: pop and peek worked correctly")
        passed += 1
    else:
        print("Test 19 failed: pop and peek did not work as expected")
        failed += 1

    # Test 20: Push duplicate "Y" and check search returns topmost occurrence
    stack.push("Y")
    if stack.search("Y") == 1:
        print("Test 20 passed: search returned 1 for duplicate Y at top")
        passed += 1
    else:
        print("Test 20 failed: search did not return correct position for duplicate Y")
        failed += 1

    # Test 21: Pop returns "Y" and next peek is "Y"
    if stack.pop() == "Y" and stack.peek() == "Y":
        print("Test 21 passed: duplicate Y handling is correct after pop")
        passed += 1
    else:
        print("Test 21 failed: duplicate Y handling failed after pop")
        failed += 1

    # Test 22: Push "M" and check push returns "M"
    if stack.push("M") == "M":
        print("Test 22 passed: push() returned M")
        passed += 1
    else:
        print("Test 22 failed: push() did not return M")
        failed += 1

    # Test 23: Peek returns "M"
    if stack.peek() == "M":
        print("Test 23 passed: peek() returned M")
        passed += 1
    else:
        print("Test 23 failed: peek() did not return M")
        failed += 1

    # Test 24: Pop "M" and then try pop on empty stack (after clearing remaining elements)
    try:
        stack.pop()  # pops M
        stack.pop()
        stack.pop()
        stack.pop()
        print("Test 24 failed: pop() did not raise exception on empty stack after clearing")
        failed += 1
    except IndexError:
        print("Test 24 passed: pop() raised exception on empty stack after clearing")
        passed += 1

    # Test 25: Verify stack is empty
    if stack.empty():
        print("Test 25 passed: empty() returned True for cleared stack")
        passed += 1
    else:
        print("Test 25 failed: empty() did not return True for cleared stack")
        failed += 1

    print("Total tests passed:", passed)
    print("Total tests failed:", failed)

main()

