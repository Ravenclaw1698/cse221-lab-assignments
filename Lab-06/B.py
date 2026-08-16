import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)
    color = [-1]*(n+1)
    ans = 0
    for i in range(1, n+1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            cnt = [0, 0]
            cnt[0] += 1
            while q:
                u = q.popleft()
                for w in adj[u]:
                    if color[w] == -1:
                        color[w] = 1 - color[u]
                        cnt[color[w]] += 1
                        q.append(w)
            ans += max(cnt[0], cnt[1])
    sys.stdout.write(str(ans) + "\n")

main()