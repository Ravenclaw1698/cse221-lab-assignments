import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1

    eu = [0]*M
    ev = [0]*M
    deg = [0]*(N+2)
    for i in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        eu[i] = u
        ev[i] = v
        deg[u] += 1
        deg[v] += 1

    start = [0]*(N+2)
    for i in range(1, N+1):
        start[i+1] = start[i] + deg[i]

    adj = [0]*(2*M)
    pos = start[:]
    for i in range(M):
        u = eu[i]; v = ev[i]
        adj[pos[u]] = v; pos[u] += 1
        adj[pos[v]] = u; pos[v] += 1

    dist = [-1]*(N+1)
    q = deque()
    for _ in range(S):
        s = int(data[idx]); idx += 1
        if dist[s] == -1:
            dist[s] = 0
            q.append(s)

    while q:
        u = q.popleft()
        du = dist[u] + 1
        for i in range(start[u], start[u+1]):
            v = adj[i]
            if dist[v] == -1:
                dist[v] = du
                q.append(v)

    out = []
    for _ in range(Q):
        d = int(data[idx]); idx += 1
        out.append(str(dist[d]))

    sys.stdout.write(' '.join(out) + '\n')

main()