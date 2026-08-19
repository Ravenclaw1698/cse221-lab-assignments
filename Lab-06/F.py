import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    S = data[idx].decode(); idx += 1
    C = data[idx].decode(); idx += 1
    n = int(data[idx]); idx += 1

    forbidden = [False]*10000
    for _ in range(n):
        f = data[idx].decode(); idx += 1
        forbidden[int(f)] = True

    s = int(S)
    c = int(C)

    if s == c:
        print(0)
        return

    dist = [-1]*10000
    dist[s] = 0
    q = deque([s])

    pw = [1000, 100, 10, 1]

    while q:
        u = q.popleft()
        du = dist[u] + 1
        digits = [u // 1000 % 10, u // 100 % 10, u // 10 % 10, u % 10]
        for pos in range(4):
            d = digits[pos]
            for delta in (1, 9):
                nd = (d + delta) % 10
                v = u + (nd - d) * pw[pos]
                if not forbidden[v] and dist[v] == -1:
                    dist[v] = du
                    if v == c:
                        print(du)
                        return
                    q.append(v)

    print(dist[c])

main()