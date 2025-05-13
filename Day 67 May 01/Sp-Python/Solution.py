def to_negative_log(x):
    ln = 0.0
    y = (x - 1) / (x + 1)
    y2 = y * y
    frac = y
    i = 1
    while i < 100:
        ln += frac / i
        frac *= y2
        i += 2
    return -2 * ln

def detect_arbitrage():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, r = input().split()
        a, b = int(a) - 1, int(b) - 1
        rate = float(r)
        edges.append((a, b, to_negative_log(rate)))

    dist = [1e9] * N
    dist[0] = 0.0

    for _ in range(N - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Arbitrage Opportunity Detected")
            return

    print("No Arbitrage Opportunity")

detect_arbitrage()
