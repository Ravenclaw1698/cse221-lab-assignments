import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    vals = list(map(int, data))
    idx = 0
    n = vals[idx]; m = vals[idx+1]; s = vals[idx+2]; d = vals[idx+3]
    idx += 4

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

    NP1 = n + 1
    INF = float('inf')
    dist1 = [INF]*(n+1)
    dist2 = [INF]*(n+1)
    dist1[s] = 0
    heap = [s]  # encode as nd*NP1 + v, initial nd=0
    push = heapq.heappush
    pop = heapq.heappop

    d_pop_count = 0

    while heap:
        key = pop(heap)
        u = key % NP1
        du = key // NP1
        if du > dist2[u]:
            continue
        if u == d:
            d_pop_count += 1
            if d_pop_count == 2:
                break
        st = start[u]
        en = start[u+1]
        for k in range(st, en):
            v = adj_to[k]
            w = adj_w[k]
            nd = du + w
            d1v = dist1[v]
            if nd < d1v:
                d2v = d1v
                dist2[v] = d2v
                dist1[v] = nd
                push(heap, nd*NP1 + v)
                if d2v < INF:
                    push(heap, d2v*NP1 + v)
            elif nd > d1v and nd < dist2[v]:
                dist2[v] = nd
                push(heap, nd*NP1 + v)

    if dist2[d] == INF:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(dist2[d]) + "\n")

main()