import sys
from collections import deque

def bfs(start, n, adj):
    dist = [-1] * (n + 1)
    parent = [0] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        du = dist[u]
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = du + 1
                parent[v] = u
                q.append(v)
    return dist, parent

def build_path(parent, start, end):
    path = [end]
    cur = end
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()
    return path

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    s = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)

    dist_s, parent_s = bfs(s, n, adj)
    dist_k, parent_k = bfs(k, n, adj)

    if dist_s[k] == -1 or dist_k[d] == -1:
        sys.stdout.write("-1")
        return

    path1 = build_path(parent_s, s, k)
    path2 = build_path(parent_k, k, d)
    full_path = path1 + path2[1:]
    total_len = dist_s[k] + dist_k[d]

    sys.stdout.write(str(total_len) + '\n' + ' '.join(map(str, full_path)))

if __name__ == "__main__":
    main()