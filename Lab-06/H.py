import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    A = data[idx].decode(); idx += 1
    B = data[idx].decode(); idx += 1

    adj = [set() for _ in range(26)]
    for _ in range(n):
        w = data[idx]; idx += 1
        f = w[0] - 65
        l = w[-1] - 65
        adj[f].add(l)

    if A == B:
        print("YES")
        return

    start = ord(A[-1]) - 65
    target_first = ord(B[0]) - 65

    visited = [False]*26
    visited[start] = True
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    print("YES" if visited[target_first] else "NO")

main()