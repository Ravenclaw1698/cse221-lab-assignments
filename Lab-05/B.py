import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    us = list(map(int, data[2:2 + m]))
    vs = list(map(int, data[2 + m:2 + 2 * m]))

    adj = [[] for _ in range(n + 1)]
    for u, v in zip(us, vs):
        adj[u].append(v)
        adj[v].append(u)

    visited = bytearray(n + 1)
    order = []
    order_append = order.append
    stack = [1]
    stack_append = stack.append
    stack_pop = stack.pop
    while stack:
        u = stack_pop()
        if visited[u]:
            continue
        visited[u] = 1
        order_append(u)
        for v in reversed(adj[u]):
            if not visited[v]:
                stack_append(v)

    sys.stdout.write(' '.join(map(str, order)))

if __name__ == "__main__":
    main()