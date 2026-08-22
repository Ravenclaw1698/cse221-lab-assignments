import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    vals = list(map(int, data))
    idx = 0
    n = vals[idx]; m = vals[idx+1]
    idx += 2

    us = vals[idx:idx+3*m:3]
    vs = vals[idx+1:idx+3*m:3]
    ws = vals[idx+2:idx+3*m:3]
    idx += 3*m

    deg = [0]*(n+2)
    for i in range(m):
        deg[us[i]] += 1
        deg[vs[i]] += 1

    start = [0]*(n+2)
    acc = 0
    for i in range(1, n+1):
        start[i] = acc
        acc += deg[i]
    start[n+1] = acc

    adj_to = [0]*(2*m)
    adj_w = [0]*(2*m)
    fill_pos = start[:]
    for i in range(m):
        u = us[i]; v = vs[i]; w = ws[i]
        p = fill_pos[u]
        adj_to[p] = v
        adj_w[p] = w
        fill_pos[u] = p + 1
        p = fill_pos[v]
        adj_to[p] = u
        adj_w[p] = w
        fill_pos[v] = p + 1

    INF = float('inf')
    dist = [INF]*(n+1)
    dist[1] = 0
    heap = [(0, 1)]
    push = heapq.heappush
    pop = heapq.heappop

    while heap:
        du, u = pop(heap)
        if du > dist[u]:
            continue
        st = start[u]
        en = start[u+1]
        for k in range(st, en):
            v = adj_to[k]
            w = adj_w[k]
            nd = w if w > du else du
            if nd < dist[v]:
                dist[v] = nd
                push(heap, (nd, v))

    out = []
    for i in range(1, n+1):
        out.append(str(dist[i]) if dist[i] != INF else "-1")

    sys.stdout.write(" ".join(out) + "\n")

main()