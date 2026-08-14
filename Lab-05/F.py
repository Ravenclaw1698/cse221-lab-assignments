import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1

    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]

    out = []
    for _ in range(q):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        out.append("YES" if find(x) == find(y) else "NO")

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()