
from Solution import MyQueue, FullQueueException

def main():
    passed = 0
    failed = 0
    queue = MyQueue(3)
    
    # Test 1: peek() on empty queue returns None.
    if queue.peek() is None:
        print("Test 1 passed")
        passed += 1
    else:
        print("Test 1 failed: peek() on empty queue should return None")
        failed += 1
    
    # Test 2: poll() on empty queue returns None.
    if queue.poll() is None:
        print("Test 2 passed")
        passed += 1
    else:
        print("Test 2 failed: poll() on empty queue should return None")
        failed += 1
    
    # Test 3: element() on empty queue raises exception.
    try:
        queue.element()
        print("Test 3 failed: element() should raise exception on empty queue")
        failed += 1
    except IndexError:
        print("Test 3 passed: element() raised exception on empty queue")
        passed += 1
    
    # Test 4: remove() on empty queue raises exception.
    try:
        queue.remove()
        print("Test 4 failed: remove() should raise exception on empty queue")
        failed += 1
    except IndexError:
        print("Test 4 passed: remove() raised exception on empty queue")
        passed += 1
    
    # Test 5: add() "A" should return True.
    try:
        if queue.add("A"):
            print("Test 5 passed: add() returned True for element A")
            passed += 1
        else:
            print("Test 5 failed: add() did not return True for element A")
            failed += 1
    except Exception:
        print("Test 5 failed: add() raised exception for element A")
        failed += 1
    
    # Test 6: element() returns "A".
    if queue.element() == "A":
        print("Test 6 passed: element() returned A")
        passed += 1
    else:
        print("Test 6 failed: element() did not return A")
        failed += 1
    
    # Test 7: peek() returns "A".
    if queue.peek() == "A":
        print("Test 7 passed: peek() returned A")
        passed += 1
    else:
        print("Test 7 failed: peek() did not return A")
        failed += 1
    
    # Test 8: offer() should add "B" and return True.
    if queue.offer("B"):
        print("Test 8 passed: offer() returned True for element B")
        passed += 1
    else:
        print("Test 8 failed: offer() did not return True for element B")
        failed += 1
    
    # Test 9: offer() should add "C" and return True.
    if queue.offer("C"):
        print("Test 9 passed: offer() returned True for element C")
        passed += 1
    else:
        print("Test 9 failed: offer() did not return True for element C")
        failed += 1
    
    # Queue is now full.
    # Test 10: add() should raise exception when full.
    try:
        queue.add("D")
        print("Test 10 failed: add() should raise exception on full queue")
        failed += 1
    except FullQueueException:
        print("Test 10 passed: add() raised exception on full queue")
        passed += 1
    
    # Test 11: offer() should return False when full.
    if not queue.offer("D"):
        print("Test 11 passed: offer() returned False on full queue")
        passed += 1
    else:
        print("Test 11 failed: offer() did not return False on full queue")
        failed += 1
    
    # Test 12: element() should still return "A".
    if queue.element() == "A":
        print("Test 12 passed: element() still returned A")
        passed += 1
    else:
        print("Test 12 failed: element() did not return A")
        failed += 1
    
    # Test 13: remove() should remove and return "A".
    if queue.remove() == "A":
        print("Test 13 passed: remove() returned A")
        passed += 1
    else:
        print("Test 13 failed: remove() did not return A")
        failed += 1
    
    # Test 14: poll() should remove and return "B".
    if queue.poll() == "B":
        print("Test 14 passed: poll() returned B")
        passed += 1
    else:
        print("Test 14 failed: poll() did not return B")
        failed += 1
    
    # Test 15: Now queue should have one element "C"; element() returns "C".
    if queue.element() == "C":
        print("Test 15 passed: element() returned C")
        passed += 1
    else:
        print("Test 15 failed: element() did not return C")
        failed += 1
    
    # Test 16: remove() should remove and return "C".
    if queue.remove() == "C":
        print("Test 16 passed: remove() returned C")
        passed += 1
    else:
        print("Test 16 failed: remove() did not return C")
        failed += 1
    
    # Queue is empty now.
    # Test 17: peek() returns None.
    if queue.peek() is None:
        print("Test 17 passed: peek() returned None on empty queue")
        passed += 1
    else:
        print("Test 17 failed: peek() did not return None on empty queue")
        failed += 1
    
    # Test 18: poll() returns None.
    if queue.poll() is None:
        print("Test 18 passed: poll() returned None on empty queue")
        passed += 1
    else:
        print("Test 18 failed: poll() did not return None on empty queue")
        failed += 1
    
    # Test 19: element() raises exception.
    try:
        queue.element()
        print("Test 19 failed: element() should raise exception on empty queue")
        failed += 1
    except IndexError:
        print("Test 19 passed: element() raised exception on empty queue")
        passed += 1
    
    # Test 20: remove() raises exception.
    try:
        queue.remove()
        print("Test 20 failed: remove() should raise exception on empty queue")
        failed += 1
    except IndexError:
        print("Test 20 passed: remove() raised exception on empty queue")
        passed += 1
    
    # Test 21: offer() to add "X", then poll() returns "X".
    if queue.offer("X"):
        if queue.poll() == "X":
            print("Test 21 passed: offer() and poll() worked correctly for X")
            passed += 1
        else:
            print("Test 21 failed: poll() did not return X after offer()")
            failed += 1
    else:
        print("Test 21 failed: offer() did not add element X")
        failed += 1
    
    # Test 22: Add two elements ("Y", "Z") and check order.
    queue.offer("Y")
    queue.offer("Z")  # Now queue: Y, Z.
    if queue.element() == "Y" and queue.remove() == "Y" and queue.element() == "Z":
        print("Test 22 passed: Queue order maintained correctly")
        passed += 1
    else:
        print("Test 22 failed: Queue order not maintained correctly")
        failed += 1
    
    # Test 23: Fill queue with capacity 3: add "P", "Q", "R".
    queue = MyQueue(3)
    queue.add("P")
    queue.add("Q")
    queue.add("R")
    try:
        queue.add("S")
        print("Test 23 failed: add() should raise exception when queue is full")
        failed += 1
    except FullQueueException:
        print("Test 23 passed: add() raised exception when queue is full")
        passed += 1
    
    # Test 24: offer() should return False on full queue.
    if not queue.offer("S"):
        print("Test 24 passed: offer() returned False when queue is full")
        passed += 1
    else:
        print("Test 24 failed: offer() did not return False when queue is full")
        failed += 1
    
    # Test 25: After removals, verify queue functions correctly.
    queue.remove()  # removes "P"
    queue.remove()  # removes "Q", leaving "R".
    if queue.peek() == "R":
        print("Test 25 passed: Queue functions correctly after removals")
        passed += 1
    else:
        print("Test 25 failed: Queue did not function correctly after removals")
        failed += 1
    
    print("Total tests passed:", passed)
    print("Total tests failed:", failed)

main()
