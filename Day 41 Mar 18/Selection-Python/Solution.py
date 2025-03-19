def compare(ele1,ele2):
    if ele1 < ele2:
        return -1
    elif ele1 == ele2:
        return 0
    else:
        return 1

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if compare(arr[j], arr[min_idx]) == -1:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    try:
        l1 = []
        while True:
            inp = input()

            if not inp:
                break

            l1.append(inp)

        

    except EOFError:
        lst = selection_sort(l1)
        for ele in lst:
            print(ele.strip())
        pass

main()