import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    vals = list(map(int, data))
    idx = 0
    n = vals[idx]; m = vals[idx+1]; s = vals[idx+2]; t = vals[idx+3]
    idx += 4

    us = vals[idx:idx+3*m:3]
    vs = vals[idx+1:idx+3*m:3]
    ws = vals[idx+2:idx+3*m:3]
    idx += 3*m

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
    adj_w = [0]*m
    fill_pos = start[:]
    for i in range(m):
        u = us[i]
        p = fill_pos[u]
        adj_to[p] = vs[i]
        adj_w[p] = ws[i]
        fill_pos[u] = p + 1

    push = heapq.heappush
    pop = heapq.heappop

    def dijkstra(src):
        INF = float('inf')
        dist = [INF]*(n+1)
        dist[src] = 0
        heap = [(0, src)]
        while heap:
            du, u = pop(heap)
            if du > dist[u]:
                continue
            st = start[u]
            en = start[u+1]
            for k in range(st, en):
                v = adj_to[k]
                w = adj_w[k]
                nd = du + w
                if nd < dist[v]:
                    dist[v] = nd
                    push(heap, (nd, v))
        return dist

    distS = dijkstra(s)
    distT = dijkstra(t)

    INF = float('inf')
    best_time = INF
    best_node = -1
    for i in range(1, n+1):
        a = distS[i]; b = distT[i]
        if a != INF and b != INF:
            c = a if a > b else b
            if c < best_time:
                best_time = c
                best_node = i

    if best_node == -1:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(f"{best_time} {best_node}\n")

main()