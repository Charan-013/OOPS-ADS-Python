comp = 0
partitions_done = 0

def partition(a, lo, hi):
    global comp
    global partitions_done
    partitions_done += 1 
    
    pivot = a[lo]  
    i = lo + 1
    j = hi
    while True:
        while i <= j and a[i] <= pivot:
            comp += 1 
            i += 1
        while i <= j and a[j] >= pivot:
            comp += 1 
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i] 
        else:
            break

    a[lo], a[j] = a[j], a[lo]  
    return j

def quick_sort(a, lo, hi):
    if lo < hi:
        pi = partition(a, lo, hi)
        
        quick_sort(a, lo, pi - 1)  
        quick_sort(a, pi + 1, hi)  

def sort(a):
    global comp
    global partitions_done
    quick_sort(a, 0, len(a) - 1)
    return a


def main():
    lt = []
    try:
        while True:
            s = input().strip()
            # print(s)
            if s :
                lt.extend(s.split())
    except:
        sort(lt)
        for i in lt:
            print(i)
        
main()