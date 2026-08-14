import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    r = int(data[1])

    idx = 2
    edge_tokens = data[idx:idx + 2 * (n - 1)]
    idx += 2 * (n - 1)
    us = list(map(int, edge_tokens[0::2]))
    vs = list(map(int, edge_tokens[1::2]))

    adj = [[] for _ in range(n + 1)]
    for u, v in zip(us, vs):
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    visited = bytearray(n + 1)
    order = [0] * n
    visited[r] = 1
    order[0] = r
    head = 0
    cnt = 1
    while head < cnt:
        u = order[head]
        head += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = 1
                parent[v] = u
                order[cnt] = v
                cnt += 1

    size = [1] * (n + 1)
    for i in range(n - 1, 0, -1):
        u = order[i]
        size[parent[u]] += size[u]

    qcount = int(data[idx]); idx += 1
    queries = data[idx:idx + qcount]
    out = [str(size[int(x)]) for x in queries]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()