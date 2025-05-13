def lsd_radix_sort(strings):
    if not strings:
        return strings
    W = len(strings[0])
    R = 256
    aux = ["" for _ in strings]
    for d in range(W - 1, -1, -1):
        count = [0] * (R + 1)
        for s in strings:
            count[ord(s[d]) + 1] += 1
        for r in range(R):
            count[r + 1] += count[r]
        for s in strings:
            aux[count[ord(s[d])]] = s
            count[ord(s[d])] += 1
        for i in range(len(strings)):
            strings[i] = aux[i]
    return strings

def main():
    l1 = []
    l2 = []
    try:
        while True:
            inp = input().strip()
            if not inp:
                break
            if inp:
                l1.extend(inp.split())
    except:
        l2 = sorted(l1)
        if l1 and all(len(x) == len(l1[0]) for x in l1):
            lsd_radix_sort(l1)
        for i in l2:
            print(i)

main()