import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); idx += 2
        adj = [[] for _ in range(n+1)]
        indeg = [0]*(n+1)
        for _ in range(m):
            a = int(data[idx]); b = int(data[idx+1]); idx += 2
            adj[a].append(b)
            indeg[b] += 1
        q = deque([i for i in range(1, n+1) if indeg[i] == 0])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(order) < n:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")

main()