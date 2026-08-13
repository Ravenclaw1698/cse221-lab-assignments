import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    us = list(map(int, data[idx:idx + m])); idx += m
    vs = list(map(int, data[idx:idx + m])); idx += m

    adj = [[] for _ in range(n + 1)]
    for u, v in zip(us, vs):
        adj[u].append(v)
        adj[v].append(u)
    for lst in adj:
        lst.sort()

    dist = [-1] * (n + 1)
    dist[d] = 0
    q = deque([d])
    while q:
        u = q.popleft()
        du = dist[u]
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = du + 1
                q.append(v)

    if dist[s] == -1:
        sys.stdout.write("-1")
        return

    path = [s]
    cur = s
    while cur != d:
        target = dist[cur] - 1
        for v in adj[cur]:
            if dist[v] == target:
                path.append(v)
                cur = v
                break

    out = []
    out.append(str(dist[s]))
    out.append(' '.join(map(str, path)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()