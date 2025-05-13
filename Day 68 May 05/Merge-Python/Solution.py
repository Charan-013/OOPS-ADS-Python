R = 256

def char_at(s, d):
    return ord(s[d]) if d < len(s) else -1

def insertion_sort(a, lo, hi, d):
    for i in range(lo + 1, hi + 1):
        temp = a[i]
        j = i
        while j > lo and a[j - 1][d:] > temp[d:]:
            a[j] = a[j - 1]
            j -= 1
        a[j] = temp

def msd_sort(a):
    aux = [None] * len(a)
    _msd_sort(a, 0, len(a) - 1, 0, aux)

def _msd_sort(a, lo, hi, d, aux):
    if hi <= lo + 15:
        insertion_sort(a, lo, hi, d)
        return

    count = [0] * (R + 2)
    for i in range(lo, hi + 1):
        c = char_at(a[i], d)
        count[c + 2] += 1

    for r in range(R + 1):
        count[r + 1] += count[r]

    for i in range(lo, hi + 1):
        c = char_at(a[i], d)
        aux[count[c + 1]] = a[i]
        count[c + 1] += 1

    for i in range(lo, hi + 1):
        a[i] = aux[i - lo]

    for r in range(R):
        _msd_sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1, aux)

def main():
    l1 = []
    try:
        while True:
            inp = input().strip()
            if inp:
                l1.extend(inp.split())
    except EOFError:
        pass

    msd_sort(l1)

    for word in l1:
        print(word)

if __name__ == "__main__":
    main()
