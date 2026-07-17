import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    matrix = [[0] * n for _ in range(n)]

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        matrix[u - 1][v - 1] = w

    out = []
    for row in matrix:
        out.append(' '.join(map(str, row)))
    print('\n'.join(out))

if __name__ == "__main__":
    main()