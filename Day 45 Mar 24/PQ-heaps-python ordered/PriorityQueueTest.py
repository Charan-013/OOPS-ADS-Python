
from Solution import BinaryHeapPriorityQueue


if __name__ == '__main__':
    pq = BinaryHeapPriorityQueue()

    # Test offer/add (adding elements to the heap)
    pq.offer(5)
    pq.add(3)
    pq.offer(9)
    pq.add(1)  # Expected minimum element: 1

    if pq.size() == 4:
        print("Size method works correctly.")
    else:
        print("Size method error.")

    if pq.contains(3):
        print("Contains method works correctly for existing element.")
    else:
        print("Contains method error.")

    if pq.peek() is not None and pq.peek() == 1:
        print("Peek method works correctly.")
    else:
        print("Peek method error.")

    first_poll = pq.poll()
    if first_poll is not None and first_poll == 1 and pq.size() == 3:
        print("Poll method works correctly.")
    else:
        print("Poll method error.")

    if pq.remove(3) and not pq.contains(3):
        print("Remove method works correctly.")
    else:
        print("Remove method error.")

    pq.clear()
    if pq.size() == 0:
        print("Clear method works correctly.")
    else:
        print("Clear method error.")

    # Test iterator by adding new elements
    pq.offer(7)
    pq.offer(2)
    pq.offer(8)
    print("Iterator method output: ", end="")
    for item in pq.iterator():
        print(item, end=" ")
    print()