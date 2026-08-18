import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)

    def bfs(src):
        dist = [-1]*(n+1)
        dist[src] = 0
        q = deque([src])
        far = src
        while q:
            u = q.popleft()
            if dist[u] > dist[far]:
                far = u
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return far, dist

    a, _ = bfs(1)
    b, dist = bfs(a)
    length = dist[b]

    sys.stdout.write(f"{length}\n{a} {b}\n")

main()