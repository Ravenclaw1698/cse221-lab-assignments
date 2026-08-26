import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    INF = 1 << 62
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); idx += 2
        us = [0]*m
        vs = [0]*m
        ws = [0]*m
        for i in range(m):
            us[i] = int(data[idx]); vs[i] = int(data[idx+1]); ws[i] = int(data[idx+2])
            idx += 3

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

        dist = [INF]*(n+1)
        dist[1] = 0
        in_queue = [False]*(n+1)
        in_queue[1] = True
        q = deque([1])

        while q:
            u = q.popleft()
            in_queue[u] = False
            du = dist[u]
            st = start[u]
            en = start[u+1]
            for k in range(st, en):
                v = adj_to[k]
                nd = du + adj_w[k]
                if nd < dist[v]:
                    dist[v] = nd
                    if not in_queue[v]:
                        in_queue[v] = True
                        q.append(v)

        out.append(str(dist[n]))

    sys.stdout.write("\n".join(out) + "\n")

main()