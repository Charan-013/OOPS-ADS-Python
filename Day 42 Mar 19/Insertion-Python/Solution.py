def insertionSort(l1):
    for i in range(1,len(l1)):
        for j in range(i,0,-1):
            if compare(l1[j],l1[j-1]) == -1:
                l1[j],l1[j-1] = l1[j-1],l1[j]
            else:
                break
    return l1

def compare(ele1, ele2):
    if ele1 < ele2:
        return -1
    elif ele1 == ele2:
        return 0
    else:
        return 1


def main():
    l1 = []
    try:
        while True:
            inp = input().strip()

            if not inp:
                break

            l1.append(inp)

        
    except EOFError:
        l1 = insertionSort(l1)

        for ele in l1:
            print(ele)
        pass
main()
