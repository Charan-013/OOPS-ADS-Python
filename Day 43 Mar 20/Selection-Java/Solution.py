def merge(l1,aux,lo,mid,hi):
    for k in range(lo,hi + 1):
        aux[k] = l1[k]
    
    i = lo
    j = mid + 1
    for k in range(lo,hi + 1):
        if i > mid:
            l1[k] = aux[j]
            j += 1
        elif j > hi:
            l1[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            l1[k] = aux[i]
            i += 1
        else:
            l1[k] = aux[j]
            j += 1

def mergesort(l1,aux,lo,hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    mergesort(l1,aux,lo,mid)
    mergesort(l1,aux,mid + 1,hi)
    merge(l1,aux,lo,mid,hi)

def sort(l1):
    aux = [0] * len(l1)
    mergesort(l1,aux,0,len(l1) - 1)
    return l1

def main():
    try:
        l1 = []
        while True:
            inp = input()
            if not inp:
                break
            l1.append(inp.strip())

            
    except EOFError:
        l1 = sort(l1)

        for ele in l1:
            print(ele)
        pass

main()
