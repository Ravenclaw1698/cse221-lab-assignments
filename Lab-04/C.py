import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        k = int(data[idx]); idx += 1
        for _ in range(k):
            j = int(data[idx]); idx += 1
            matrix[i][j] = 1

    out = []
    for row in matrix:
        out.append(' '.join(map(str, row)))
    print('\n'.join(out))

if __name__ == "__main__":
    main()