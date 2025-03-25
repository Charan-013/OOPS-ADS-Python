import random

def quickSort(l1,lo,hi):
    if lo >= hi:
        return l1
    p = partition(l1,lo,hi)
    quickSort(l1,lo,p - 1)
    quickSort(l1,p + 1,hi)
    return l1

def partition(l1,lo,hi):
    i = lo + 1
    j = hi
    v = l1[lo]
    while True:
        while i <= j and l1[i] <= v:
            i += 1
        while i <= j and l1[j] >= v:
            j -= 1
        if i <= j:
            l1[i], l1[j] = l1[j], l1[i] 
        else:
            break

    l1[lo], l1[j] = l1[j], l1[lo]  
    return j

def main():
    l1 = []
    try:
        while True:
            inp = input().strip()
            if inp :
                l1.extend(inp.split())
    except:
        quickSort(l1,0,len(l1) - 1)
        for i in l1:
            print(i)


main()