import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    vals = list(map(int, data))
    idx = 0
    n = vals[idx]; m = vals[idx+1]; s = vals[idx+2]; d = vals[idx+3]
    idx += 4

    us = vals[idx:idx+m]; idx += m
    vs = vals[idx:idx+m]; idx += m
    ws = vals[idx:idx+m]; idx += m

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

    INF = float('inf')
    dist = [INF]*(n+1)
    parent = [0]*(n+1)
    dist[s] = 0
    heap = [(0, s)]

    while heap:
        du, u = heapq.heappop(heap)
        if du > dist[u]:
            continue
        if u == d:
            break
        st = start[u]
        en = start[u+1]
        for k in range(st, en):
            v = adj_to[k]
            w = adj_w[k]
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(heap, (nd, v))

    if dist[d] == INF:
        sys.stdout.write("-1\n")
        return

    path = []
    cur = d
    while cur != s:
        path.append(cur)
        cur = parent[cur]
    path.append(s)
    path.reverse()

    sys.stdout.write(str(dist[d]) + "\n")
    sys.stdout.write(" ".join(map(str, path)) + "\n")

main()