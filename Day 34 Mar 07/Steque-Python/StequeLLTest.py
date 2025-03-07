from Solution import Steque

def main():
    steque = Steque()
    count = 0

    # Test case 1: push one element.
    steque.push("A")
    if str(steque) == "[A]" and steque.size() == 1:
        print("Test case 1 passed")
        count += 1
    else:
        print("Test case 1 failed")

    # Test case 2: push another element.
    steque.push("B")
    if str(steque) == "[B][A]" and steque.size() == 2:
        print("Test case 2 passed")
        count += 1
    else:
        print("Test case 2 failed")

    # Test case 3: enqueue element.
    steque.enqueue("C")
    if str(steque) == "[B][A][C]" and steque.size() == 3:
        print("Test case 3 passed")
        count += 1
    else:
        print("Test case 3 failed")

    # Test case 4: pop element.
    popped = steque.pop()
    if popped == "B" and str(steque) == "[A][C]" and steque.size() == 2:
        print("Test case 4 passed")
        count += 1
    else:
        print("Test case 4 failed")

    # Test case 5: pop again.
    popped = steque.pop()
    if popped == "A" and str(steque) == "[C]" and steque.size() == 1:
        print("Test case 5 passed")
        count += 1
    else:
        print("Test case 5 failed")

    # Test case 6: pop last element.
    popped = steque.pop()
    if popped == "C" and str(steque) == "Steque is empty" and steque.size() == 0:
        print("Test case 6 passed")
        count += 1
    else:
        print("Test case 6 failed")

    # Test case 7: mix of enqueue and push.
    steque.enqueue("D")  # steque: [D]
    steque.push("E")     # steque: [E][D]
    steque.enqueue("F")  # steque: [E][D][F]
    if str(steque) == "[E][D][F]" and steque.size() == 3:
        print("Test case 7 passed")
        count += 1
    else:
        print("Test case 7 failed")

    print("Total testcases passed:", count)

main()
