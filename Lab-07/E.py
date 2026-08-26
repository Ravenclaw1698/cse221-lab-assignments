import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    vals = list(map(int, data))
    idx = 0
    n = vals[idx]; m = vals[idx+1]
    idx += 2

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
    adj_p = [0]*m
    fill_pos = start[:]
    for i in range(m):
        u = us[i]
        p = fill_pos[u]
        adj_to[p] = vs[i]
        adj_w[p] = ws[i]
        adj_p[p] = ws[i] & 1
        fill_pos[u] = p + 1

    # state = node*2 + parity(0/1) meaning parity of last edge used to arrive
    INF = float('inf')
    dist = [INF]*(2*(n+1))
    dist[1*2+0] = 0
    dist[1*2+1] = 0
    heap = [(0, 1, 0), (0, 1, 1)]
    push = heapq.heappush
    pop = heapq.heappop

    while heap:
        du, u, p = pop(heap)
        sidx = u*2 + p
        if du > dist[sidx]:
            continue
        st = start[u]
        en = start[u+1]
        for k in range(st, en):
            v = adj_to[k]
            wp = adj_p[k]
            if wp != p:
                nd = du + adj_w[k]
                nsidx = v*2 + wp
                if nd < dist[nsidx]:
                    dist[nsidx] = nd
                    push(heap, (nd, v, wp))

    ans = dist[n*2+0]
    b = dist[n*2+1]
    if b < ans:
        ans = b

    if ans == INF:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(ans) + "\n")

main()