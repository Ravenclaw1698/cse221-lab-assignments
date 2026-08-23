import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    vals = list(map(int, data))
    idx = 0
    n = vals[idx]; m = vals[idx+1]; s = vals[idx+2]; d = vals[idx+3]
    idx += 4

    w = vals[idx:idx+n]
    idx += n
    w = [0] + w  # 1-indexed

    us = vals[idx:idx+2*m:2]
    vs = vals[idx+1:idx+2*m:2]
    idx += 2*m

    deg = [0]*(n+2)
    for i in range(m):
        deg[us[i]] += 1

    start = [0]*(n+2)
    acc = 0
    for i in range(1, n+1):
        start[i] = acc
        acc += deg[i]
    start[n+1] = acc

    adj_to = [0]*m
    fill_pos = start[:]
    for i in range(m):
        u = us[i]
        p = fill_pos[u]
        adj_to[p] = vs[i]
        fill_pos[u] = p + 1

    INF = float('inf')
    dist = [INF]*(n+1)
    dist[s] = w[s]
    heap = [(w[s], s)]
    push = heapq.heappush
    pop = heapq.heappop

    while heap:
        du, u = pop(heap)
        if du > dist[u]:
            continue
        if u == d:
            break
        st = start[u]
        en = start[u+1]
        for k in range(st, en):
            v = adj_to[k]
            nd = du + w[v]
            if nd < dist[v]:
                dist[v] = nd
                push(heap, (nd, v))

    if dist[d] == INF:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(dist[d]) + "\n")

main()