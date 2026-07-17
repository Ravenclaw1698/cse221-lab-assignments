import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    u = [0] * m
    v = [0] * m
    for i in range(m):
        u[i] = int(data[idx]); idx += 1
    for i in range(m):
        v[i] = int(data[idx]); idx += 1

    degree = [0] * (n + 1)

    parent = list(range(n + 1))
    rank_ = [0] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank_[ra] < rank_[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank_[ra] == rank_[rb]:
            rank_[ra] += 1

    for i in range(m):
        a, b = u[i], v[i]
        degree[a] += 1
        degree[b] += 1
        if a != b:
            union(a, b)

    # check connectivity among vertices that have at least one edge
    root = -1
    connected = True
    for i in range(1, n + 1):
        if degree[i] > 0:
            r = find(i)
            if root == -1:
                root = r
            elif r != root:
                connected = False
                break

    odd_count = sum(1 for i in range(1, n + 1) if degree[i] % 2 == 1)

    if connected and (odd_count == 0 or odd_count == 2):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()