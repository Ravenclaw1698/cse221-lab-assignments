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

    indeg = [0] * (n + 1)
    outdeg = [0] * (n + 1)

    for i in range(m):
        outdeg[u[i]] += 1
        indeg[v[i]] += 1

    result = [str(indeg[i] - outdeg[i]) for i in range(1, n + 1)]
    print(' '.join(result))

if __name__ == "__main__":
    main()